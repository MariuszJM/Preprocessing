from src.fed_data_processor import FedDataProcessor


def main():
    config_file = './config/config.yaml'
    csv_file_paths = ['./data/2023-table_1b_historic_international.csv',
                      './data/2023-table_2b_supervisory_baseline_international.csv',
                      './data/2023-table_3b_supervisory_severely_adverse_international.csv']
    mapping_file_path = './config/mapping.yaml'

    processor = FedDataProcessor(config_file)
    processed_data = processor.process(csv_file_paths, mapping_file_path)

    print(processed_data)

    # processor.save(processed_data, 'processed_data.csv')

if __name__ == "__main__":
    main()
    print('test')
