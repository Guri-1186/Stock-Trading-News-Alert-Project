import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

STOCK_KEY = os.getenv("STOCK_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
MY_PHONE = os.getenv("MY_PHONE")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterdays_data = data_list[0]
yesterdays_closing_price = float(yesterdays_data["4. close"])

day_before_yesterdays_data = data_list[1]
day_before_yesterdays_closing_price = float(day_before_yesterdays_data["4. close"])

difference = yesterdays_closing_price - day_before_yesterdays_closing_price
up_down = "🔺" if difference > 0 else "🔻"

percentage_change = round((difference / yesterdays_closing_price) * 100)

if abs(percentage_change) > 2:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apikey": NEWS_API_KEY
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{percentage_change}%\n"
        f"Headline: {article['title']}.\n"
        f"Brief: {article['description'] if article['description'] else 'No description available.'}"
        for article in three_articles
    ]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_PHONE,
            to=MY_PHONE
        )
        print(f"Message sent: {message.sid}")