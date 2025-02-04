import logging
import asyncio

from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair
from config import RPC, PRIVATE_KEY
from logging_config import setup_logging
from raydium_amm import buy, sell

# Initialize logging configuration
setup_logging()
logger = logging.getLogger(__name__)


async def main():
    # Define common parameters
    token_address = "5D27EZ1prg14zDFfDXZPfebej2Q4mX12VBqLeXdppump"  # Token address to trade
    slippage = 10  # Allowed slippage percentage for the trade

    # Parameters for buying tokens
    sol_in = 0.0001  # Amount of SOL to spend for the purchase

    # Parameters for selling tokens (currently not used)
    percentage = 100  # Percentage of tokens to sell

    # Create an asynchronous Solana client using the provided RPC endpoint
    client = AsyncClient(RPC)

    # Create a keypair from the provided PRIVATE_KEY
    key_pair = Keypair.from_base58_string(PRIVATE_KEY)

    # Execute the buy function. To execute the sell function, comment out the buy line and uncomment the sell line.
    await buy(client, key_pair, token_address, sol_in, slippage)
    # To perform a sell operation, uncomment the line below:
    # await sell(client, key_pair, token_address, percentage, slippage)


if __name__ == "__main__":
    asyncio.run(main())