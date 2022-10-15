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


def iface(num):
    return conf.ifaces.dev_from_index(num)


def ipv4_addr(num):
    return get_if_addr(conf.ifaces.dev_from_index(num))


def ipv6_addr(num):
    return get_if_addr6(conf.ifaces.dev_from_index(num))


def mac_addr(num):
    return get_if_hwaddr(conf.ifaces.dev_from_index(num))

