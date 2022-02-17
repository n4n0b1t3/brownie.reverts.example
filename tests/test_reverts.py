import brownie
import pytest
from brownie import ExampleContract, accounts, exceptions


def test_only_owner_can_withdraw():
    example_contract = ExampleContract.deploy({"from": accounts[0]})
    print(f"example_contract deployed to {example_contract.address}")
    good = accounts[0]
    bad = accounts.add()
    example_contract.withdraw({"from": bad})
    with pytest.raises(exceptions.VirtualMachineError):
        example_contract.withdraw({"from": good})

    # brownie.reverts example
    # with brownie.reverts():
    #    example_contract.withdraw({"from": good})
