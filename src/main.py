from dotenv import load_dotenv
from polygon import RESTClient
import os
from weathsimpleParse import extract_trade_actions 
from user_portfolio import UserPortfolio

load_dotenv()
polygon_key = os.getenv("POLYGON_KEY")
polygon_client = RESTClient(api_key=polygon_key)

# Initialize user portfolio
portfolio = UserPortfolio()

# Get trade actions from email
trade_actions = extract_trade_actions(os.getenv('TRADE_EMAIL_PATH'))

# Process each trade action
for trade in sorted(trade_actions, key=lambda x: x.time):
    print(trade)
    portfolio.add_trade(trade)

# Print the portfolio
print(portfolio)