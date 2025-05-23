import requests
import datetime
news_api_key = '21280525e394452db99f4fc2eb962c95'
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_key = ' C7Z3FH6HGX3GCUE8'
stock_parameter = {'function': 'TIME_SERIES_DAILY', 'symbol': STOCK, 'apikey': stock_api_key}
news_parameter = {'q': COMPANY_NAME, 'apikey': news_api_key}
stock_response = requests.get('https://www.alphavantage.co/query', params=stock_parameter)
stock_data = stock_response.json()
news_response = requests.get('https://newsapi.org/v2/everything', params=news_parameter)
print(stock_data)
yesterday = (datetime.datetime.now().date() - datetime.timedelta(1))
print(yesterday)
day_before_yesterday = (datetime.datetime.now().date() - datetime.timedelta(2))
stock_data_yesterday = float(stock_data['Time Series (Daily)'][f'{yesterday}']['4. close'])
stock_data_daybefore_yesterday = float(stock_data['Time Series (Daily)'][f'{day_before_yesterday}']['4. close'])
percentage = abs((stock_data_yesterday-stock_data_daybefore_yesterday)/stock_data_yesterday*100)
percentage = round(percentage, 2)
if percentage > 10:
    print('get_news')

print(stock_data_yesterday)
print(stock_data_daybefore_yesterday)
print(percentage)
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
