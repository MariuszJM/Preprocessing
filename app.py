from flask import Flask, request, jsonify
from flask_cors import CORS  # You need to install this package if not already installed

app = Flask(__name__)
CORS(app)  # This will allow CORS for all routes

test_cycles_data = {
    "test_cycle1": ["scenario1", "scenario2"],
    "test_cycle2": ["scenario3", "scenario4"]
}
existing_data = {
    "test_cycle1": ["scenario2"]
}

@app.route('/prepare-data-fed', methods=['POST'])
def prepare_data_fed():
    data = request.json
    output_csv = data.get('output_csv')
    mapping_file = data.get('mapping_file')
    fed_csv_files = data.get('fed_csv_files')
    response_message = "FED files processing completed."
    return jsonify({"message": response_message}), 200

@app.route('/get-test-cycles', methods=['GET'])
def get_test_cycles():
    # Here would be the logic for fetching available test cycles and scenarios from the database

    return jsonify(test_cycles_data), 200

@app.route('/get-existing-data', methods=['GET'])
def get_existing_data():
    # Here would be the logic for checking existing data

    return jsonify(existing_data), 200

@app.route('/prepare-data-db', methods=['POST'])
def prepare_data_db():
    data = request.json
    selected_test_cycles = data.get('selected_test_cycles')  # Dictionary with selected test cycles and scenarios
    output_csv = data.get('output_csv')

    response_message = "Data preparation from the database completed."
    return jsonify({"message": response_message}), 200

if __name__ == '__main__':
    app.run(debug=True)
