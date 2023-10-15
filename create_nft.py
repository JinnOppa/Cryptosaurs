# from py_algorand import Algorand
# from py_algorand.transaction import AssetConfigTxn, AssetTransferTxn
# from py_algorand.account import Account

# # Initialize Algorand client
# algod_token = "your-algod-token"
# algod_address = "https://testnet-algorand.api.purestake.io/ps2"
# algod_client = Algorand(algod_token, algod_address)

# # Define your account
# mnemonic = "your-mnemonic-phrase"
# account = Account(mnemonic)

# # Create the ASA
# asset_config = AssetConfigTxn(
#     sender=account.get_address(),
#     total=1,          # Total supply for NFT
#     decimals=0,       # NFTs typically have 0 decimals
#     default_frozen=False,  # Not frozen by default
#     unit_name="NFT",
#     asset_name="MyNFT",
#     manager=account.get_address(),
#     reserve=account.get_address(),
# )

# # Sign and send the transaction to create the ASA
# txn_id = algod_client.send_transaction(asset_config)

# # Wait for confirmation (you can implement this part)
# # ...

# # Mint the NFT
# mint_tx = AssetTransferTxn(
#     sender=account.get_address(),
#     receiver=account.get_address(),  # Mint to your own address
#     asset_id=txn_id,  # Asset ID from the previous transaction
#     amount=1,  # Minting 1 NFT
# )

# # Sign and send the minting transaction
# txn_id = algod_client.send_transaction(mint_tx)

# # Wait for confirmation (you can implement this part)
# # ...


from algosdk.v2client import algod
from algosdk import mnemonic
from algosdk.future.transaction import AssetConfigTxn, AssetTransferTxn

# Algorand Testnet node
algod_address = "https://testnet-algorand.api.purestake.io/ps2"
algod_token = "your-algod-token"
algod_client = algod.AlgodClient(algod_token, algod_address)

# Define your account
mnemonic_phrase = "your-mnemonic-phrase"
private_key = mnemonic.to_private_key(mnemonic_phrase)
sender_address = mnemonic.to_public_key(mnemonic_phrase)

# Create the ASA
asset_config = AssetConfigTxn(
    sender=sender_address,
    sp=params,
    index=None,  # Set to None for a new asset
    total=1,     # Total supply for NFT
    decimals=0,  # NFTs typically have 0 decimals
    default_frozen=False,  # Not frozen by default
    unit_name="NFT",
    asset_name="MyNFT",
    manager=sender_address,
    reserve=sender_address,
    freeze=None,   # Address that can freeze assets
    clawback=None,  # Address that can clawback assets
)

# Sign and send the transaction to create the ASA
transaction_id = algod_client.send_transaction(asset_config)
print("Asset ID: ", transaction_id)

# Wait for confirmation (you can implement this part)

# Mint the NFT
mint_tx = AssetTransferTxn(
    sender=sender_address,
    sp=params,
    index=transaction_id,  # Asset ID from the previous transaction
    receiver=sender_address,  # Mint to your own address
    amt=1,  # Minting 1 NFT
)

# Sign and send the minting transaction
mint_transaction_id = algod_client.send_transaction(mint_tx)
print("Minted NFT with ID: ", mint_transaction_id)

# Wait for confirmation (you can implement this part)
