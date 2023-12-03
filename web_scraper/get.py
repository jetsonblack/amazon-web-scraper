import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

def get_review_data(url):
    print(f"Scraping reviews from {url}")
    raw_html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(raw_html, 'html.parser')

    review_data = []
    for review_div in soup.find_all("div", class_="a-section review aok-relative"):
        review_text = review_div.find("span", class_="a-size-base review-text review-text-content")
        if review_text:
            review_data.append(review_text.get_text(strip=True))
            print("Review Found!")

    print(f"Found {len(review_data)} reviews on {url}")
    return review_data

def get_all_reviews(url):
    reviews = []
    first_page_reviews = get_review_data(url)
    reviews.extend(first_page_reviews)
    return reviews

url = "https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/product-reviews/B07PXGQC1Q/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber=3"

reviews = get_all_reviews(url)

print(f"Total reviews: {len(reviews)}")

dataset = {'text-review': reviews}
dataframe = pd.DataFrame(dataset)

dataframe.to_csv('amazon_review_scrape.csv', mode='a', header=False, index=False)
