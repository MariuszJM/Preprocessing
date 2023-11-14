from abc import ABC, abstractmethod
import pandas as pd
import yaml
import os


class AbstractDataProcessor(ABC):
    """
    Abstract class for data processing.
    """

    @abstractmethod
    def process(self, *args, **kwargs):
        pass

    @abstractmethod
    def save(self, processed_data, destination):
        pass


class FedDataProcessor(AbstractDataProcessor):
    """
    Class for processing data from CSV files.
    """

    def __init__(self, config_file):
        self.config = self._load_config(config_file)
        self.data = None
        self.mapping = None

    def process(self, csv_file_paths, mapping_file_path):
        self.data = self._load_csv_files(csv_file_paths)
        self.mapping = self._load_yaml(mapping_file_path)

        self._prepare_data()
        return self.data

    def save(self, processed_data, destination):
        processed_data.to_csv(destination, index=False)

    def _load_config(self, file):
        with open(file, 'r') as f:
            return yaml.safe_load(f)

    def _load_csv_files(self, paths):
        return {os.path.basename(path): pd.read_csv(path) for path in paths}

    def _load_yaml(self, file):
        with open(file, 'r') as f:
            return yaml.safe_load(f)

    def _prepare_data(self):
        self._rename_date()
        self._map_scenario()
        self._melt_data()
        self._add_economic_scope()
        self._merge_dataframes()
        self._add_additional_columns()
        self._map_and_add_columns()

    def _rename_date(self):
        for df in self.data.values():
            df.rename(columns={"DATE": "AS OF DATE"}, inplace=True)

    def _map_scenario(self):
        for name, data in self.data.items():
            data['Scenario name'] = data['Scenario name'].map(
                self.config.get('SCENARIOS_MAPPING'))
            data.rename(columns={"Scenario name": "SCENARIO"}, inplace=True)

    def _add_economic_scope(self):
        for name, data in self.data.items():
            domestic_variables = set(self.mapping.get('Domestic', {}).values())
            international_variables = set(self.mapping.get('International', {}).values())

            def get_scope(variable):
                if variable in international_variables:
                    return 'International'
                elif variable in domestic_variables:
                    return 'Domestic'
                else:
                    return 'Unknown'

            data['ECONOMIC SCOPE'] = data.apply(lambda row: get_scope(row['FED VARIABLE NAME']), axis=1)

    def _melt_data(self):
        self.data = {
            name: pd.melt(df, id_vars=["AS OF DATE", 'SCENARIO'],
                          var_name="FED VARIABLE NAME", value_name="INPUT VALUE")
            for name, df in self.data.items()
        }

    def _merge_dataframes(self):
        self.data = pd.concat(self.data.values(), ignore_index=True)

    def _add_additional_columns(self):
        self.data['CHART CATEGORY'] = 'FED'
        self.data['TEST CYCLE'] = 'CCAR_2023'

    def _map_and_add_columns(self):
        flattened_mapping = {k: v for mappings in self.mapping.values() for k, v in mappings.items()}
        reverse_mapping = {v: k for k, v in flattened_mapping.items()}

        self.data['VARIABLE NUMBER'] = self.data['FED VARIABLE NAME'].map(reverse_mapping)
        self.data['CAR VARIABLE NAME'] = self.data['VARIABLE NUMBER'].map(
            self.config.get('VARIABLE_NUMBER_2_CAR_VARIABLE_NAME'))
