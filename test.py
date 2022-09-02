from cns.auto import ns
from cns import CNS, exceptions

if __name__=="__main__":
    print("+++++++++++++++++++++++++++ Get the Address for an ENS Name +++++++++++++++++++++++++++")
    eth_address = ns.address('ferf.cfx')
    print(eth_address,"have registered for: ferf.cfx")
    print("+++++++++++++++++++++++++ Get the Address for an ENS Name end +++++++++++++++++++++++++\n")

    print("+++++++++++++++++++++++++++ Get the ENS Name for an Address +++++++++++++++++++++++++++")
    domain = ns.name('0x103af2b33400a4f955744a7f70e749435444f808')
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
    print("++++++++++++++++++++++++++++ Link a Name to an Address end +++++++++++++++++++++++++++++\n")

