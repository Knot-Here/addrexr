# tests/test_regex_search.py

from addrexr.regex_search import find_contract_addresses

def test_find_contract_addresses():
    sample_text = "Here is a contract address: 0x1234567890abcdef1234567890abcdef12345678"
    result = find_contract_addresses(sample_text)

