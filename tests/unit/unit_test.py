from scripts.helpful_scripts import get_account
from brownie import ShelterCollectible, ShelterMarketplace, config, network, exceptions
import pytest
from web3 import Web3

MINT_PRICE = Web3.toWei(0.0001, "ether")


def test_can_deploy():
    account = get_account()
    shelter_collectible = ShelterCollectible.deploy({"from": account},
                                                    publish_source=config["networks"][network.show_active()]["verify"])
    print(f"Shelter Collectible deployed at {shelter_collectible.address}")
    shelter_marketplace = ShelterMarketplace.deploy(shelter_collectible.address, {"from": account},
                                                    publish_source=config["networks"][network.show_active()]["verify"])
    print(f"Shelter Marketplace deployed at {shelter_marketplace.address}")
    tx_marketplace = shelter_collectible.setMarketplace(shelter_marketplace.address, {"from": account})
    tx_marketplace.wait(1)
    assert True


def test_only_admin_can_mint():
    non_admin_account = get_account(index=1)
    shelter_collectible = ShelterCollectible[-1]
    shelter_marketplace = ShelterMarketplace[-1]
    fake_uri = "https://test.test"
    with pytest.raises(exceptions.VirtualMachineError):
        tx_mint = shelter_collectible.mint(fake_uri,
                                           shelter_marketplace.address,
                                           {"from": non_admin_account})


def test_cannot_adopt_adopted():
    admin_account = get_account()
    first_adopter = get_account(index=1)
    second_adopter = get_account(index=2)
    shelter_collectible = ShelterCollectible[-1]
    shelter_marketplace = ShelterMarketplace[-1]
    fake_uri = "https://test.test"
    tx_mint = shelter_collectible.mint(fake_uri,
                                       shelter_marketplace.address,
                                       {"from": admin_account})
    tx_mint.wait(1)
    tx_adopt = shelter_marketplace.adopt(0, {"from": first_adopter, "value": MINT_PRICE})
    tx_adopt.wait(1)

    with pytest.raises(exceptions.VirtualMachineError):
        tx_adopt_2 = shelter_marketplace.adopt(0, {"from": second_adopter, "value": MINT_PRICE})
