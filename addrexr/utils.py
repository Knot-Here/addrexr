# addrexr/utils.py
import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def get_blockchains():
    """Loads the blockchains.json file from the package."""
    with open(os.path.join(os.path.dirname(__file__), 'config', 'blockchains.json')) as file:
        data = json.load(file)
    return data

def get_slugs(ticker):
    return 0

if __name__ == "__main__":
    print(get_blockchains())

