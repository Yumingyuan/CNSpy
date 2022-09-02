from cns.auto import ns
from cns import CNS

if __name__=="__main__":
    print("+++++++++++++++++++++++++++ Get the Address for an ENS Name +++++++++++++++++++++++++++")
    eth_address = ns.address('ferf.cfx')
    print(eth_address,"have registered for: ferf.cfx")
    print("+++++++++++++++++++++++++ Get the Address for an ENS Name end +++++++++++++++++++++++++")

    print("+++++++++++++++++++++++++++ Get the ENS Name for an Address +++++++++++++++++++++++++++")
    domain = ns.name('0x103af2b33400a4f955744a7f70e749435444f808')
    if domain is None:
        print("Checking your reverse setting status!")
    else:
        print("0x103af2b33400a4f955744a7f70e749435444f808 hold",domain)
    print("+++++++++++++++++++++++++ Get the ENS Name for an Address end +++++++++++++++++++++++++")

    ##ns.setup_address('jasoncarver.cfx')

