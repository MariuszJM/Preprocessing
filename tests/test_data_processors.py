import pandas as pd
import pytest
from unittest.mock import patch
from data_processor.data_processor import FedDataProcessor
from mock_data import initial_data, renamed_columns_data, data_with_economic_scope, melted_data, merged_data, additional_columns_data, final_data, mapped_scenario_data


@pytest.fixture
def processor():
    with patch('data_processor.data_processor.FedDataProcessor._load_config') as mock_config:

        mock_config.return_value = initial_data['config']
        processor = FedDataProcessor("config.yml")
        processor.data = initial_data['data']
        processor.mapping = initial_data['mapping']
        return processor


class TestFedDataProcessor:

    def test_rename_date(self, processor):
        processor.data = initial_data['data'].copy()
        processor._rename_date()

        for name, df in processor.data.items():
            pd.testing.assert_frame_equal(df, renamed_columns_data[name], check_like=True, check_dtype=False)

    def test_map_scenario(self, processor):
        processor.data = renamed_columns_data.copy()
        processor._map_scenario()

        for name, df in processor.data.items():
            pd.testing.assert_frame_equal(df, mapped_scenario_data[name], check_like=True, check_dtype=False)

    def test_melt_data(self, processor):
        processor.data = mapped_scenario_data.copy()
        processor._melt_data()
        for name, df in processor.data.items():
            pd.testing.assert_frame_equal(df, melted_data[name], check_like=True, check_dtype=False)

    def test_add_economic_scope(self, processor):
        processor.data = melted_data.copy()
        processor._add_economic_scope()

        for name, df in processor.data.items():
            pd.testing.assert_frame_equal(df, data_with_economic_scope[name], check_like=True, check_dtype=False)

    def test_merge_dataframes(self, processor):
        processor.data = melted_data.copy()
        processor._merge_dataframes()

        pd.testing.assert_frame_equal(processor.data, merged_data, check_like=True, check_dtype=False)

    def test_add_additional_columns(self, processor):
        processor.data = merged_data.copy()
        processor._add_additional_columns()

        pd.testing.assert_frame_equal(processor.data, additional_columns_data, check_like=True, check_dtype=False)

    def test_map_and_add_columns(self, processor):
        processor.data = additional_columns_data.copy()
        processor._map_and_add_columns()

        pd.testing.assert_frame_equal(processor.data, final_data, check_like=True, check_dtype=False)