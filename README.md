"# DS3500---MP1 Data Pipeline---Maximus-Vo" 

#This pipeline loads csv file, validates it, cleans it, and saves the result
#this is all controlled by a yaml config file "pipeline.py"
#the filepath is checked, data is loaded, and then passes through the data.

#src/data_loaders.py reads csv, JSOn, and YAML files
#src/data_validator.py` checks that required columns exist and removes rows with invalid numeric values.
#src/data_processor.py` then removes duplicates, missing values, and outliers based on the settings in the config. 
#src/data_output.py` saves the cleaned data to a csv
#src/utils.py` holds the logging setup and path validation. 
#All settings live in config/config.yaml, so a new dataset only needs config changes, not code changes.


## example

```bash
python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose
```

Output:
23:15:01 DEBUG    __main__ — Arguments parsed: input=fixtures/sample_data.csv, output=output/clean.csv, config=config/config.yaml
23:15:01 INFO     src.utils — Input file validated: fixtures/sample_data.csv
23:15:01 INFO     src.utils — Input file validated: config/config.yaml
23:15:01 INFO     src.data_loaders — Loaded CSV file: fixtures\sample_data.csv (100 rows)
23:15:01 INFO     src.data_loaders — Loaded YAML file: config\config.yaml
23:15:01 WARNING  src.data_validator — Removed 2 rows with invalid numeric values in rating
23:15:01 DEBUG    src.data_validator — Validation: 100 -> 98 rows (2 removed)
23:15:01 INFO     __main__ — Validation complete: 100 -> 98 rows
23:15:01 DEBUG    src.data_processor — remove_duplicates: 98 → 96 rows
23:15:01 DEBUG    src.data_processor — handle_missing: 96 → 94 rows
23:15:01 WARNING  src.data_processor — Column not found: Score
23:15:01 INFO     __main__ — Processing complete: 98 → 94 rows
23:15:01 DEBUG    src.data_output — Saved 94 rows to output\clean.csv
23:15:01 INFO     __main__ — Saved cleaned data to output/clean.csv
cleaned report

