# ticker_resolver.py

import json

# Placeholder for your actual data source, this could be replaced by a database call or an API
# For now, we'll use a mock JSON-like dictionary
ticker_data = {
    "ETH": {
        "erc20_addresses": {
            "ethereum": "0x1234567890abcdef1234567890abcdef12345678",
            "binance_smart_chain": "0xabcdef1234567890abcdef1234567890abcdef12"
        },
        "oracle_addresses": {
            "chainlink": "0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef",
            "uniswap": "0x1234567890abcdef1234567890abcdef12345678"
        }
    },
    "USDC": {
        "erc20_addresses": {
            "ethereum": "0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef",
            "polygon": "0x1234567890abcdef1234567890abcdef12345678"
        },
        "oracle_addresses": {
            "chainlink": "0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef"
        }
    }
}


def resolve_ticker(ticker, chain=None, include_oracles=True):
    """
    Resolves the ticker to ERC20 and/or oracle addresses across chains.

    :param ticker: str, the ticker symbol (e.g., 'ETH', 'USDC').
    :param chain: str, optional, filter by a specific chain (e.g., 'ethereum').
    :param include_oracles: bool, if True, include oracle addresses.
    :return: dict, a dictionary containing resolved addresses.
    """

    # Convert ticker to uppercase to ensure consistency
    ticker = ticker.upper()

    if ticker not in ticker_data:
        return {"error": f"No data found for ticker: {ticker}"}

    result = {}

    # Fetch contract addresses
    erc20_addresses = ticker_data[ticker].get("erc20_addresses", {})
    oracle_addresses = ticker_data[ticker].get("oracle_addresses", {})

    # Filter by chain if provided
    if chain:
        erc20_address = erc20_addresses.get(chain)
        if not erc20_address:
            return {"error": f"No ERC20 address found for ticker: {ticker} on chain: {chain}"}
        result["erc20_address"] = erc20_address

        if include_oracles:
            oracle_address = oracle_addresses.get(chain)
            if oracle_address:
                result["oracle_address"] = oracle_address

    # Return all chain addresses if no chain specified
    else:
        result["erc20_addresses"] = erc20_addresses
        if include_oracles:
            result["oracle_addresses"] = oracle_addresses

    return result


if __name__ == "__main__":
    # Hardcoded example: Get all ERC20 and oracle addresses for ETH across all chains
    ticker = "ETH"
    chain = None  # Set to 'ethereum' or another chain if needed
    include_oracles = True

    resolved_data = resolve_ticker(ticker, chain, include_oracles)
    print(json.dumps(resolved_data, indent=4))

