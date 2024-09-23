from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import pprint
import ssl
from collections import defaultdict
from datetime import datetime, timedelta
import re

# Bypass SSL verification issues
ssl._create_default_https_context = ssl._create_unverified_context

# Install ChromeDriver automatically
chromedriver_autoinstaller.install()

# Set up Chrome options for headless scraping
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

# Navigate to the BBC Innovation news page
url = "https://www.bbc.com/innovation"
driver.get(url)

# Wait for the article elements to load on the page
wait = WebDriverWait(driver, 10)
articles_loaded = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="card-headline"]')))

# Get the page source and parse it using BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Dictionary to store categorized articles by month
articles_by_month = defaultdict(list)

# Current date
today = datetime.now()

# Regex to detect relative dates like "3 days ago"
relative_date_pattern = re.compile(r"(\d+)\s+days?\s+ago")

# Find all article blocks (parent elements)
articles = soup.find_all('div', attrs={"data-testid": "liverpool-article"})

# Extract title and publication date for each article
for article in articles:
    # Get the title using the correct CSS selector for headline
    title_tag = article.find('h2', attrs={"data-testid": "card-headline"})
    title = title_tag.get_text() if title_tag else "No title"

    # Get the publication date using the correct CSS selector for date
    date_tag = article.find('span', attrs={"data-testid": "card-metadata-lastupdated"})
    date_text = date_tag.get_text() if date_tag else "No date"

    # Handle relative dates like "3 days ago"
    match = relative_date_pattern.match(date_text)
    if match:
        # Extract the number of days from the relative date
        days_ago = int(match.group(1))
        # Calculate the actual date by subtracting the number of days from today
        actual_date = today - timedelta(days=days_ago)
        month = actual_date.strftime('%B')  # Extract the month name
        date_text = actual_date.strftime('%d %b %Y')  # Format the absolute date
    else:
        # If the date is not relative, assume it's a specific date (if available)
        try:
            actual_date = datetime.strptime(date_text, '%d %b %Y')
            month = actual_date.strftime('%B')  # Extract the month name
        except ValueError:
            month = "Unknown"  # Handle cases where the date is in an unrecognized format

    # Categorize the article by month
    articles_by_month[month].append({
        'title': title,
        'publication_date': date_text
    })

# Print categorized articles by month
pprint.pprint(dict(articles_by_month))

# Close the browser instance
driver.quit()
