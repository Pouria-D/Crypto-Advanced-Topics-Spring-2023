import xml.etree.ElementTree as ET
from dijkstraPath import calculatePath
import json

topo = json.load(open('topo.txt'))
n = topo.__len__()
path = calculatePath(initialGraph=topo, source='1', dest=f'{n}')
pathLen = path.__len__()


def addRouteFlow(switch_index, direction):
    id = ET.SubElement(root, 'id')
    id.text = f'{direction}'
    # Match
    match = ET.SubElement(root, 'match')
    in_port = ET.SubElement(match, 'in-port')
    if direction == 1:
        in_port.text = f'{path[switch_index-1]}'
    else:
        in_port.text = f'{path[switch_index+1]}'
    # Action
    action = ET.SubElement(applyActions, 'action')
    actionOrder = ET.SubElement(action, 'order')
    actionOrder.text = '0'
    outputAction = ET.SubElement(action, 'output-action')
    maxLength = ET.SubElement(outputAction, 'max-length')
    maxLength.text = '0'
    outputNodeConnector = ET.SubElement(outputAction, 'output-node-connector')
    if direction == 1:
        outputNodeConnector.text = f'{path[switch_index +1]}'
    else:
        outputNodeConnector.text = f'{path[switch_index-1]}'

    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)
    location = ""
    if direction == 1:
        # Typical name: switch-i-forwardFlow.xml
        location = f'./Flows/switch-{path[switch_index]}-forwardFlow.xml'
    else:
        # Typical name: switch-i-backwardFlow.xml
        location = f'./Flows/switch-{path[switch_index]}-backwardFlow.xml'
    tree.write(location, xml_declaration=True, encoding='utf-8')


def initialFlows(switch_index, direction):
    # for each switch add a go and a back flow; id=1 for go and id=2 for back
    match = ET.SubElement(root, 'match')
    id = ET.SubElement(root, 'id')
    id.text = f'{direction}'
    ethernetMatch = ET.SubElement(match, 'ethernet-match')
    etherType = ET.SubElement(ethernetMatch, 'ethernet-type')
    type = ET.SubElement(etherType, 'type')
    type.text = '2048'
    ipv4Destination = ET.SubElement(match, 'ipv4-destination')
    if direction == 1:
        ipv4Destination.text = '10.0.2.0/24'
    else:
        ipv4Destination.text = '10.0.1.0/24'
    # Action
    action0 = ET.SubElement(applyActions, 'action')
    actionOrder = ET.SubElement(action0, 'order')
    actionOrder.text = '0'
    decNwTtl = ET.SubElement(action0, 'dec-nw-ttl')

    action1 = ET.SubElement(applyActions, 'action')
    actionOrder = ET.SubElement(action1, 'order')
    actionOrder.text = '1'
    set_field = ET.SubElement(action1, 'set-field')
    ethernet_match = ET.SubElement(set_field, 'ethernet-match')
    ethernet_destination = ET.SubElement(ethernet_match, 'ethernet-destination')
    address = ET.SubElement(ethernet_destination, 'address')
    if direction == 1:
        address.text = '00:00:00:00:00:02'
    else:
        address.text = '00:00:00:00:00:01'

    action2 = ET.SubElement(applyActions, 'action')
    actionOrder = ET.SubElement(action2, 'order')
    actionOrder.text = '2'
    set_field = ET.SubElement(action2, 'set-field')
    ethernet_match = ET.SubElement(set_field, 'ethernet-match')
    ethernet_source = ET.SubElement(ethernet_match, 'ethernet-source')
    address = ET.SubElement(ethernet_source, 'address')
    if direction == 1:
        address.text = '00:00:00:00:00:03'
    else:
        address.text = '00:00:00:00:00:04'

    action3 = ET.SubElement(applyActions, 'action')
    actionOrder = ET.SubElement(action3, 'order')
    actionOrder.text = '3'
    outputAction = ET.SubElement(action3, 'output-action')
    maxLength = ET.SubElement(outputAction, 'max-length')
    maxLength.text = '0'
    outputNodeConnector = ET.SubElement(outputAction, 'output-node-connector')
    if direction == 1:
        if switch_index == 0:
            outputNodeConnector.text = f'{path[switch_index + 1]}'
        else:
            outputNodeConnector.text = f'{n+1}'
    else:
        if switch_index == 0:
            outputNodeConnector.text = f'{n+1}'
        else:
            outputNodeConnector.text = f'{path[switch_index - 1]}'

    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)
    location = ""
    if direction == 1:
        # Typical name: switch-i-forwardFlow.xml
        location = f'./Flows/switch-{path[switch_index]}-forwardFlow.xml'
    else:
        # Typical name: switch-i-backwardFlow.xml
        location = f'./Flows/switch-{path[switch_index]}-backwardFlow.xml'
    tree.write(location, xml_declaration=True, encoding='utf-8')


def buildStructure():
    root = ET.Element('flow', {'xmlns': 'urn:opendaylight:flow:inventory'})
    priority = ET.SubElement(root, 'priority')
    priority.text = '32768'
    flowName = ET.SubElement(root, 'flow-name')
    flowName.text = 'ManualFlow'

    table_id = ET.SubElement(root, 'table_id')
    table_id.text = '0'
    instructions = ET.SubElement(root, 'instructions')
    instruction = ET.SubElement(instructions, 'instruction')
    instructionOrder = ET.SubElement(instruction, 'order')
    instructionOrder.text = '0'
    applyActions = ET.SubElement(instruction, 'apply-actions')
    return [root, applyActions]


for i in range(0, pathLen):
    # [root, applyActions] = buildStructure()
    # for each switch add a forward and a backward flow with id=1 and id=2 respectively
    for j in range(1, 3):
        root = ET.Element('flow', {'xmlns': 'urn:opendaylight:flow:inventory'})
        priority = ET.SubElement(root, 'priority')
        priority.text = '32768'
        flowName = ET.SubElement(root, 'flow-name')
        flowName.text = 'ManualFlow'

        table_id = ET.SubElement(root, 'table_id')
        table_id.text = '0'
        instructions = ET.SubElement(root, 'instructions')
        instruction = ET.SubElement(instructions, 'instruction')
        instructionOrder = ET.SubElement(instruction, 'order')
        instructionOrder.text = '0'
        applyActions = ET.SubElement(instruction, 'apply-actions')

        if i == 0:
            initialFlows(switch_index=0, direction=j)
        elif i == pathLen-1:
            initialFlows(switch_index=pathLen - 1, direction=j)
        else:
            addRouteFlow(switch_index=i, direction=j)


