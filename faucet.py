from web3 import Web3

web3 = Web3(Web3.HTTPProvider('YOUR_PROVIDER_URL'))

sender_address = 'SENDER WALLET ADDRESS'
private_key = 'YOUR PRIVATE KEY'
token_contract_address = 'YOUR TOKEN CONTRACT ADDRESS'
token_abi = []

token_contract = web3.eth.contract(address=token_contract_address, abi=token_abi)
recipient_address = 'RECIPIENT ADDRESS'
amount = 100

decimals = token_contract.functions.decimals().call()
token_amount = amount * 10**decimals

nonce = web3.eth.get_transaction_count(sender_address)
tx = token_contract.functions.transfer(recipient_address, token_amount).build_transaction({
    'nonce': nonce,
    'gas': 2000000,
    'gasPrice': web3.to_wei('10', 'gwei'),
})

signed_txn = web3.eth.account.sign_transaction(tx, private_key=private_key)
tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

print(f'Transaction hash: {web3.to_hex(tx_hash)}')
