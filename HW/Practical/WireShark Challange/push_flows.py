import requests
from dijkstraPath import calculatePath
import json

topo = json.load(open('topo.txt'))
n = topo.__len__()
path = calculatePath(initialGraph=topo, source='1', dest=f'{n}')
pathLen = path.__len__()


requests.packages.urllib3.disable_warnings()

HOST = "192.168.1.100"
PORT = "8181"
USER = "admin"
PASSWORD = "admin"
header = {
    'Content-Type': 'application/xml',
    'Accept': 'application/xml',
}

for i in range(1, pathLen):
    switch_id = path[i-1]
    node_id = f"openflow:{switch_id}"
    table_id = 0
    # add two forward and backward flow for each switch with id=1 and 2 respectively
    for j in range(1, 3):
        flow_id = j
        # typical file name:
        if j == 1:
            fileLocation = f'./Flows/switch-{switch_id}-forwardFlow.xml'
        else:
            fileLocation = f'./Flows/switch-{switch_id}-backwardFlow.xml'
        xmlFile = open(fileLocation, 'rb')
        # typical URL: “http://<controller IP>:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/0/flow/1”
        url = f"http://{HOST}:{PORT}/restconf/config/opendaylight-inventory:nodes/node/{node_id}/table/{table_id}/flow/{flow_id}"
        response = requests.put(url=url, data=xmlFile, headers=header, auth=(USER, PASSWORD))
        print(f"Switch: {switch_id}, flow: {flow_id}    {response.status_code}")