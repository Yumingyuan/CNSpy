#from cns.auto import ns
from cns import CNS, exceptions
import os
from dotenv import find_dotenv, load_dotenv
from cns.utils import Web3
from conftest import w3
from web3 import HTTPProvider
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3.auto import w3
from web3.middleware import construct_sign_and_send_raw_middleware
from web3.eth import Account


def get_Account_From_Env():
    private_key = os.environ.get("PRIVATE_KEY")
    assert private_key is not None, "You must set PRIVATE_KEY environment variable"
    assert private_key.startswith("0x"), "Private key must start with 0x hex prefix"
    account = Account.from_key(private_key)
    return account

if __name__=="__main__":
    # load .env file
    load_dotenv(find_dotenv('.env'))
    # import the RPC
    provider = HTTPProvider(os.environ.get("RPC_URL"),)
    #print(provider.isConnected())
    account = get_Account_From_Env()
    #w3.middleware_stack.add(construct_sign_and_send_raw_middleware('ENS_OWNER_PRIVATE_KEY'))
    #w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
    #w3.eth.default_account = account.address
    #print(len(w3.middleware_onion))

    print(f"Your hot wallet address is {account.address}")
    #print(w3.eth.chain_id)

    # init the provider for ns
    ns = CNS(provider)
    result = ns.address('0xares.cfx')
    print(result)
    #resolver_result = ns.resolver('conflux.cfx')
    #print(resolver_result.address)
    #result = ns.w3.eth.account.from_key(os.environ.get("PRIVATE_KEY"))

    address = ns.owner('miner.cfx')
    print("owner of miner.cfx",address)

    #print("get result",result.address)
    result = ns.w3.eth.account.privateKeyToAccount(os.environ.get("PRIVATE_KEY"))
    print("private key to account",result)
    #ns.w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
    ns.w3.eth.default_account=ns.w3.eth.account.privateKeyToAccount(os.environ.get("PRIVATE_KEY")).address
    #print("account.address",account.address)
    nft_address = ns.address("miner.cfx")
    print("miner.cfx owned by",nft_address)
    
    print("default account",ns.w3.eth.default_account)

    ns.setup_address('miner.cfx','0xb75f07A2749a312496788a7b73fDD386EA529F2B')
    

'''
    print("+++++++++++++++++++++++++++ Get the Address for an ENS Name +++++++++++++++++++++++++++")
    eth_address = ns.address('ferf.cfx')
    print(eth_address,"have registered for: ferf.cfx")
    print("+++++++++++++++++++++++++ Get the Address for an ENS Name end +++++++++++++++++++++++++\n")

    print("+++++++++++++++++++++++++++ Get the ENS Name for an Address +++++++++++++++++++++++++++")
    domain = ns.name('0xb75f07A2749a312496788a7b73fDD386EA529F2B')
    if domain is None:
        print("Checking your reverse setting status!")
    else:
        print("0x103af2b33400a4f955744a7f70e749435444f808 hold",domain)
    print("+++++++++++++++++++++++++ Get the ENS Name for an Address end +++++++++++++++++++++++++\n")

    print("+++++++++++++++++++++++++++++++ Get the Owner of a Name +++++++++++++++++++++++++++++++")
    cfx_address = ns.owner('0xares.cfx')
    print(cfx_address,"owns 0xareas.cfx")
    print("+++++++++++++++++++++++++++++ Get the Owner of a Name end +++++++++++++++++++++++++++++\n")

    print("++++++++++++++++++++++++++++++ Link a Name to an Address +++++++++++++++++++++++++++++++")
    try:
        ns.setup_address('0xares.cfx')
    except exceptions.UnauthorizedError:
        print("You must control the account who owns 0xares.cfx")
    print("++++++++++++++++++++++++++++ Link a Name to an Address end +++++++++++++++++++++++++++++\n")'''

