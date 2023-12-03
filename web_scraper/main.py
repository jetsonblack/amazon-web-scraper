from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
script_directory = os.path.dirname(os.path.abspath(__file__))
CHROME_DRIVER_PATH = os.path.join(script_directory, 'chromedriver.exe')

def get_review_data(url, driver): #gets review data via html scrape and search.
    print(f"Scraping reviews from {url}")
    driver.get(url)
    time.sleep(2)

    raw_html = driver.page_source
    soup = BeautifulSoup(raw_html, 'html.parser')

    review_data = []
    for review_span in soup.find_all("span", class_="a-size-base review-text review-text-content"):
        review_text = review_span.get_text(strip=True)
        if review_text:
            review_data.append(review_text)
            print("Review Found!")

    print(f"Found {len(review_data)} reviews on {url}")
    return review_data

def get_all_reviews(url, driver):
    reviews = []
    first_page_reviews = get_review_data(url, driver)
    reviews.extend(first_page_reviews)
    return reviews

url = str(input("URL?:")) #prompt user for URL of amazon review page an example: https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/product-reviews/B07PXGQC1Q/ref=cm_cr_arp_d_paging_btm_prev_9?ie=UTF8&pageNumber=9&reviewerType=avp_only_reviews&sortBy=recent#reviews-filter-bar

chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without opening a browser window)
chrome_service = ChromeService(executable_path=CHROME_DRIVER_PATH)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

reviews = get_all_reviews(url, driver)

driver.quit()

print(f"Total reviews: {len(reviews)}")

dataset = {'text-review': reviews}
dataframe = pd.DataFrame(dataset)
dataframe.to_csv('amazon_review_scrape.csv', mode='a', header=False, index=False) #writes and appends to the amazon_review_scrape.csv file
