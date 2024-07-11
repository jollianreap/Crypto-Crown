from web3 import Web3

sender_address = ""
receiver_address = ""
private_key = ""

arb_rpc = "https://arbitrum.blockpi.network/v1/rpc/public"
web3 = Web3(Web3.HTTPProvider(arb_rpc))

# ---------- Проверка подключения ----------
if web3.is_connected():
    print("Подключение к сети Arbitrum установлено")
else:
    print("Не удалось подключиться к сети Arbitrum")


# ---------- Получение баланса отправителя в Wei ----------
balance = web3.eth.get_balance(sender_address)

# ---------- Определение базовой цены газа ----------
gas_price = web3.eth.gas_price

transaction = {
    'to': receiver_address,
    'value': balance,
    'gasPrice': gas_price,
    'nonce': web3.eth.get_transaction_count(sender_address),
    'chainId': 42161  # Идентификатор сети Arbitrum mainnet
}

# ---------- Оценка лимита газа ----------
gas_limit = web3.eth.estimate_gas(transaction)

# ---------- Перерасчет значения транзакции с учетом лимита газа ----------
gas_cost = gas_price * gas_limit
value = balance - gas_cost

# ---------- Проверка, что баланс достаточен для оплаты комиссии за газ ----------
if value < 0:
    raise Exception("Недостаточно средств для покрытия комиссии за газ")

# ---------- Обновление значения транзакции с учетом нового значения value ----------
transaction['value'] = value
transaction['gas'] = gas_limit

# ---------- Подписание транзакции ----------
signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

# ---------- Отправка транзакции ----------
txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

# ---------- Получение хеша транзакции ----------
print(f"Хеш транзакции: {txn_hash.hex()}")

# ---------- Ожидание подтверждения транзакции ----------
txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
print(f"Транзакция подтверждена: {txn_receipt}")
