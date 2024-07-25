from typing import List
import math
import json
import asyncio

from web3 import Web3
from web3.eth import AsyncEth
from fake_useragent import UserAgent

from .utils import load_tokens_data
from main_data import DATA
from main_data import MULTICALL_ETH_CONTRACTS
from main_data import contract_abi
from main_data import base_dir

with open(base_dir / 'main_data' / 'abi' / 'erc20.json', 'r') as f:
    erc20 = json.load(f)


class EvmBalanceChecker:
    def __init__(self, wallets, chains: List[str], proxy: None | str = None, check_proxy: bool = False):
        self.wallets = wallets
        self.chains = chains
        self.proxy = proxy
        self.headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'user-agent': UserAgent().chrome
        }

    def get_web3(self, chain):
        w3 = Web3(
            provider=Web3.AsyncHTTPProvider(
                endpoint_uri=DATA[chain]['rpc'],
            ),
            modules={'eth': (AsyncEth,)},
            request_kwargs = {{'headers': self.headers}},
            middlewares=[],
        )
        return w3

    def get_tokens_data(self):
        tokens_list = {}
        for chain in self.chains:
            tokens_list[chain] = {}
            token_data = load_tokens_data(chain)
            for coin in token_data:
                if coin != '':
                    tokens_list[chain][coin['symbol']] = {
                        'address': coin['address'],
                        'decimals': coin['decimals']
                    }

        return tokens_list

    async def balance_of_all_tokens(self, w3: Web3, chain: str, wallets_list: List[str], tokens_list: List[str]):
        multicall_contract = w3.eth.contract(
            address=Web3.to_checksum_address(MULTICALL_ETH_CONTRACTS[chain]), abi=contract_abi)
        multicall_result = await multicall_contract.functions.balances(
            wallets_list, tokens_list
        ).call()
        return multicall_result

    async def get_balances(self, chain, wallets, tokens_list):
        symbols_list = [token for token in tokens_list.keys()]
        wallets_ = [Web3.to_checksum_address(wallet) for wallet in wallets]
        contracts = [Web3.to_checksum_address(token['address']) for token in tokens_list.values()]

        batch_limit = 1000
        len_batch = math.floor(batch_limit / len(tokens_list))
        len_batch = len_batch if len_batch != 0 else 1
        wallets_batches = [wallets_[i:i + len_batch] for i in range(0, len(wallets_), len_batch)]

        balances_dict = {}
        zero = 0
        for wallets_list in wallets_batches:
            max_attempts = 10
            for attempt in range(max_attempts):
                try:
                    web3 = self.get_web3(chain)
                    multicall_result = await self.balance_of_all_tokens(web3, chain, wallets_list, contracts)
                    zero += len(wallets_list)
                    multicall_result = [multicall_result[i:i + len(tokens_list)] for i in
                                        range(0, len(multicall_result), len(tokens_list))]

                    for number, wallet in enumerate(wallets_list):
                        balances = multicall_result[number]
                        balances_dict[wallet] = {}

                        for i, balance in enumerate(balances):
                            symbol = symbols_list[i]
                            balance = int(balance / 10 ** tokens_list[symbol]['decimals'])

                            if balance > 0:
                                balances_dict[wallet][symbol] = balance
                    break

                except Exception as e:
                    await asyncio.sleep(1)

        return balances_dict

    async def evm_balances(self):
        tokens_data = self.get_tokens_data()
        tasks = []
        results = {}
        for chain in self.chains:
            if chain in tokens_data:
                tokens_list = tokens_data[chain]
                task = asyncio.create_task(self.get_balances(chain, self.wallets, tokens_list))
                tasks.append(task)

            chain_result = await asyncio.gather(*tasks)
            results[chain] = chain_result[-1]

        return results
