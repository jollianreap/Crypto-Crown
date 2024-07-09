import math
import asyncio
import aiohttp

from web3 import Web3, AsyncHTTPProvider
from web3.eth import AsyncEth

from setting import Value_EVM_Balance_Checker
from main_data.data import DATA
from modules.utils.loader import load_erc20
from main_data.data import MULTICALL_ETH_CONTRACTS


class EvmBalanceChecker:
    # def __init__(self, list_pks: list):
    #     self.pks = list_pks

    @staticmethod
    def get_web3(chain):
        return Web3(
            provider=Web3.AsyncHTTPProvider(
                endpoint_uri=DATA[chain]['rpc'],
            ),
            modules={'eth': (AsyncEth,)},
            middlewares=[])

    async def get_tokens_data(self):
        list_symbols = {}
        for chain, coins in Value_EVM_Balance_Checker.evm_tokens.items():
            web3 = EvmBalanceChecker.get_web3(chain)
            list_symbols[chain] = {}
            for coin in coins:
                if coin != '':
                    coin = Web3.to_checksum_address(coin)
                    token_contract = web3.eth.contract(address=coin, abi=load_erc20())
                    try:
                        symbol = await token_contract.functions.symbol().call()
                        list_symbols[chain][coin] = symbol
                    except Exception as e:
                        print(f"Error fetching symbol for {coin}: {e}")

        return list_symbols

    async def fetch_price(self, session, symbol, url):
        try:
            async with session.get(url) as response:
                result = await response.json()
                price = result['USDT']
                self.prices[symbol] = float(price)
        except Exception as error:
            self.prices[symbol] = 0

    async def get_prices(self):
        self.prices = {}
        for chain, coins in Value_EVM_Balance_Checker.evm_tokens.items():
            web3 = self.get_web3(chain)
            for address_contract in coins:
                if address_contract == '':  # eth
                    symbol = DATA[chain]['token']
                else:
                    token_contract = web3.eth.contract(address=Web3.to_checksum_address(address_contract),
                                                       abi=load_erc20())
                    symbol = await token_contract.functions.symbol().call()

                self.prices.update({symbol: 0})

        async with aiohttp.ClientSession() as session:
            tasks = []
            for symbol in self.prices:
                if symbol == 'CORE':
                    url = f'https://min-api.cryptocompare.com/data/price?fsym=COREDAO&tsyms=USDT'
                else:
                    url = f'https://min-api.cryptocompare.com/data/price?fsym={symbol}&tsyms=USDT'

                tasks.append(self.fetch_price(session, symbol, url))

            await asyncio.gather(*tasks)

    async def get_balances(self, chain, wallets, tokens_list, symbols_list):

        if "" in tokens_list:
            index = tokens_list.index("")  # Находим индекс первого вхождения элемента
            tokens_list[index] = "0x0000000000000000000000000000000000000000"

        wallets_ = [Web3.to_checksum_address(wallet) for wallet in wallets]
        tokens_list = [Web3.to_checksum_address(token) for token in tokens_list]

        batch_limit = 1000
        print(chain)
        len_batch = math.floor(batch_limit / len(tokens_list))
        wallets_batches = [wallets_[i:i + len_batch] for i in range(0, len(wallets_), len_batch)]

        balances_dict = {}
        zero = 0
        for wallets_list in wallets_batches:
            max_attempts = 10
            for attempt in range(max_attempts):
                try:
                    web3 = EvmBalanceChecker.get_web3(chain)
                    abi = '[{"constant":true,"inputs":[{"name":"user","type":"address"},{"name":"token","type":"address"}],"name":"tokenBalance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"users","type":"address[]"},{"name":"tokens","type":"address[]"}],"name":"balances","outputs":[{"name":"","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"}]'
                    multicall_contract = web3.eth.contract(
                        address=Web3.to_checksum_address(MULTICALL_ETH_CONTRACTS[chain]), abi=abi)
                    multicall_result = await multicall_contract.functions.balances(
                        wallets_list, tokens_list
                    ).call()

                    zero += len(wallets_list)
                    multicall_result = [multicall_result[i:i + len(tokens_list)] for i in
                                        range(0, len(multicall_result), len(tokens_list))]

                    for number, wallet in enumerate(wallets_list):
                        balances = multicall_result[number]
                        balances_dict[wallet] = {}

                        for i, balance in enumerate(balances):
                            token = tokens_list[i]
                            if token == '0x0000000000000000000000000000000000000000':
                                symbol = DATA[chain]['token']
                            else:
                                symbol = symbols_list[chain][token]

                            balances_dict[wallet][symbol] = int(balance / 10 ** 6)
                    break

                except Exception as e:
                    await asyncio.sleep(1)
        print(balances_dict)
        return balances_dict

    async def evm_balances(self, tokens_data):

        wallets = [
            '0xec3d68dc25be091b812a67b075f4668e4e4183c3',
            '0x9d17bb55b57b31329cf01aa7017948e398b277bc',
            '0x0edefa91e99da1eddd1372c1743a63b1595fc413',
            '0xbdfa4f4492dd7b7cf211209c4791af8d52bf5c50',
            '0x41bc7d0687e6cea57fa26da78379dfdc5627c56d',
            '0x6cd68e8f04490cd1a5a21cc97cc8bc15b47dc9eb',
            '0x192820ce84fa9eb457fb228c386fe0ed22f7e33c',
            '0x0172e05392aba65366c4dbbb70d958bbf43304e4'
        ]
        chains = DATA.keys()
        # tokens_data = await self.get_tokens_data()
        tasks = []

        for chain in chains:
            if chain in tokens_data:
                tokens_list = tokens_data[chain].keys()
                symbols_list = tokens_data[chain].values()

                task = asyncio.create_task(self.get_balances(chain, wallets, tokens_list, symbols_list))
                tasks.append(task)

        results = await asyncio.gather(*tasks)

        return results


async def main():
    evm = EvmBalanceChecker()
    td = await evm.get_tokens_data()
    print(await evm.evm_balances(td))

if __name__ == "__main__":
    asyncio.run(main())