import requests
import random # to select random countries
from typing import List, Dict # we do this for type hinting. This helps us know that the function returns a list of dictionaries.

# Function to fetch data from the REST Countries API
def fetch_random_countries(count: int = 10) -> List[Dict]:
    """
    Fetches data from the REST Countries API and returns a list of random countries.

    Parameters:
    count (int): The number of random countries to fetch. Default is 10.
    
    Returns:
    List[Dict]: A list of dictionaries where each dictionary contains information about a country.
    """
    # The API URL with the fields we need - SEE filter response under API documentation
    url = "https://restcountries.com/v3.1/all?fields=name,capital,flags,subregion,population"
    
    # Send the GET request to the API
    response = requests.get(url)
    
    # Ensure the request was successful
    if response.status_code != 200:
        raise Exception("Error fetching data from the API")
    
    # The response is in JSON format, so we parse it into Python objects (a list of dictionaries) - called PARSING
    countries = response.json()
    
    # Randomly select the specified number of countries
    random_countries = random.sample(countries, count)
    
    return random_countries

# Now that we have random countries with filtered data we'd need to store it in  a SQL and create table with coresponding fields (columns)
# I created table in SQL (advisable?), now in step 3 we need to insert that data from python
# Here is the SQL QUERY: CREATE TABLE countries (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(255),
#     capital VARCHAR(255),
#     flag VARCHAR(255),
#     subregion VARCHAR(255),
#     population BIGINT
# );

import psycopg2

# Function to insert country data into PostgreSQL
def insert_country_data(country: Dict) -> None:
    """
    Inserts a country's data into the PostgreSQL database.
    
    Parameters:
    country (Dict): A dictionary containing information about the country.
    
    Returns:
    None
    """
    # Database connection parameters (adjust as needed)
    conn = psycopg2.connect(
        dbname="menu_db", user="postgres", password="koliko22", host="localhost", port="5432"
    )
    
    # Create a cursor object
    cur = conn.cursor()
    
    # SQL insert query
    insert_query = """
    INSERT INTO countries (name, capital, flag, subregion, population)
    VALUES (%s, %s, %s, %s, %s)
    """
    
    # Execute the insert query with the country's data
    cur.execute(insert_query, (
        country['name']['common'],
        country['capital'][0],
        country['flags']['png'],
        country['subregion'],
        country['population']
    ))
    
    # Commit the transaction
    conn.commit()
    
    # Close the cursor and connection
    cur.close()
    conn.close()


#We need to fetch the data and insert it into the database. Let’s wrap everything in the main function:

if __name__ == "__main__":
    # Fetch random countries
    countries = fetch_random_countries()
    
    # Insert each country into the database
    for country in countries:
        insert_country_data(country)

# Check table in SQL for output ( I executed python code x2 times - therefore there is 20 countries there
# NOTE TO CHECKER - is there a way for me to undo one python execution?