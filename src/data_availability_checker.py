import os


def get_test_cycles_and_scenarios_from_file(file_path):
    if os.path.exists(file_path):
        return {
            "test_cycle1": ["scenario1", "scenario2"],
            "test_cycle2": ["scenario3", "scenario4"]
        }
    return {}


def get_test_cycles_and_scenarios_from_db():
    """Return a mapping of test cycles to their respective scenarios from the database."""
    # Logic to retrieve available test cycles and scenarios from the database
    return {
        "test_cycle1": ["scenario1", "scenario2"],
        "test_cycle2": ["scenario3", "scenario4"]
    }
