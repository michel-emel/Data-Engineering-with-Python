# Import necessary libraries
from bs4 import BeautifulSoup  # For parsing HTML content
import requests  # For making HTTP requests
import pandas as pd  # For handling data in DataFrame format
import sqlite3  # For SQLite database operations
from datetime import datetime  # For handling date and time


URL = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'

def log_progress(message):
    ''' Log the progress of the ETL process with a timestamp. '''
    timestamp_format = '%Y-%m-%d %H:%M:%S'  # Corrected timestamp format
    now = datetime.now()  # Get the current timestamp
    timestamp = now.strftime(timestamp_format)  # Format the timestamp
    
    # Append the log message to the log file
    with open("./etl_project_log.txt", "a") as f:
         f.write(timestamp + ' : ' + message + '\n')

def extract(url, table_attribs):
    ''' Extract data from the website, parse the required information,
    and save it to a DataFrame. Returns the DataFrame for further processing. '''
    page = requests.get(url).text  # Fetch the page content as text
    data = BeautifulSoup(page, 'html.parser')  # Parse the HTML content using BeautifulSoup
    tables = data.find_all('tbody')  # Find all 'tbody' tags in the HTML content

    data_list = []
    rows = tables[0].find_all('tr')  # Extract rows from the first table (index 0)
    
    # Iterate through each row to extract the relevant data
    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            if col[1].find('a') is not None and '—' not in col[2]:
                data_dict = {
                    "Bank name": col[1].find('a').text.strip(),
                    "Market cap (USD)": float(col[2].text.strip().replace(',', '').replace('$', ''))
                }
                data_list.append(data_dict)

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data_list, columns=table_attribs)
    return df

def transform(df, exchange_rate):
    '''Transform the DataFrame by adding columns for different currency conversions.'''
    for i in range(len(exchange_rate)):
        cur_rate = exchange_rate.iloc[i].tolist()
        df[f'Market cap ({cur_rate[0]})'] = round(df['Market cap (USD)'] * cur_rate[1], 2)   
    return df

def load_to_csv(df, csv_path):
    ''' Save the DataFrame to a CSV file at the specified path. '''
    df.to_csv(csv_path, index=False)

def load_to_db(df, sql_connection, table_name):
    ''' Save the DataFrame as a table in the SQLite database.
    Replace the table if it already exists. '''
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)
    log_progress(f'Data successfully loaded into the table {table_name} in the SQLite database.')

def run_query(query_statement, sql_connection):
    ''' Execute a SQL query on the database and print the result. '''
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)
    return query_output

# Load exchange rates
exchange_rate = pd.read_csv('exchange_rate.csv')

# Extract the bank data from the Wikipedia page
df = extract(URL, ['Bank name', 'Market cap (USD)'])

# Transform the data by converting market cap to different currencies
df_transformed = transform(df, exchange_rate)

# Load the transformed data to a CSV file
load_to_csv(df_transformed, './Largest_banks_data.csv')

# Load the transformed data to an SQLite database
log_progress('SQL Connection initiated.')
connection = sqlite3.connect('Banks.db')
load_to_db(df_transformed, connection, 'Largest_banks')

# Run and print the results of the queries
query_1 = "SELECT * FROM Largest_banks"
result_1 = run_query(query_1, connection)

query_2 = "SELECT AVG([Market cap (GBP)]) FROM Largest_banks"
result_2 = run_query(query_2, connection)

query_3 = "SELECT [Bank name] FROM Largest_banks LIMIT 5"
result_3 = run_query(query_3, connection)

# Close the database connection
connection.close()
