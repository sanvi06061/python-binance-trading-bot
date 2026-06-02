from bot.client import client

orders = client.futures_get_all_orders(symbol="BTCUSDT")

print("Total Orders:", len(orders))

for order in orders[-10:]:
    print(
        order["orderId"],
        order["status"],
        order["type"],
        order["side"]
    )