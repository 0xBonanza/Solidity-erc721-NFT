from brownie import (
    network,
    config,
    accounts,
    Contract,
)

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS \
            or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    # returns by default
    return accounts.add(config["wallets"]["from_key"])
