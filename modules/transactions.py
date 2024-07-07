import os
import json
from eth_account import Account
from web3 import Web3
from setting import MAX_GAS_CHARGE, MAINNET_RPC_URLS, LAYER2_RPC_URLS, NONEVM_RPC_URLS


def get_wallet_addresses(file_path):
    """
    Извлекает адреса кошельков из текстового файла с сид фразами или приватными ключами.
    """
    wallet_addresses = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                private_key = line.strip()
                wallet = Account.from_key(private_key)
                wallet_addresses.append(wallet.address)
            except:
                pass
    return wallet_addresses


def check_balances(wallet_addresses):
    """
    Проверяет баланс на каждом адресе во всех сетях.
    """
    balances = {}
    for network, rpc_urls in {
        'Mainnet': MAINNET_RPC_URLS,
        'Layer2': LAYER2_RPC_URLS,
        'Non-EVM': NONEVM_RPC_URLS
    }.items():
        for url in rpc_urls:
            w3 = Web3(Web3.HTTPProvider(url))
            for address in wallet_addresses:
                balance = w3.eth.get_balance(address)
                if balance > 0:
                    if address not in balances:
                        balances[address] = {}
                    balances[address][network] = w3.from_wei(balance, 'ether')
    return balances


def withdraw_funds(wallet_addresses, withdrawal_address, withdrawal_amount):
    """
    Выводит средства с найденных адресов на указанный адрес.
    """
    for address in wallet_addresses:
        for network, rpc_urls in {
            'Mainnet': MAINNET_RPC_URLS,
            'Layer2': LAYER2_RPC_URLS,
            'Non-EVM': NONEVM_RPC_URLS
        }.items():
            for url in rpc_urls:
                w3 = Web3(Web3.HTTPProvider(url))
                if address in w3.eth.get_balance(address) > 0:
                    tx = {
                        'to': withdrawal_address,
                        'value': w3.to_wei(withdrawal_amount, 'ether'),
                        'gas': w3.eth.estimate_gas({'to': withdrawal_address, 'from': address, 'value': w3.to_wei(withdrawal_amount, 'ether')}),
                        'gasPrice': w3.to_wei(MAX_GAS_CHARGE[network.lower()], 'gwei'),
                        'nonce': w3.eth.get_transaction_count(address)
                    }
                    signed_tx = w3.eth.account.sign_transaction(tx, private_key=w3.eth.account.from_key(address).key)
                    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
                    print(f"Транзакция отправлена в сети {network}: {w3.to_hex(tx_hash)}")


if __name__ == "__main__":
    file_path = input("Введите путь к файлу с сид фразами или приватными ключами: ")
    withdrawal_address = input("Введите адрес для вывода средств: ")
    withdrawal_amount = float(input("Введите сумму для вывода (в ETH): "))

    wallet_addresses = get_wallet_addresses(file_path)
    balances = check_balances(wallet_addresses)
    print("Найденные балансы:")
    print(json.dumps(balances, indent=2))

    withdraw_funds(wallet_addresses, withdrawal_address, withdrawal_amount)