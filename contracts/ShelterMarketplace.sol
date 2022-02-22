// SPDX-License-Identifier: MIT

pragma solidity ^0.7.0;

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "./ShelterCollectible.sol";

contract ShelterMarketplace is Ownable {

    ShelterCollectible public shelterCollectible;

    constructor(address _shelterCollectibleAddress) public {
        shelterCollectible = ShelterCollectible(_shelterCollectibleAddress);
    }

    // we assign a new token ID to a new user
    function adopt(uint256 _tokenId) public payable {
        require(msg.value >= shelterCollectible.adoptionPrice(_tokenId), "Adoption price not reached!");
        require(shelterCollectible.canAdopt(_tokenId) == true, "This item cannot be adopted!");
        shelterCollectible.safeTransferFrom(address(this), msg.sender, _tokenId);
        shelterCollectible.setAfterAdopt(_tokenId, msg.sender);
    }

}