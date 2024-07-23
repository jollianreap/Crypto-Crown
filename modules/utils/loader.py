import json
import os

from setting import base_dir


def load_tokens_data(chain: str):

    with open(base_dir / 'main_data' / 'tokenlists' / f'{chain.capitalize()}.json', 'r') as f:
        token_list = json.load(f)

    return token_list

