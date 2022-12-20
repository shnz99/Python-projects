from email import message
from http import client
import os
from pydoc import cli
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

alphavantage_api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
news_api_key = os.environ.get("NEWS_API")
twilio_acc_sid = os.environ.get("TWILIO_SID")
twilio_acc_auth = os.environ.get("TWILIO_AUTH")
twilio_sender_num = os.environ.get("TWILIO_NUMBER")
your_num = os.environ.get("YOUR_NUMBER")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alphavantage_params = {
    "function": "GLOBAL_QUOTE",
    "symbol": STOCK,
    "apikey": alphavantage_api_key,
}
alphavantage = requests.get(
    url="https://www.alphavantage.co/query", params=alphavantage_params
)
alphavantage.raise_for_status()

stock_data = alphavantage.json()
last_day_close = stock_data["Global Quote"]["05. price"]
before_last_day_close = stock_data["Global Quote"]["08. previous close"]
percent_change = stock_data["Global Quote"]["10. change percent"]
latest_trading_day = stock_data["Global Quote"]["07. latest trading day"]

if (
    float(percent_change[:-1]) > 2 or float(percent_change[:-1]) < -2
):  # float because it is conversion from string to % and slice with -1 because symbol % at the end in json
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_api_params = {
        "apiKey": news_api_key,
        "q": COMPANY_NAME,
        "from": latest_trading_day,
    }
    news_api = requests.get(
        url="https://newsapi.org/v2/everything", params=news_api_params
    )
    news_api.raise_for_status()

    news_data = news_api.json()
    articles = news_data["articles"][:3]

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    client = Client(twilio_acc_sid, twilio_acc_auth)
    for article in articles:
        formatted_article = {
            f"\n{COMPANY_NAME}: {percent_change}\nHeadline: {article['title']}\n\nBrief: {article['description']}"
            for article in articles
        }

        message = client.messages.create(
            body=formatted_article,
            from_=twilio_sender_num,
            to=your_num,
        )
        print(message.status)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
