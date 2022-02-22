from scripts.helpful_scripts import get_account
from scripts.ipfs_upload import publish_collectibles
from brownie import ShelterCollectible, ShelterMarketplace, config, network
from web3 import Web3

MINT_PRICE = Web3.toWei(0.0001, "ether")
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def test_all():
    # deploy
    account = get_account()
    shelter_collectible = ShelterCollectible.deploy({"from": account},
                                                    publish_source=config["networks"][network.show_active()]["verify"])
    shelter_marketplace = ShelterMarketplace.deploy(shelter_collectible.address, {"from": account},
                                                    publish_source=config["networks"][network.show_active()]["verify"])
    tx_marketplace = shelter_collectible.setMarketplace(shelter_marketplace.address, {"from": account})
    tx_marketplace.wait(1)

    # mint
    sample_uri = "https://ipfs.io/ipfs/QmXj26PLa5SmBMGmq6cLurpcSkDnVtgnfJ7W4R68jQbjtf?filename=0.json"
    tx_mint = shelter_collectible.mint(sample_uri,
                                       shelter_marketplace.address,
                                       {"from": account})
    tx_mint.wait(1)

    # adopt
    account_1 = get_account(index=1)
    adoption_token = 0
    tx_adopt = shelter_marketplace.adopt(adoption_token, {"from": account_1, "value": MINT_PRICE})
    tx_adopt.wait(1)

    assert True
