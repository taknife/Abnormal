# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project -> @File : Abnormal -> crafting_addr.py
# @Author   : Taknife
# @IDE      : PyCharm
# @Time     : 2022/9/29 0:54

"""
-------------------- Function --------------------
Desc: 
---------------------- End -----------------------
"""

from scapy.all import get_if_addr, get_if_addr6, get_if_hwaddr, conf
import random


def iface(index):
    return conf.ifaces.dev_from_index(index)


def ipv4_addr(index):
    return get_if_addr(conf.ifaces.dev_from_index(index))


def ipv6_addr(index):
    return get_if_addr6(conf.ifaces.dev_from_index(index))


def mac_addr(index):
    return get_if_hwaddr(conf.ifaces.dev_from_index(index))


def random_srcip():
    paragraph_1 = random.randint(1, 254)
    paragraph_2 = random.randint(1, 254)
    paragraph_3 = random.randint(1, 254)
    paragraph_4 = random.randint(1, 254)
    src_ip = str(paragraph_1) + '.' + str(paragraph_2) + '.' + str(paragraph_3) + '.' + str(paragraph_4)
    return src_ip


def random_srcmac():
    paragraph_1 = hex(random.randint(1, 254))[2:]
    paragraph_2 = hex(random.randint(1, 254))[2:]
    paragraph_3 = hex(random.randint(1, 254))[2:]
    paragraph_4 = hex(random.randint(1, 254))[2:]
    paragraph_5 = hex(random.randint(1, 254))[2:]
    paragraph_6 = hex(random.randint(1, 254))[2:]
    src_mac = str(paragraph_1) + ':' + str(paragraph_2) + ':' + str(paragraph_3) + ':' + str(paragraph_4) + ':' + str(paragraph_5) + ':' + str(paragraph_6)
    return src_mac


# 根据IP与子网掩码构造广播
def ip_broadcast(network_bit, host_bit="24"):
    paragraph_list = network_bit.split('.', 4)
    paragraph_bin = ""
    mask_bin = ""
    for i in paragraph_list:
        paragraph_bin += "{:0>8d}".format(int(bin(int(i))[2:]))

    for j in range(32 - int(host_bit)):
        mask_bin += "1"
    mask_bin = "{:0>32d}".format(int(mask_bin))

    broadcast_bin = bin(int(paragraph_bin, base=2) | int(mask_bin, base=2))[2:]

    broadcast_list = []
    paragraph_bro = ""
    counter = 1
    for k in broadcast_bin:
        paragraph_bro += k
        if counter % 8 == 0:
            broadcast_list.append(paragraph_bro)
            paragraph_bro = ""
        counter += 1

    for l in range(len(broadcast_list)):
        broadcast_list[l] = str(int(broadcast_list[l], base=2))

    connector = "."
    broadcast = connector.join(broadcast_list)
    return broadcast