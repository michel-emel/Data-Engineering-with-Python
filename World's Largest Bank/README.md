---

# World's Largest Banks Data ETL Project

This project extracts data from Wikipedia's list of the largest banks, transforms the data by converting market capitalizations into multiple currencies, and loads the data into both a CSV file and an SQLite database. The project also includes SQL queries to retrieve and analyze the data.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Data Extraction](#data-extraction)
- [Data Transformation](#data-transformation)
- [Data Loading](#data-loading)
- [Usage](#usage)
- [SQL Queries](#sql-queries)
- [Logs](#logs)
- [License](#license)

## Project Overview

This ETL (Extract, Transform, Load) project fetches data from an archived Wikipedia page listing the largest banks by market capitalization. The extracted data is then transformed by converting the market cap from USD to other currencies using exchange rates provided in a CSV file. The transformed data is stored in both a CSV file and an SQLite database for further analysis.

## Technologies Used

- **Python**: The primary programming language used for scripting.
- **BeautifulSoup**: For parsing and extracting data from HTML.
- **Requests**: For making HTTP requests to fetch web pages.
- **Pandas**: For data manipulation and transformation.
- **SQLite3**: For database operations and data storage.
- **Datetime**: For handling and logging timestamps.

## Data Extraction

The `extract()` function fetches the HTML content from the archived Wikipedia page and parses it using BeautifulSoup. The function specifically targets the table containing the list of banks and their market capitalizations in USD.

```python
df = extract(URL, ['Bank name', 'Market cap (USD)'])
```

## Data Transformation

The `transform()` function converts the market capitalization from USD to other currencies, including EUR, GBP, and INR, based on exchange rates provided in the `exchange_rate.csv` file.

```python
df_transformed = transform(df, exchange_rate)
```

## Data Loading

### Loading to CSV

The transformed data is saved to a CSV file using the `load_to_csv()` function:

```python
load_to_csv(df_transformed, './Largest_banks_data.csv')
```

### Loading to SQLite Database

The transformed data is also loaded into an SQLite database using the `load_to_db()` function. The database table is replaced if it already exists:

```python
load_to_db(df_transformed, connection, 'Largest_banks')
```

## Usage

To run the ETL process:

1. Ensure that `exchange_rate.csv` is available in the same directory as the script.
2. Run the script using Python:
    ```bash
    python your_script_name.py
    ```

The script will fetch the data, transform it, and save it in both CSV and SQLite database formats.

## SQL Queries

Several SQL queries are executed on the SQLite database to analyze the data:

- Retrieve all data:
  ```sql
  SELECT * FROM Largest_banks;
  ```

- Calculate the average market capitalization in GBP:
  ```sql
  SELECT AVG([Market cap (GBP)]) FROM Largest_banks;
  ```

- Retrieve the names of the first five banks:
  ```sql
  SELECT [Bank name] FROM Largest_banks LIMIT 5;
  ```

## Logs

The ETL process logs its progress in a file named `etl_project_log.txt`. The logs include timestamps and messages indicating the steps completed.

---


