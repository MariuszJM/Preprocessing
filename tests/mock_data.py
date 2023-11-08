import pandas as pd

initial_data = {
    'config': {
        'CHART_CATEGORY': 'FED',
        'TEST_CYCLE': 'CCAR_2023',
        'SCENARIOS_MAPPING': {
            'Actual': 'Historic',
            'Supervisory Internal Baseline': 'Internal Baseline',
            'Supervisory Severely Adverse': 'Severely Adverse'
        },
        'FILE_NAME_MAPPING': {
            'ECONOMIC_SCOPES': {
                'Domestic': 'domestic',
                'International': 'international'
            }
        },
        'VARIABLE_NUMBER_2_CAR_VARIABLE_NAME': {
            153: 'Euro Zone - National Accounts: Real GDP, (bill. 2010 EUR, CADARSAAR), Ann. % Ch_Stock'
        }
    },
    'data': {
        '2023-table_1b_historic_international.csv': pd.DataFrame({
            'Scenario name': ['Actual'] * 8,
            'DATE': ['2021 Q1', '2021 Q2', '2021 Q3', '2021 Q4', '2022 Q1', '2022 Q2', '2022 Q3', '2022 Q4'],
            'Euro area real GDP growth': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        }),
        '2023-table_2b_supervisory_baseline_international.csv': pd.DataFrame({
            'Scenario name': ['Supervisory Internal Baseline'] * 8,
            'DATE': ['2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3'],
            'Euro area real GDP growth': [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        }),
        '2023-table_3b_supervisory_severely_adverse_international.csv': pd.DataFrame({
            'Scenario name': ['Supervisory Severely Adverse'] * 8,
            'DATE': ['2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3'],
            'Euro area real GDP growth': [0.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
        })
    },
    'mapping': {
        'Domestic': {
            '627-834': 'Corporate Spreads',
            751: 'Real GDP growth'
        },
        'International': {
            153: 'Euro area real GDP growth',
            164: 'Euro area bilateral dollar exchange rate (USD/euro)'
        }
    }
}


renamed_columns_data = {
        '2023-table_1b_historic_international.csv': pd.DataFrame({
            'Scenario name': ['Actual'] * 8,
            'AS OF DATE': ['2021 Q1', '2021 Q2', '2021 Q3', '2021 Q4', '2022 Q1', '2022 Q2', '2022 Q3', '2022 Q4'],
            'Euro area real GDP growth': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        }),
        '2023-table_2b_supervisory_baseline_international.csv': pd.DataFrame({
            'Scenario name': ['Supervisory Internal Baseline'] * 8,
            'AS OF DATE': ['2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3'],
            'Euro area real GDP growth': [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        }),
        '2023-table_3b_supervisory_severely_adverse_international.csv': pd.DataFrame({
            'Scenario name': ['Supervisory Severely Adverse'] * 8,
            'AS OF DATE': ['2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3'],
            'Euro area real GDP growth': [0.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
        })
    }

mapped_scenario_data = {
    '2023-table_1b_historic_international.csv': pd.DataFrame({
        'AS OF DATE': ['2021 Q1', '2021 Q2', '2021 Q3', '2021 Q4', '2022 Q1', '2022 Q2', '2022 Q3', '2022 Q4'],
        'Euro area real GDP growth': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'SCENARIO': ['Historic'] * 8,
    }),
    '2023-table_2b_supervisory_baseline_international.csv': pd.DataFrame({
        'AS OF DATE': ['2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3'],
        'Euro area real GDP growth': [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        'SCENARIO': ['Internal Baseline'] * 8,
    }),
    '2023-table_3b_supervisory_severely_adverse_international.csv': pd.DataFrame({
        'AS OF DATE': ['2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3'],
        'Euro area real GDP growth': [0.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0],
        'SCENARIO': ['Severely Adverse'] * 8,
    }),
}

melted_data = {
    '2023-table_1b_historic_international.csv': pd.DataFrame({
        'AS OF DATE': ['2021 Q1', '2021 Q2', '2021 Q3', '2021 Q4', '2022 Q1', '2022 Q2', '2022 Q3', '2022 Q4'],
        'SCENARIO': ['Historic']*8,
        'FED VARIABLE NAME': ['Euro area real GDP growth'] * 8,
        'INPUT VALUE': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    }),
    '2023-table_2b_supervisory_baseline_international.csv': pd.DataFrame({
        'AS OF DATE': ['2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3'],
        'SCENARIO': ['Internal Baseline']*8,
        'FED VARIABLE NAME': ['Euro area real GDP growth'] * 8,
        'INPUT VALUE': [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    }),
    '2023-table_3b_supervisory_severely_adverse_international.csv': pd.DataFrame({
        'AS OF DATE': ['2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3'],
        'SCENARIO': ['Severely Adverse']*8,
        'FED VARIABLE NAME': ['Euro area real GDP growth'] * 8,
        'INPUT VALUE': [0.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
    })
}


data_with_economic_scope = {
    '2023-table_1b_historic_international.csv': pd.DataFrame({
        'AS OF DATE': ['2021 Q1', '2021 Q2', '2021 Q3', '2021 Q4', '2022 Q1', '2022 Q2', '2022 Q3', '2022 Q4'],
        'SCENARIO': ['Historic']*8,
        'ECONOMIC SCOPE': ['International']*8,
        'FED VARIABLE NAME': ['Euro area real GDP growth'] * 8,
        'INPUT VALUE': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    }),
    '2023-table_2b_supervisory_baseline_international.csv': pd.DataFrame({
        'AS OF DATE': ['2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3'],
        'SCENARIO': ['Internal Baseline']*8,
        'ECONOMIC SCOPE': ['International'] * 8,
        'FED VARIABLE NAME': ['Euro area real GDP growth'] * 8,
        'INPUT VALUE': [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    }),
    '2023-table_3b_supervisory_severely_adverse_international.csv': pd.DataFrame({
        'AS OF DATE': ['2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3'],
        'SCENARIO': ['Severely Adverse']*8,
        'ECONOMIC SCOPE': ['International']*8,
        'FED VARIABLE NAME': ['Euro area real GDP growth'] * 8,
        'INPUT VALUE': [0.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
    })
}


merged_data = pd.DataFrame({
    'AS OF DATE': ['2021 Q1', '2021 Q2', '2021 Q3', '2021 Q4', '2022 Q1', '2022 Q2', '2022 Q3', '2022 Q4',
                   '2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3',
                   '2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3'],
    'ECONOMIC SCOPE': ['International'] * 24,
    'SCENARIO': ['Historic'] * 8 + ['Internal Baseline'] * 8 + ['Severely Adverse'] * 8,
    'FED VARIABLE NAME': ['Euro area real GDP growth'] * 24,
    'INPUT VALUE': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                    0.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
})


additional_columns_data = pd.DataFrame({
    'AS OF DATE': ['2021 Q1', '2021 Q2', '2021 Q3', '2021 Q4', '2022 Q1', '2022 Q2', '2022 Q3', '2022 Q4',
                   '2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3',
                   '2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3'],
    'ECONOMIC SCOPE': ['International'] * 24,
    'SCENARIO': ['Historic'] * 8 + ['Internal Baseline'] * 8 + ['Severely Adverse'] * 8,
    'FED VARIABLE NAME': ['Euro area real GDP growth'] * 24,
    'INPUT VALUE': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                    0.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0],
    'CHART CATEGORY': ['FED'] * 24,
    'TEST CYCLE': ['CCAR_2023'] * 24
})


final_data = pd.DataFrame({
    'AS OF DATE': ['2021 Q1', '2021 Q2', '2021 Q3', '2021 Q4', '2022 Q1', '2022 Q2', '2022 Q3', '2022 Q4',
                   '2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3',
                   '2022 Q4', '2023 Q1', '2023 Q2', '2023 Q3', '2023 Q4', '2024 Q1', '2024 Q2', '2024 Q3'],
    'ECONOMIC SCOPE': ['International'] * 24,
    'SCENARIO': ['Historic'] * 8 + ['Internal Baseline'] * 8 + ['Severely Adverse'] * 8,
    'FED VARIABLE NAME': ['Euro area real GDP growth'] * 24,
    'CAR VARIABLE NAME': ['Euro Zone - National Accounts: Real GDP, (bill. 2010 EUR, CADARSAAR), Ann. % Ch_Stock'] * 24,
    'INPUT VALUE': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                    0.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0],
    'CHART CATEGORY': ['FED'] * 24,
    'TEST CYCLE': ['CCAR_2023'] * 24,
    'VARIABLE NUMBER': [153] * 24
})
