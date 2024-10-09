import requests
import xmltodict
from rich import print as rprint

requests.packages.urllib3.disable_warnings()

HOST = "192.168.1.100"
PORT = "8181"
USER = "admin"
PASSWORD = "admin"
header = {
  'Content-Type': 'application/xml',
  'Accept': 'application/xml',
}
# add flows for s1 and s2:
for i in range(1, 3):
    node_id = "openflow:" + str(i)
    table_id = 0
    # add simple switch (port and mac) flows for each s1 and s2
    for j in range(1, 3):
        flow_id = j
        # URL: “http://<controller IP>:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/0/flow/1”
        url = f"https://{HOST}:{PORT}/restconf/config/opendaylight-inventory:nodes/node/{node_id}/table/{table_id}/flow/{flow_id}"
        response = requests.put(url=url, headers=header, auth=(USER, PASSWORD), verify=False)
