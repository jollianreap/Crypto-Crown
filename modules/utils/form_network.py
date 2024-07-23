import re
import json


import requests
# from eth_async.models import Network

"""
name: str,
rpc: str,
chain_id: int | None = None,
coin_symbol: str | None = None,
"""


def check_link(link):
    pattern = re.compile(r"(?=.*API.*KEY)(?=.*KEY.*API)", re.IGNORECASE)
    return bool(pattern.search(link))


def check_rpc(url, method='eth_blockNumber', params=[]):
    headers = {
        'Content-Type': 'application/json',
    }

    payload = {
        'jsonrpc': '2.0',
        'method': method,
        'params': params,
        'id': 1,
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            result = response.json()
            if 'result' in result:
                return True # rpc works
            else:
                return False # rpc doesn't work
        else:
            return False # rpc doesn't work

    except requests.exceptions.RequestException as e:
        return False, str(e)