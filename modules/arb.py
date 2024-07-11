import asyncio

from web3 import Web3
from web3.eth import AsyncEth

from main_data.data import DATA


class AutoWithdraw:
    def __init__(self, private_key: str, receiver_address: str):
        self.private_key = private_key
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

        assert await AutoWithdraw.check_rpc(w3) is True, "rpc doesn't work"
        return w3

    async def get_sender(self, w3: Web3):
        account = await w3.eth.account.from_key(self.private_key)
        address = account.address
        return address

    async def create_tx(self, chain_id, w3: Web3):
        balance = await w3.eth.get_balance(await self.get_sender(w3))
        default_gas_price = await w3.eth.gas_price

        transaction = {
            'to': self.receiver_address,
            'value': balance,
            'gasPrice': default_gas_price,
            'nonce': w3.eth.get_transaction_count(await self.get_sender(w3)),
            'chainId': chain_id
        }

        gas_limit = await w3.eth.estimate_gas(transaction)
        gas_cost = default_gas_price * gas_limit
        value = balance - gas_cost

        assert value > 0, 'Недостаточно средств для покрытия газа за транзу'
        transaction['value'] = value
        transaction['gas'] = gas_limit

        return transaction

    async def send_tx(self, net_name):
        chain_id, rpc = DATA[net_name]['chain_id'], DATA[net_name]['rpc']
        print(f'Process tx in {net_name} net ({chain_id}) via this rpc: {rpc}')
        w3 = AutoWithdraw.get_w3(rpc)
        tx = self.create_tx(chain_id)
        signed_txn = await w3.eth.account.sign_transaction(tx, self.private_key)
        txn_hash = await w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        txn_receipt = await w3.eth.wait_for_transaction_receipt(txn_hash)
        return f'Transaction in {net_name} net is approved: {txn_receipt}'

    async def nets(self):
        tasks = []

        for net_name in DATA.keys():
            task = asyncio.create_task(self.send_tx(net_name))
            tasks.append(task)

        results = asyncio.gather(*tasks)
        return results