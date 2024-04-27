First thing make new folder and put 2 scripts inside the new folder

1- Make Rpc Connection With Your Core Wallet - put your own ( user + pass + port )
2-click on First script ( only PVKEY ) - you will have New Text File ( Only-private-keys.txt ) in same folder
3-click on second script ( convert ) .

After Step 3 You Will have new Text File ( command_file.txt ) .. 
it has all your privet keys with command to importprivkey without rescan to make it fast 
( importprivkey ****** "" false )
Then when u finish close everything and Reopen your wallet with -rescan=1
"# dumpprivkey-wallet-Core" 
