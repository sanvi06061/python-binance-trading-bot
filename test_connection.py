from bot.client import client

try:
    info = client.futures_account_balance()
    print("Connected Successfully!")
    print(info)
except Exception as e:
    print("Error:", e)