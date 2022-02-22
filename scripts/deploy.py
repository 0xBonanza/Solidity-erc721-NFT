from scripts.helpful_scripts import get_account
from scripts.ipfs_upload import publish_collectibles
from brownie import ShelterCollectible, ShelterMarketplace, config, network
from web3 import Web3

MINT_PRICE = Web3.toWei(0.0001, "ether")
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def deploy_contract():
    account = get_account()
    shelter_collectible = ShelterCollectible.deploy({"from": account},
                                                    publish_source=config["networks"][network.show_active()]["verify"])
    print(f"Shelter Collectible deployed at {shelter_collectible.address}")
    shelter_marketplace = ShelterMarketplace.deploy(shelter_collectible.address, {"from": account},
                                                    publish_source=config["networks"][network.show_active()]["verify"])
    print(f"Shelter Marketplace deployed at {shelter_marketplace.address}")
    tx_marketplace = shelter_collectible.setMarketplace(shelter_marketplace.address, {"from": account})
    tx_marketplace.wait(1)
    print(f"Marketplace set for ShelterCollectible!")


def upload_nft():
    publish_collectibles()


def mint_nft():
    account = get_account()
    shelter_collectible = ShelterCollectible[-1]
    shelter_marketplace = ShelterMarketplace[-1]
    sample_uri = "https://ipfs.io/ipfs/QmXj26PLa5SmBMGmq6cLurpcSkDnVtgnfJ7W4R68jQbjtf?filename=0.json"
    tx_mint = shelter_collectible.mint(sample_uri,
                                       shelter_marketplace.address,
                                       {"from": account})
    tx_mint.wait(1)
    print(f"Token minted to {shelter_marketplace.address}")
    if config["networks"][network.show_active()] == "rinkeby":
        print(f"You can view your NFT at: "
              f"{OPENSEA_URL.format(shelter_collectible.address, 0)}")


def adopt():
    account = get_account()
    adoption_token = 0
    shelter_collectible = ShelterCollectible[-1]
    shelter_marketplace = ShelterMarketplace[-1]
    tx_adopt = shelter_marketplace.adopt(adoption_token, {"from": account, "value": MINT_PRICE})
    tx_adopt.wait(1)
    print(f"Token adopted by {account}")
    print(f"Token ownership confirmed to {shelter_collectible.ownership(adoption_token)} ")


def main():
    deploy_contract()
    mint_nft()
    adopt()
