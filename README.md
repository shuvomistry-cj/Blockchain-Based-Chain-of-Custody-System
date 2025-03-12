# Chain of Custody - Asset Management

## Description
This is a blockchain-based **Chain of Custody** system built using **Solidity** and **Hardhat** for tracking the ownership of digital assets. It allows users to register digital assets, transfer ownership, and retrieve asset history. The project also supports **IPFS** for storing evidence files (e.g., PDFs) as decentralized assets.

## Features
- **Register digital assets** with unique IDs.
- **Transfer ownership** of assets securely.
- **Store and retrieve asset history** on the blockchain.
- **Upload digital evidence files** (PDFs, images, or other documents) and store their IPFS hash.
- **Frontend built using Python & Web3** to interact with the smart contract.

## Technologies Used
- **Solidity** (Smart Contract Development)
- **Hardhat** (Development & Testing)
- **Metamask** (Wallet Integration)
- **IPFS** (Decentralized File Storage)
- **Python (Flask / Streamlit)** (Frontend & Backend)
- **Web3.py** (Blockchain Interaction)

## Installation & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/shuvomistry-cj/Blockchain-Based-Chain-of-Custody-System.git
```

### 2. Install Dependencies
#### Install Hardhat & Node.js dependencies:
```bash
npm install
```
#### Install Python dependencies:
```bash
pip install -r requirements.txt
```

### 3. Start Local Blockchain (Hardhat)
```bash
npx hardhat node
```

### 4. Deploy Smart Contract
```bash
npx hardhat run scripts/deploy.js --network localhost
```

### 5. Run the Python Frontend
```bash
python app.py
```

### 6. Connect MetaMask to Hardhat Localhost
- Open **MetaMask**.
- Add a new **network** with RPC URL: `http://127.0.0.1:8545`.
- Import an account using a private key from Hardhat.

### 7. Upload Files to IPFS (Optional)
You can use **Pinata** or **Infura** to upload files and get their **IPFS CID**. Add the CID as a file hash when registering assets.

## Usage
- Register a new asset by providing **Asset ID**, **Asset Name**, and **File Hash (IPFS CID)**.
- Transfer ownership to another Ethereum address.
- View asset details, including current owner and ownership history.

![Image](https://github.com/user-attachments/assets/38834113-1fad-429a-b529-54af08e9d7a0)

## License
This project is licensed under the MIT License.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For any queries, feel free to reach out at [your-email@example.com].

