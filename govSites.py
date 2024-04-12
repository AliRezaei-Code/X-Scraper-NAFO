import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def scrape_news(url, tag, class_name):
    # Get the webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all news items
    news_items = soup.findAll(tag, {"class": class_name})

    # Today's date
    today = datetime.now()
    one_month_ago = today - timedelta(days=30)

    for item in news_items:
        date_text = item.find("span", {"class": "date"}).text  
        news_date = datetime.strptime(date_text, "%d %b %Y")  
        if news_date >= one_month_ago:
            title = item.find("a").text
            link = item.find("a")["href"]
            print(f"Title: {title}, Date: {news_date.strftime('%Y-%m-%d')}, Link: {link}")

# Example usage
scrape_news("https://www.mod.gov.lv/en/news", "div", "views-row")
