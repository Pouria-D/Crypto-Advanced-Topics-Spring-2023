import xml.etree.ElementTree as ET

flows = ['Switch1-OutputFlow', 'Switch1-InputFlow', 'Switch1-ArpFlow',
         'Switch2-OutputFlow', 'Switch2-InputFlow', 'Switch2-ArpFlow',
         'Router-Arp1Flow', 'Router-Arp2Flow', 'Router-IP1Flow', 'Router-IP2Flow']


def addMatchAndActions(index):
    match = ET.SubElement(root, 'match')
    id = ET.SubElement(root, 'id')

    if index == 1 or index == 5 or index == 2 or index == 4:
        # Match:
        ethernetMatch = ET.SubElement(match, 'ethernet-match')
        ethernetDestination = ET.SubElement(ethernetMatch, 'ethernet-destination')
        address = ET.SubElement(ethernetDestination, 'address')
        if index == 1 or index == 5:
            address.text = '00:00:00:00:00:02'
            # flow id
            id.text = '1'
        else:
            address.text = '00:00:00:00:00:01'
            # flow id
            id.text = '2'
        # Action
        action = ET.SubElement(applyActions, 'action')
        actionOrder = ET.SubElement(action, 'order')
        actionOrder.text = '0'
        outputAction = ET.SubElement(action, 'output-action')
        maxLength = ET.SubElement(outputAction, 'max-length')
        maxLength.text = '0'
        outputNodeConnector = ET.SubElement(outputAction, 'output-node-connector')
        if index == 1 or index == 4:
            outputNodeConnector.text = '2'
        else:
            outputNodeConnector.text = '1'

    elif index == 3 or index == 6:
        # Match
        ethernetMatch = ET.SubElement(match, 'ethernet-match')
        etherType = ET.SubElement(ethernetMatch, 'ethernet-type')
        type = ET.SubElement(etherType, 'type')
        type.text = '2048'
        # flow id
        id.text = '3'
        # Action
        action = ET.SubElement(applyActions, 'action')
        actionOrder = ET.SubElement(action, 'order')
        actionOrder.text = '0'
        outputAction = ET.SubElement(action, 'output-action')
        maxLength = ET.SubElement(outputAction, 'max-length')
        maxLength.text = '0'
        outputNodeConnector = ET.SubElement(outputAction, 'output-node-connector')
        outputNodeConnector.text = 'FLOOD'
    elif index == 7 or index == 8:
        ethernetMatch = ET.SubElement(match, 'ethernet-match')
        etherType = ET.SubElement(ethernetMatch, 'ethernet-type')
        type = ET.SubElement(etherType, 'type')
        type.text = '2054'
        arpTargetTransportAddress = ET.SubElement(match, 'arp-target-transport-address')
        if index == 7:
            arpTargetTransportAddress.text = '10.0.1.1/32'
            # flow id
            id.text = '1'
        else:
            arpTargetTransportAddress.text = '10.0.2.1/32'
            # flow id
            id.text = '2'
        # Action
        action = ET.SubElement(applyActions, 'action')
        actionOrder = ET.SubElement(action, 'order')
        actionOrder.text = '0'
        outputAction = ET.SubElement(action, 'output-action')
        maxLength = ET.SubElement(outputAction, 'max-length')
        maxLength.text = '0'
        outputNodeConnector = ET.SubElement(outputAction, 'output-node-connector')
        if index == 7:
            outputNodeConnector.text = '1'
        else:
            outputNodeConnector.text = '2'
    elif index == 9 or index == 10:
        ethernetMatch = ET.SubElement(match, 'ethernet-match')
        etherType = ET.SubElement(ethernetMatch, 'ethernet-type')
        type = ET.SubElement(etherType, 'type')
        type.text = '2048'
        ipv4Destination = ET.SubElement(match, 'ipv4-destination')
        if index == 9:
            ipv4Destination.text = '10.0.1.0/24'
            # flow id
            id.text = '3'
        else:
            ipv4Destination.text = '10.0.2.0/24'
            # flow id
            id.text = '4'
        # Action
        action1 = ET.SubElement(applyActions, 'action')
        actionOrder = ET.SubElement(action1, 'order')
        actionOrder.text = '0'
        decNwTtl = ET.SubElement(action1, 'dec-nw-ttl')
        action2 = ET.SubElement(applyActions, 'action')
        actionOrder = ET.SubElement(action2, 'order')
        actionOrder.text = '1'
        outputAction = ET.SubElement(action2, 'output-action')
        maxLength = ET.SubElement(outputAction, 'max-length')
        maxLength.text = '0'
        outputNodeConnector = ET.SubElement(outputAction, 'output-node-connector')
        if index == 9:
            outputNodeConnector.text = '1'
        else:
            outputNodeConnector.text = '2'


for i in range(1, 11):
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

    addMatchAndActions(i)
    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)
    tree.write(flows[i-1] + '.xml', xml_declaration=True, encoding='utf-8')


