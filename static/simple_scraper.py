import requests
from bs4 import BeautifulSoup
import csv
from pprint import pprint
import threading


url_base = "https://webscraper.io/test-sites/e-commerce/allinone"
resources = [
    "computers",
    "computers/laptops",
    "computers/tablets",
    "phones",
    "phones/touch"
]

def make_article(name, price, review_number, url):
    return (name, price, review_number, url)

with open("output/articles_simple.csv", "w") as f:
    csv_writer = csv.writer(f)
    
    for resource in resources:
        url = f"{url_base}/{resource}"
        response = requests.get(url)

        if response.status_code == 200:
            print(f"Scraping : {url}")
            parser = BeautifulSoup(response.content, "html.parser")

            article_names = parser.find_all("a", {"class" : "title"})
            article_prices = parser.find_all("h4", {"class" : "price"})
            article_review_numbers = [item.find("p", {"class" : "pull-right"}) for item in  parser.find_all("div", {"class" : "ratings"})]
            article_urls = [ name.get("href") for name in article_names]

            for name, price, review_number, url in zip(article_names, article_prices, article_review_numbers, article_urls):
                csv_writer.writerow( make_article( name.string, price.string, review_number.string.split()[0], url ) )