from pprint import pprint
import algokit_utils as algokit

def main():
    my_account = algokit.Account.new_account()

    print("address: ", my_account.address)

main()