# 📈 Python Binance Trading Bot

A Python-based cryptocurrency trading bot that connects to the Binance Exchange API to automate cryptocurrency trading. The bot fetches live market data, places buy/sell orders based on predefined trading strategies, and provides a simple command-line interface for execution.

---

## 🚀 Features

- Connects securely to the Binance API
- Retrieves real-time cryptocurrency market prices
- Executes buy and sell orders
- Supports automated trading strategies
- Command-line interface for easy interaction
- Error handling and logging
- Modular project structure for easy maintenance

---

## 🛠️ Technologies Used

- Python 3.x
- Binance API
- Requests
- Python-dotenv
- Logging

---

## 📂 Project Structure

```
python-binance-trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── ...
│
├── cli.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/sanvi06061/python-binance-trading-bot.git
```

### 2. Navigate to the project

```bash
cd python-binance-trading-bot
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

Create a `.env` file in the project directory and add your Binance API credentials.

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

> **Important:** Never upload your API keys to GitHub.

---

## ▶️ Running the Bot

Run the following command:

```bash
python cli.py
```

The bot will connect to Binance and execute the configured trading operations.

---

## 📌 Future Improvements

- Trading strategy customization
- Stop-loss and take-profit support
- Technical indicators (RSI, MACD, EMA)
- Web dashboard
- Trade history visualization
- Telegram notifications
- Backtesting module

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 📄 License

This project is intended for educational purposes.

---

## 👩‍💻 Author

**Sanvi Rai**

GitHub: https://github.com/sanvi06061
