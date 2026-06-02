from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET")
)

client.FUTURES_URL = "https://demo-fapi.binance.com/fapi"

# Sync with Binance server time
server_time = client.get_server_time()
client.timestamp_offset = server_time["serverTime"] - int(__import__("time").time() * 1000)