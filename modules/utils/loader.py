import json


def load_erc20():
    with open('/home/jollyreap/crypto_crown/main_data/erc20.json', 'r') as f:
        return json.load(f)

