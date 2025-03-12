import streamlit as st
from web3 import Web3
import json

# Connect to Ganache
infura_url = "http://127.0.0.1:8545/"  # Local blockchain
w3 = Web3(Web3.HTTPProvider(infura_url))

# Contract Address & ABI (Replace with your deployed contract address)
contract_address = "0x8464135c8F25Da09e49BC8782676a84730C318bC"




abi = json.loads('''[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "assetId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "fileHash",
				"type": "string"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			}
		],
		"name": "AssetRegistered",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "assetId",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "newFileHash",
				"type": "string"
			}
		],
		"name": "EvidenceUpdated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "uint256",
				"name": "assetId",
				"type": "uint256"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "assetId",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "fileHash",
				"type": "string"
			}
		],
		"name": "registerAsset",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "assetId",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "assetId",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "newFileHash",
				"type": "string"
			}
		],
		"name": "updateEvidence",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "assets",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "fileHash",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "currentOwner",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "assetId",
				"type": "uint256"
			}
		],
		"name": "getAsset",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			},
			{
				"internalType": "address[]",
				"name": "",
				"type": "address[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "assetId",
				"type": "uint256"
			}
		],
		"name": "getAssetHistory",
		"outputs": [
			{
				"internalType": "address[]",
				"name": "",
				"type": "address[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]''')



contract = w3.eth.contract(address=contract_address, abi=abi)

# UI
st.title("Chain of Custody - Asset Management")

# Register Asset
st.header("Register a New Asset")
asset_id = st.number_input("Asset ID", min_value=1, step=1)
asset_name = st.text_input("Asset Name")
file_hash = st.text_input("File Hash (IPFS/CID)")
if st.button("Register Asset"):
    tx_hash = contract.functions.registerAsset(asset_id, asset_name, file_hash).transact({"from": w3.eth.accounts[0]})
    st.success(f"Asset Registered! Tx Hash: {tx_hash.hex()}")

# Transfer Ownership
st.header("Transfer Ownership")
transfer_asset_id = st.number_input("Asset ID to Transfer", min_value=1, step=1)
new_owner = st.text_input("New Owner Address")
if st.button("Transfer"):
    tx_hash = contract.functions.transferOwnership(transfer_asset_id, new_owner).transact({"from": w3.eth.accounts[0]})
    st.success(f"Ownership Transferred! Tx Hash: {tx_hash.hex()}")

# View Asset
st.header("View Asset Details")
view_asset_id = st.number_input("Asset ID to View", min_value=1, step=1)
if st.button("Get Asset Details"):
    name, file_hash, owner, history = contract.functions.getAsset(view_asset_id).call()
    st.write(f"**Name:** {name}")
    st.write(f"**File Hash:** {file_hash}")
    st.write(f"**Current Owner:** {owner}")
    st.write(f"**Ownership History:** {history}")
