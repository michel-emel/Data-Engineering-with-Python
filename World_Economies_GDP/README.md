
# ETL Project: Extracting and Transforming GDP Data
## Overview
This project is an ETL pipeline designed to extract GDP data from a Wikipedia page, transform it into a usable format, and load it into both a CSV file and an SQLite database. The project logs each stage of the process, ensuring traceability and easy debugging.
## Features
- **Data Extraction**: Fetches GDP data of countries from a Wikipedia page using web scraping.
- **Data Transformation**: Converts the GDP values from USD Millions to USD Billions, ensuring they are in a numerical format for further analysis.
- **Data Loading**: Saves the transformed data to both a CSV file and an SQLite database.
- **Logging**: Tracks the progress of the ETL process in a log file.
## Project Structure
- **`extract()`**: Scrapes data from the given URL and parses it into a DataFrame.
- **`transform()`**: Transforms the GDP data from string format (USD Millions) to numerical format (USD Billions).
- **`load_to_csv()`**: Saves the transformed data into a CSV file.
- **`load_to_db()`**: Loads the data into an SQLite database.
- **`run_query()`**: Runs a SQL query to retrieve data from the database.
- **`log_progress()`**: Logs messages with timestamps to track the progress of the ETL process.
## Requirements
- `beautifulsoup4`: To parse HTML content.
- `requests`: To make HTTP requests.
- `pandas`: For handling data in DataFrame format.
- `numpy`: For numerical operations.
- `sqlite3`: To interact with SQLite databases.
You can install the required libraries using pip:
```bash
pip install beautifulsoup4 requests pandas numpy
```
## Usage
1. **Set Up the Environment**: Ensure that the required libraries are installed.
   
2. **Run the Script**: Execute the Python script to run the ETL pipeline. It will:
   - Extract GDP data from the specified Wikipedia page.
   - Transform the GDP data into a numeric format.
   - Save the data to a CSV file and load it into an SQLite database.
   - Log the progress in the `etl_project_log.txt` file.
3. **Review the Output**:
   - The CSV file will be saved at `./Countries_by_GDP.csv`.
   - The SQLite database will be saved as `World_Economies.db`.
   - Query results are displayed on the terminal.
## Example Query
The script includes an example SQL query that retrieves countries with a GDP of 100 billion USD or more:
```sql
SELECT * FROM Countries_by_GDP WHERE GDP_USD_billions >= 100;
```
## Logs
The script logs all stages of the ETL process in `etl_project_log.txt`, allowing for easy monitoring and debugging.

## Contact
For any questions or issues, please feel free to contact [(lechiffremel@gmail.com)](lechiffremel@gmail.com).
```
