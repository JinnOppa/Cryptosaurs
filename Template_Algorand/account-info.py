from pprint import pprint
import algokit_utils as algokit

def main():
    my_account = algokit.Account.new_account()

    print("address: ", my_account.address)


    algod = algokit.get_algod_client(algokit.get_default_localnet_config("algod"))

    pprint(algod.account_info(my_account.address))

    kmd = algokit.get_kmd_client_from_algod_client(algod)

    algokit.ensure_funded(
        algod,
        algokit.EnsureBalanceParameters(
            account_to_fund = my_account,
            min_spending_balance_micro_algos = 1_000_000
        )
    )

    pprint(algod.account_info(my_account.address))

main()