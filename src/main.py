from dotenv import load_dotenv
from polygon import RESTClient
import os

load_dotenv()
polygon_key = os.getenv("POLYGON_KEY")
polygon_client = RESTClient(api_key=polygon_key)

ticker = "AAPL"

aggs = []
for a in polygon_client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2023-01-01", to="2023-06-13", limit=50000):
    aggs.append(a)

print(aggs)
