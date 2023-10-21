import algosdk
import algokit_utils as algokit
from pprint import pprint

def main():
    my_account = algokit.Account.new_account()
    print("address: ", my_account.address)

    algod = algokit.get_algod_client(algokit.get_default_localnet_config("algod"))

    pprint(algod.account_info(my_account.address))

    kmd = algokit.get_kmd_client_from_algod_client(algod)

    algokit.ensure_funded(
        algod,
        algokit.EnsureBalanceParameters(
            account_to_fund=my_account.address,
            min_spending_balance_micro_algos=1_000_000
        )
    )

    unsigned_txn = algosdk.transaction.AssetCreateTxn(
        sender=my_account.address,
        sp=algod.suggested_params(),
        total=1,
        decimals=0,
        default_frozen=False
    )

    signed_txn = unsigned_txn.sign(my_account.private_key)
 
    txid = algod.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))     
 
    pprint(algod.account_info(my_account.address))

    results = algod.pending_transaction_info(txid)
    assetID = results["asset-index"]
    print("assetID: ", assetID)



    other_account = algokit.Account.new_account()
    print("address: ", other_account.address)

    algokit.ensure_funded(
        algod,
        algokit.EnsureBalanceParameters(
            account_to_fund=other_account.address,
            min_spending_balance_micro_algos=1_000_000
        )
    ) 

    unsigned_txn = algosdk.transaction.AssetTransferTxn(
        sender=other_account.address,
        sp=algod.suggested_params(),
        receiver=other_account.address,
        amt=0,
        index=assetID,
    )

    signed_txn = unsigned_txn.sign(other_account.private_key)
 
    txid = algod.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))

    pprint(algod.account_info(other_account.address))

    unsigned_txn = algosdk.transaction.AssetTransferTxn(
        sender=my_account.address,
        sp=algod.suggested_params(),
        receiver=other_account.address,
        amt=1,
        index=assetID,
    )

    signed_txn = unsigned_txn.sign(my_account.private_key)
 
    txid = algod.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))

    pprint(algod.account_info(other_account.address))

main()