from typing import List
import asyncio

from web3 import Web3
from web3.eth import AsyncEth

from main_data.data import DATA


class AutoWithdraw:
    """
    Class to transfer all native currencies from many wallets
    """
    def __init__(self, private_keys: List, receiver_address: str):
        self.private_keys = private_keys
        self.receiver_address = receiver_address

    @staticmethod
    async def check_rpc(w3: Web3):
        if await w3.is_connected():
            return True

        return False

    @staticmethod
    async def get_w3(rpc):
        w3 = Web3(
            provider=Web3.AsyncHTTPProvider(
                endpoint_uri=rpc,
                # request_kwargs={'proxy': self.proxy, 'headers': self.headers}
            ),
            modules={'eth': (AsyncEth,)},
            middlewares=[]
        )

        if await AutoWithdraw.check_rpc(w3) is True:
            return w3

        return None

    def get_sender(self, w3: Web3, pk: str):
        account = w3.eth.account.from_key(pk)
        address = account.address
        return address

    async def create_tx(self, chain_id, w3: Web3, pk: str):
        balance = await w3.eth.get_balance(self.get_sender(w3, pk))
        default_gas_price = await w3.eth.gas_price

        transaction = {
            'to': self.receiver_address,
            'value': balance,
            'gasPrice': default_gas_price,
            'nonce': await w3.eth.get_transaction_count(self.get_sender(w3, pk)),
            'chainId': chain_id
        }

        gas_limit = await w3.eth.estimate_gas(transaction)
        gas_cost = default_gas_price * gas_limit
        value = balance - gas_cost

        transaction['value'] = value
        transaction['gas'] = gas_limit

        if value > 0:
            return transaction

        return False

    async def send_tx(self, net_name: str, pk: str):
        try:
            chain_id, rpc = DATA[net_name]['chain_id'], DATA[net_name]['rpc']
            print(f'Process tx in {net_name} net ({chain_id}) via this rpc: {rpc}')
            w3 = await AutoWithdraw.get_w3(rpc)
            if isinstance(w3, Web3):
                tx = await self.create_tx(chain_id, w3, pk)
                if isinstance(tx, dict):
                    signed_txn = w3.eth.account.sign_transaction(tx, pk)
                    txn_hash = await w3.eth.send_raw_transaction(signed_txn.rawTransaction)
                    txn_receipt = await w3.eth.wait_for_transaction_receipt(txn_hash)
                    return f'Transaction in {net_name} net is approved: {txn_receipt}'

                return f'Not enough money for transaction in {net_name}'

            else:
                return f"RPC of {net_name} doesn't work: {rpc}"
        except Exception as e:
            return f'Got unexpected error: {e}'

    async def process_key(self, pk: str):
        tasks = []
        for net_name in DATA.keys():
            task = asyncio.create_task(self.send_tx(net_name, pk))
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        return results

    async def get_results(self):
        result = {}
        for private_key in self.private_keys:
            result[private_key] = await self.process_key(private_key)

        return result
