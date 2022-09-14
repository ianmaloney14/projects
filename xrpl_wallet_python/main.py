if __name__ == '__main__':

    # Define the network client
    from xrpl.clients import JsonRpcClient

    JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
    client = JsonRpcClient(JSON_RPC_URL)
    print("Nothing failed so far")

    from xrpl.wallet import generate_faucet_wallet
    test_wallet = generate_faucet_wallet(client, debug=True)
    print(test_wallet)

    # Prepare a payment transaction
    from xrpl.models.transactions import Payment
    from xrpl.utils import xrp_to_drops
    my_tx_payment = Payment(
        account=test_wallet.classic_address,
        amount=xrp_to_drops(22),
        destination="rpspfHe3n9trZX94B42BHs1tTq4Vubc7Cd",
    )

    # Sign the transaction
    from xrpl.transaction import safe_sign_and_autofill_transaction
    my_tx_payment_signed = safe_sign_and_autofill_transaction(my_tx_payment, test_wallet, client)

    # Submit and send the transaction
    from xrpl.transaction import send_reliable_submission
    tx_response = send_reliable_submission(my_tx_payment_signed, client)
    print(tx_response)