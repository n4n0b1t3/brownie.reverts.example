# brownie.reverts.example
repository to solve a brownie.reverts() bug with reverted transactions

## On stackoverflow
[stackoverflow](https://stackoverflow.com/questions/71126128/)
[stackexchange](https://ethereum.stackexchange.com/questions/121687/)

# Brownie testing for reverted transactions does not work with pytest.raises() or brownie.reverts()
## Issue description 
Brownie tests containing either `pytest.raises(exceptions.VirtualMachineError)` or `brownie.reverts()` producing an error, when the request by design fails (is reverted). This producing an error, when the request by design fails (is reverted).

### Expected behavior:
The test should either fail or succeed, depending on the outcome of the transaction.

### Noticeable:
When the test is set up in a way, that the transaction is not reverted, the test works correctly without producing an error.

### What I have tried so far:
I reduced the code to remove all unnecessary dependencies to contain only the problematic parts. After a complete new setup of a python virtual environment with only the necessary features (described below under setup), I ran the code again, to make sure the issue prevails and is not solved.

### My setting:
The root directory contains the .venv virtual python environment. Under venv Cython and Brownie are installed. In VSC I am using the latest solidity compiler. In order to install ganache I opened a powershell with admin rights and activated the virtual environment, installed nodeenv, and connected it with venv. After this step I installed ganache and tested it. Everything is working correctly. Complete projects are tested and work correctly in this setup, besides tests with brownie.reverts().

### Here in short the command line overview:
```
projectroot>.\.venv\Scripts\Activate.ps1
(.venv) projectroot>pip install nodeenv
(.venv) projectroot>nodeenv -p
(.venv) projectroot>npm install -g ganache
(.venv) projectroot>ganache --version
(.venv) projectroot>mkdir sourcecode
(.venv) projectroot>cd sourcecode
(.venv) sourcecode>brownie init
(.venv) sourcecode>brownie --version
```
