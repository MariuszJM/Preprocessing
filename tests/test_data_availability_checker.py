import unittest

from src.utils import get_test_cycles_and_scenarios_from_file


class TestGetDataFromCSV(unittest.TestCase):

    def setUp(self):
        self.test_output_file = 'test_output.csv'

    def test_get_test_cycles_and_scenarios_from_file(self):
        expected_output = {'CCAR_2023': ['Historic', 'Internal Baseline', 'Severely Adverse']}
        result = get_test_cycles_and_scenarios_from_file(self.test_output_file)
        self.assertEqual(result, expected_output, "The function did not return the expected dictionary structure.")

    def test_get_test_cycles_and_scenarios_from_file_nonexistent(self):
        result = get_test_cycles_and_scenarios_from_file('nonexistent_file.csv')
        self.assertEqual(result, {}, "The function should return an empty dictionary for non-existent files.")
