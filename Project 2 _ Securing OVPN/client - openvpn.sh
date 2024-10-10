#!/bin/bash

sudo apt update
sudo apt install openvpn

echo "  ------------------------------------------------------------------------------------------------------"
echo "#													#"
echo "#	If you have imported the *.ovpn file into the client, continue, otherwise import it first	#"
echo "#													#"
echo "  ------------------------------------------------------------------------------------------------------"

sudo apt-get install obfsproxy
obfsproxy obfs3 socks 127.0.0.1:10194

echo ""; echo "Please input the full address (with name) of *.ovpn file (for exp. /home/client.ovpn):"; read ADDRESS; 

sudo openvpn –config $ADDRESS


