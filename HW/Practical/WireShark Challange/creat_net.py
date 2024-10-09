# from mininet.net import Mininet
# from mininet.node import RemoteController, OVSKernelSwitch
# from mininet.cli import CLI
# from mininet.log import setLogLevel
# from mininet.link import TCLink
from dijkstraPath import calculatePath
import json
#setLogLevel('info')


def initial_graph():

    topo = {
        '1': {'2': 2, '3': 3, '4': 4},
        '2': {'1': 2, '4': 1},
        '3': {'1': 3},
        '4': {'1': 1, '2': 1}
    }
    json.dump(topo, open("topo.txt", 'w'))
    return topo


# input graph:
topo = initial_graph()
n = topo.__len__()

"""
n = 6
edges = [
    (1, 2, {"weight": 4}),
    (1, 3, {"weight": 2}),
    (2, 3, {"weight": 1}),
    (2, 4, {"weight": 5}),
    (3, 4, {"weight": 8}),
    (3, 5, {"weight": 10}),
    (4, 5, {"weight": 2}),
    (4, 6, {"weight": 8}),
    (5, 6, {"weight": 5}),
]
"""

net = Mininet(controller=RemoteController,
              switch=OVSKernelSwitch,
              link=TCLink
              )

# Adding hosts

h1 = net.addHost(
    name="h1",
    ip="10.0.1.1/24",
    mac="00:00:00:00:00:01",
    defaultRoute="h1-eth0"
)
h2 = net.addHost(
    name="h2",
    ip="10.0.2.1/24",
    mac="00:00:00:00:00:02",
    defaultRoute="h2-eth0"
)

# Adding switches
s = []
for i in range(1, n+1):
    s.append(
        net.addSwitch(
            name=f"s{i}"
        )
    )

# Adding controller (if any!)
c0 = net.addController(
    name="c0",
    ip="192.168.1.100",  # static ip defined in vm
    port=6633,
    protocols="OpenFlow13"
)

# Adding links
net.addLink(h1, s[0], 0, n+1)
net.addLink(h2, s[n-1], 0, n+1)
for src in topo:
    for dst in topo[src].keys():
        s_port1 = int(dst)
        s_port2 = int(src)
        if src < dst:
            net.addLink(s[int(src)-1], s[int(dst)-1], s_port1, s_port2)
# for link in edges:
#     node1 = link[0]
#     node2 = link[1]
#     if node1 < node2:
#         s_port1 = node2
#         s_port2 = node1
#         net.addLink(s[node1-1], s[node2-1], s_port1, s_port2)
#         # print(f'Switch{node1} to switch {node2} port1 = {s_port1} port2 = {s_port2}')

# Start controller on switches (if any!)
c0.start()
for i in range(0, n):
    s[i].start([c0])

# Start CLI and build the network

net.build()
net.start()
CLI(net)
net.stop()
