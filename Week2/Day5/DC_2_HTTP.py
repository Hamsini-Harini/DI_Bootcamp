import requests  # first pip install requests and then import handle HTTP requests
import time  # to measure the time taken for a request

# Defining a function to measure the time taken for a webpage to load
def get_page_load_time(url: str) -> float:
    """
    This function takes a URL as input and returns the time (in seconds) 
    it takes to load the webpage.
    """
    
    # Start the clock before making the request
    start_time = time.time()  # Record the current time
    
    # Send a GET request to the webpage
    response = requests.get(url)  # This sends the request and waits for the response
    
    # Stop the clock after receiving the response
    end_time = time.time()  # Record the current time after the response is received
    
    # Calculate the difference between end_time and start_time
    load_time = end_time - start_time  # This gives us the total time in seconds
    
    return load_time 


if __name__ == "__main__":
    # Test the function with multiple websites
    websites = ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com", "https://kriptoholicar.rs/", "https://originalanpoklon.com/", "https://www.ronkinlaw.co.il/", "https://kualastyle.com/"]
    
    for site in websites:
        time_taken = get_page_load_time(site)  # Call the function for each site
        print(f"Time taken to load {site}: {time_taken:.4f} seconds")  # Print the result
