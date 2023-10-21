import algokit_utils as algokit
from pprint import pprint

def main():
    algod = algokit.get_algod_client(algokit.get_default_localnet_config("algod"))

    kmd = algokit.get_kmd_client_from_algod_client(algod)

    my_account = algokit.Account.new_account()
    print("address: ", my_account.address)

    pprint(algod.account_info(my_account.address))

    other_account = algokit.get_localnet_default_account(algod)

    txn = algokit.transfer(algod, algokit.TransferParameters(
        from_account = other_account.signer,
        to_address = my_account.address, 
        micro_algos = 1_000_000
        )
    )

    pprint(algod.account_info(my_account.address))

main()