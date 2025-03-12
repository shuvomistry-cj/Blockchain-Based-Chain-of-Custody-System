// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ChainOfCustody {
    struct Asset {
        string name;
        string fileHash; // Stores the hash or IPFS CID of the evidence file
        address currentOwner;
        address[] history;
    }

    mapping(uint256 => Asset) public assets;

    event AssetRegistered(uint256 indexed assetId, string name, string fileHash, address indexed owner);
    event OwnershipTransferred(uint256 indexed assetId, address indexed newOwner);
    event EvidenceUpdated(uint256 indexed assetId, string newFileHash);

    function registerAsset(uint256 assetId, string memory name, string memory fileHash) public {
        require(assets[assetId].currentOwner == address(0), "Asset already registered");

        address[] memory emptyHistory;
        assets[assetId] = Asset({
            name: name,
            fileHash: fileHash, // Store file reference
            currentOwner: msg.sender,
            history: emptyHistory
        });

        assets[assetId].history.push(msg.sender);

        emit AssetRegistered(assetId, name, fileHash, msg.sender);
    }

    function transferOwnership(uint256 assetId, address newOwner) public {
        require(assets[assetId].currentOwner == msg.sender, "Only owner can transfer");

        assets[assetId].currentOwner = newOwner;
        assets[assetId].history.push(newOwner);

        emit OwnershipTransferred(assetId, newOwner);
    }

    function updateEvidence(uint256 assetId, string memory newFileHash) public {
        require(assets[assetId].currentOwner == msg.sender, "Only owner can update evidence");

        assets[assetId].fileHash = newFileHash;

        emit EvidenceUpdated(assetId, newFileHash);
    }

    function getAssetHistory(uint256 assetId) public view returns (address[] memory) {
        return assets[assetId].history;
    }

    function getAsset(uint256 assetId) public view returns (string memory, string memory, address, address[] memory) {
        Asset storage asset = assets[assetId];
        return (asset.name, asset.fileHash, asset.currentOwner, asset.history);
    }
}
