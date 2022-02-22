// SPDX-License-Identifier: MIT

pragma solidity ^0.7.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ShelterCollectible is ERC721, Ownable {

    uint256 public tokenCounter;
    uint256 public basePrice;
    mapping(uint256 => address) public ownership;
    mapping(uint256 => bool) public canAdopt;
    mapping(uint256 => uint256) public adoptionPrice;
    address public marketplace;

    modifier onlyMarket {
        require(msg.sender == marketplace);
        _;
    }

    constructor () public ERC721 ("TEST 1", "SHTD"){
        tokenCounter = 0;
    }

    // set base price
    function setBasePrice(uint256 _price) public onlyOwner {
        basePrice = _price;
    }

    // set marketplace address
    function setMarketplace(address _marketplace) public onlyOwner {
        marketplace = _marketplace;
    }

    // ONLY MARKET: change the adoption status and owner after adoption
    function setAfterAdopt(uint256 _tokenId, address _newOwner) public onlyMarket {
        canAdopt[_tokenId] = false;
        ownership[_tokenId] = _newOwner;
    }

    // ONLY OWNER: mint a new token directly to the marketplace
    function mint(string memory _tokenURI, address _marketplace) public onlyOwner returns (uint256) {
        uint256 newTokenId = tokenCounter;
        _mint(_marketplace, newTokenId);
        _setTokenURI(newTokenId, _tokenURI);
        ownership[newTokenId] = _marketplace;
        canAdopt[newTokenId] = true;
        adoptionPrice[newTokenId] = basePrice;
        tokenCounter++;
        return newTokenId;
    }

}