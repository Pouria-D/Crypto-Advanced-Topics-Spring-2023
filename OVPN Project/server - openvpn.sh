#!/bin/bash

sudo apt install curl
sudo curl -O https://raw.githubusercontent.com/angristan/openvpn-install/master/openvpn-install.sh
sudo chmod +x openvpn-install.sh

echo ""

echo "  --------------------------------------------------------------------------------------"
echo "#											#"
echo "#	Pay attention to the following points when installing OpenVPN:			#"
echo "#											#"
echo "#	1- Both IPs must be the same and equal to the IP that the clients connect to! 	#"
echo "#	2- Port = 443 									#"
echo "#	3- Protocol = TCP 								#"
echo "#	4- IPv6 = n 									#"
echo "#	5- No custom enc 								#"
echo "#	6- Certificateless user 							#"
echo "#	7- At the end, Chose a username for user 					#"
echo "#											#"
echo "  ---------------------------------------------------------------------------------------"



echo ""; echo "If it is ok to continue! Press any key..."
read key
sudo ./openvpn-install.sh

echo ""
echo ""

echo "Your *.ovpn file is in /root"
cd /root/
file_name=$(find . -name "*.ovpn")
echo $file_name

sed -i '1s/^/socks-proxy-retry\n/' $file_name
sed -i '1s/^/socks-proxy 127.0.0.1 10194\n/' $file_name
sed -i "s/443/21194/" $file_name

echo "You can move this *.ovpn to the client"
echo ""

echo "Now we are installing Obfsproxy!"
echo ""

sudo apt-get install obfsproxy
echo ""
echo "Now server is up and ready to use!"
echo ""
obfsproxy obfs3 --dest=127.0.0.1:443 server 0.0.0:21194

