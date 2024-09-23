from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import pprint
import ssl
import urllib.request

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

# Navigate to the Rotten Tomatoes Certified Fresh Movies page
url = "https://www.rottentomatoes.com/browse/movies_at_home/critics:certified_fresh"
driver.get(url)

# Wait for the movie elements to load on the page
wait = WebDriverWait(driver, 10)
movies_loaded = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-qa="discovery-media-list-item-title"]')))

# Get the page source and parse it using BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Find all movie elements (titles, scores, release dates)
movies = soup.find_all(attrs={"data-qa": "discovery-media-list-item-title"})

# List to store movie details
movie_list = []

# Extract title, score, and release date for each movie
for movie in movies:
    title = movie.get_text()  # Movie title
    # Extract parent element to find the associated data for this movie
    parent = movie.find_parent()

    # Critic Score (Using the class to find the text)
    score = parent.select_one('rt-text[slot="criticsScore"]')  # Modify if needed to fit the correct element
    if score:
        score = score.get_text()
    else:
        score = "N/A"

    # Release Date
    release_date = parent.find(class_="smaller").get_text()

    # Append extracted details to the movie list
    movie_list.append({
        "title": title,
        "critic_score": score,
        "release_date": release_date
    })

# Print extracted movie data
pprint.pprint(movie_list)

# Close the browser instance
driver.quit()
