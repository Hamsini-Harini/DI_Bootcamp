# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import time
import csv
import ssl

# Bypass SSL verification issues
ssl._create_default_https_context = ssl._create_unverified_context


# Automatically install chromedriver
chromedriver_autoinstaller.install()

# Initialize Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (without opening browser)
service = Service()

driver = webdriver.Chrome(service=service, options=chrome_options)

# Load the website
url = "https://www.inmotionhosting.com/shared-hosting"
driver.get(url)

# Allow time for the page to fully load
time.sleep(10)  # Wait for X seconds to ensure all content loads

#-------------------------------------------------------------------
# STARTING THE EXTRACTION

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all hosting plan cards
hosting_plans = soup.find_all('div', class_='imh-rostrum-card')

# Create an empty list to store the data
hosting_data = []

# Loop through each hosting plan and extract data
for plan in hosting_plans:
    # Extract the title
    title = plan.find('h3', class_='imh-rostrum-card-title').get_text(strip=True)
    
    # Extract the price
    price = plan.find('div', class_='imh-rostrum-starting-at-price-discounted').find('span', class_='rostrum-price').get_text(strip=True)
    
    # Extract the features
    features = [li.get_text(strip=True) for li in plan.find('ul', class_='imh-rostrum-details-list').find_all('li')]
    
    # Store the data in the list
    hosting_data.append({
        'Plan Title': title,
        'Price': price,
        'Features': features
    })

# Print extracted data for verification
for plan in hosting_data:
    print(f"Title: {plan['Plan Title']}")
    print(f"Price: {plan['Price']}")
    print("Features:")
    for feature in plan['Features']:
        print(f"- {feature}")
    print("\n")

#-----------------------------------------------------------------------------
# SINCE I HAD ISSUES WITH PANDAS, I AM USING OLD METHOD OF DIRECTLY WRITING TO CSV FILE BEFORE INSPECTING WITH PANDAS

# Save the extracted data into a CSV file
with open('hosting_plans.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Plan Title', 'Price', 'Features'])
    writer.writeheader()

    # Write the data for each hosting plan
    for plan in hosting_data:
        writer.writerow({
            'Plan Title': plan['Plan Title'],
            'Price': plan['Price'],
            'Features': ', '.join(plan['Features'])  # Convert features list to a comma-separated string
        })

print("Data successfully saved to 'hosting_plans.csv'")



# Close the Selenium WebDriver
driver.quit()
