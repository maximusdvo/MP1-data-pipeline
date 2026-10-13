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


