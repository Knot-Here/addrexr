# addrexr/regex_search.py

import re

def find_evm_contract_addresses(text):
    eth_contract_pattern = r'0x[a-fA-F0-9]{40}'
    return re.findall(eth_contract_pattern, text)

#TODO: add find solana addresses
#TODO: add find btc addresses

#TODO: make master find function for all address types w/ json mapping

def find_all_addresses(text):
    results = {}

