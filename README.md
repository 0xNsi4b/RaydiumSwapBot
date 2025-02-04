# Solana Raydium AMM Trading Bot

This project is a trading bot for the Solana blockchain using the Raydium AMM protocol. It supports performing buy and sell operations for a specified token with configurable parameters.

## 💸 Support My Work
If my work has been helpful to you or your projects, consider supporting me. Ethereum (ETH) and Solana (SOL) donations are greatly appreciated!

- **Ethereum (ETH):** `0x1Bd298391Bc8E79189ccA44fE5C4221c0d26c4cD`
- **Solana (SOL):** `EeQFCivLhFFjDfUrna1Qnw2yJtxLQLUGR66dPEcZZTNA`

## Prerequisites

- **Python 3.12**  
  Ensure you have Python 3.12 installed. You can download it from [python.org](https://www.python.org/downloads/).

- **Pip**  
  The Python package installer (usually comes bundled with Python).

- **Virtual Environment (Recommended)**  
  It's recommended to use a virtual environment to manage your dependencies. You can use Python's built-in `venv` module or tools like `pipenv`.

- **Solana Wallet and RPC Endpoint**  
  You will need a Solana private key (in base58 string format) and an RPC endpoint URL.

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/solana-trading-bot.git
   cd solana-trading-bot

2.	**Install dependencies**

	```bash
	pip install -r requirements.txt

3.	**Create a .env file**
In the project root directory, create a file named .env with the following content:
	```bash
	PRIVATE_KEY=your_solana_private_key_here
	RPC=https://api.mainnet-beta.solana.com
Replace your_solana_private_key_here with your actual Solana private key. Update the RPC URL if needed.

## Project Structure

- **main.py**

The entry point for the trading bot. It initializes the asynchronous Solana client, sets trading parameters, and calls either the buy or sell function.
- **config.py**

Loads configuration variables (like the RPC endpoint and PRIVATE_KEY) from the environment using the dotenv library.
- **logging_config.py**

Configures logging for the application.
- **raydium_amm.py**

Contains the implementations of the buy and sell functions.
- **.env**

Contains sensitive environment variables like your PRIVATE_KEY and RPC endpoint.


## 🔗 Connect with Me:
[![Telegram](https://img.shields.io/badge/-Telegram-000000?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/nsi4b)
