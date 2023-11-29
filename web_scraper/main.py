import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_review_data(url):
    # Extract reviews from a single page
    print(f"Scraping reviews from {url}")
    raw_html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(raw_html, 'html.parser')

    review_data = []
    for review_div in soup.find_all("div", class_="a-row a-spacing-small review-data"):
        review_span = review_div.find("span", {"data-hook": "review-body"})
        if review_span:
            review_text = review_span.get_text(strip=True)
            review_data.append(review_text)
            print("Fuck") 
    print(f"Found {len(review_data)} reviews on {url}")
    return review_data

def get_all_reviews(url):
    reviews = []

    # Get the first page of reviews
    first_page_reviews = get_review_data(url)
    reviews.extend(first_page_reviews)

    # Extract reviews from subsequent pages
    next_page_url = url + "&pageNumber=2"
    while next_page_url:
        more_reviews = get_review_data(next_page_url)

        if more_reviews:
            reviews.extend(more_reviews)
            next_page_url = url + "&pageNumber=" + str(int(next_page_url.split("pageNumber=")[-1]) + 1)
        else:
            next_page_url = None

    return reviews

url = "https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/product-reviews/B07PXGQC1Q/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

reviews = get_all_reviews(url)

# Save reviews to a CSV file
dataset = {'text-review': reviews}
dataframe = pd.DataFrame(dataset)

# Add a print statement to check the length of reviews before saving to CSV
print(f"Total reviews: {len(reviews)}")

dataframe.to_csv('amazon_review_scrape.csv', index=False)
