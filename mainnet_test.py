#from cns.auto import ns
from cns import CNS, exceptions
import os
from dotenv import find_dotenv, load_dotenv
from cns.utils import Web3
from conftest import w3
from web3 import HTTPProvider, providers
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
    provider = HTTPProvider(os.environ.get("RPC_URL"))
    account = get_Account_From_Env()
    #w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
    #w3.eth.default_account = account.address
    #print(len(w3.middleware_onion))

    print(f"Your hot wallet address is {account.address}")
    #print(w3.eth.chain_id)

    # init the provider for ns
    ns = CNS(provider)
    result = ns.address('0xares.cfx')
    print(result)

    address = ns.owner('miner.cfx')
    print("owner of miner.cfx",address)

    ns.w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
    ns.w3.eth.default_account=ns.w3.eth.account.privateKeyToAccount(os.environ.get("PRIVATE_KEY")).address
    #print("account.address",account.address)
    nft_address = ns.address("miner.cfx")
    print("miner.cfx owned by",nft_address)
    
    print("default account",ns.w3.eth.default_account)

    email = ns.get_text('00000.cfx','email')
    print("email of 00000.cfx",email)

    avatar = ns.get_text('00000.cfx','avatar')
    print("avatar of 00000.cfx",avatar)

    twitter = ns.get_text('00000.cfx','twitter')
    print("twitter of 00000.cfx",twitter)

    description = ns.get_text('00000.cfx','description')
    print("description of 00000.cfx",description)

    github = ns.get_text('00000.cfx','github')
    print("github of 00000.cfx",github)



    #CNS._assert_control = lambda self, *args, **kwargs: None

    #result = ns.setup_address('miner.cfx','0xb75f07A2749a312496788a7b73fDD386EA529F2B')
    #print("setup_address result",result)
    