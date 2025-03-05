# Stock-Trading-News-Alert-Project# Stock Price Alert Project

This project monitors the stock price of Tesla (TSLA) and sends an SMS notification using Twilio if there is a price change of more than 2%. Additionally, it retrieves the latest news articles related to Tesla and includes them in the SMS.

## Features

- Fetches the daily stock price of Tesla (TSLA) using the Alpha Vantage API.
- Compares the closing price of Tesla's stock from the previous day and the day before that.
- If the price changes by more than 2%, it fetches the latest news articles related to Tesla using the NewsAPI.
- Sends an SMS with the stock price change and the top 3 news articles via Twilio.

## Requirements

- Python 3.x
- `requests` library for API calls.
- `twilio` library for sending SMS.
- `python-dotenv` to load environment variables.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/YourUsername/YourRepoName.git
   cd YourRepoName
   ```
