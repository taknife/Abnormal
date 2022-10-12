# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project -> @File : Abnormal -> show_information.py
# @Author   : Taknife
# @IDE      : PyCharm
# @Time     : 2022/9/29 11:03

"""
-------------------- Function --------------------
Desc: 
---------------------- End -----------------------
"""

from scapy.all import conf, get_if_addr


def show_interface():
    print(conf.ifaces)


def show_route(num):
    if num == 4:
        print(conf.route)
    elif num == 6:
        print(conf.route6)
    else:
        print("Wrong IP protocol version, select IPv4 or IPv6.")
        exit()


def show_ip_address():
    print(get_if_addr(conf.ifaces.dev_from_index(8)))