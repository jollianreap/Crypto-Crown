import json
import os

from setting import ROOT_PATH

def load_tokens_data(chain: str):

    with open(ROOT_PATH + f'/main_data/tokenlists/{chain.capitalize()}.json', 'r') as f:
        token_list = json.load(f)

    return token_list


if __name__ == '__main__':
    print(load_tokens_data('base'))