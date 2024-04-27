from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

rpc_user = '12345'
rpc_password = '12345'
rpc_connection = AuthServiceProxy(f'http://{rpc_user}:{rpc_password}@127.0.0.1:5415')

try:
    addresses = rpc_connection.listaddressgroupings()
    with open("Only-private-keys.txt", "w") as file:
        for group in addresses:
            for address_info in group:
                private_key = rpc_connection.dumpprivkey(address_info[0])
                file.write(f"{private_key}\n")
    print("Private keys successfully saved in private_keys.txt file")
except JSONRPCException as e:
    print(e)
