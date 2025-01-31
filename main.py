import requests
from bs4 import BeautifulSoup
import time

class_name = "YMlKec fxKbKc"  # Class for NIFTY 50 index value
url = 'https://www.google.com/finance/quote/NIFTY_50:INDEXNSE?hl=en'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

while True:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(class_=class_name)

    if elements:
        print("NIFTY 50 Index:", elements[0].text)
    else:
        print("Failed to fetch data.")

    time.sleep(60)  # Wait for 1 minute before fetching again
