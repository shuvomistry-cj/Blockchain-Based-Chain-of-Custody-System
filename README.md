# Work in Progress............

🔗 Chain of Custody - Secure Asset Tracking on Blockchain
🚀 Project Workflow
1️⃣ User Opens Streamlit App

Streamlit-based UI loads.
MetaMask prompt appears for wallet connection.
2️⃣ Register an Asset

User inputs Asset ID and Description.
MetaMask signs the transaction.
Asset details are stored on Ethereum (Hardhat) blockchain.
3️⃣ Transfer Asset Ownership

Current owner enters new owner’s address.
MetaMask signs transaction.
Ownership record updates on blockchain.
4️⃣ Verify Custody History

Anyone can enter Asset ID to check past ownership.
Smart contract fetches and returns transaction history.
5️⃣ Streamlit Displays Ownership Data

UI dynamically shows real-time ownership history.
⚙ Tech Stack Overview
Component	Technology Used
Frontend (UI)	Streamlit (Python)
Blockchain	Ethereum (Hardhat Network)
Wallet Auth	MetaMask (Web3.js in Streamlit)
Backend	Flask + Web3.py
Smart Contract	Solidity (Remix + Hardhat)
Data Storage	Blockchain (Immutable Ledger)
📌 Next Steps
✔ Finalize Solidity Smart Contract (Asset Registration + Transfer).
✔ Deploy Smart Contract on Hardhat Local Network.
✔ Build Streamlit UI for User Interaction.
✔ Develop Flask Backend for Blockchain Integration (Web3.py).

Would you like sample code for Streamlit & Web3.py integration? 🚀
