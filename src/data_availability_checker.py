import os
import pandas as pd


def get_test_cycles_and_scenarios_from_file(output_file):
    """
    Retrieve the structure of test cycles and their associated scenarios from a CSV file.

    :param output_file: The path to the output CSV file.
    :return: A dictionary with test cycles as keys and lists of scenarios as values.
    """
    if os.path.exists(output_file):
        df = pd.read_csv(output_file)
        test_cycles_scenarios = df.groupby('TEST CYCLE')['SCENARIO'].unique().to_dict()
        test_cycles_scenarios = {tc: scenarios.tolist() for tc, scenarios in test_cycles_scenarios.items()}
        return test_cycles_scenarios
    else:
        return {}


def get_available_test_cycles_and_scenarios_from_db():
    test_cycles = read_available_test_cycles()
    data_structure = {}
    for test_cycle in test_cycles:
        scenarios_df = get_scenario(test_cycle)
        scenarios = scenarios_df['SCENARIO'].unique().tolist() if not scenarios_df.empty else []
        data_structure[test_cycle] = scenarios
    return data_structure
