import requests
from bs4 import BeautifulSoup

def get_amazon_price(product_name):
    url = f"https://www.amazon.com/s?k={product_name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        price = soup.find("span", class_="a-price-whole").text
        return f"Amazon: ${price}"
    except AttributeError:
        return "Amazon: Price not found"

def get_walmart_price(product_name):
    url = f"https://www.walmart.com/search?q={product_name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        price = soup.find("span", class_="price-characteristic").text
        return f"Walmart: ${price}"
    except AttributeError:
        return "Walmart: Price not found"

def get_ebay_price(product_name):
    url = f"https://www.ebay.com/sch/i.html?_nkw={product_name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        price = soup.find("span", class_="s-item__price").text
        return f"eBay: {price}"
    except AttributeError:
        return "eBay: Price not found"

def get_alibaba_price(product_name):
    url = f"https://www.alibaba.com/trade/search?SearchText={product_name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    try:
        price = soup.find("div", class_="elements-offer-price-normal__price").text
        return f"Alibaba: {price}"
    except AttributeError:
        return "Alibaba: Price not found"

def compare_prices(product_name):
    print("Fetching prices...")
    amazon_price = get_amazon_price(product_name)
    walmart_price = get_walmart_price(product_name)
    ebay_price = get_ebay_price(product_name)
    alibaba_price = get_alibaba_price(product_name)

    print(amazon_price)
    print(walmart_price)
    print(ebay_price)
    print(alibaba_price)

if _name_ == "_main_":
    product = input("Enter product name: ")
    compare_prices(product)
