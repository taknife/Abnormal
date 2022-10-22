# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project -> @File : Abnormal -> send_exception_packets.py
# @Author   : Taknife
# @IDE      : PyCharm
# @Time     : 2022/9/28 15:14

"""
-------------------- Function --------------------
Desc: 
---------------------- End -----------------------
"""

from scapy.all import send, sendp


# 循环发送带数据链路层的报文（循环次数自定义）
def loop_packets(pkt, tim, num, net):
    if tim:
        sendp(pkt, inter=tim, count=num, iface=net)
    else:
        sendp(pkt, inter=0, count=num, iface=net)


# 循环发送带数据链路层的报文（循环次数默认100000次，伪死循环）
def infinite_packets(pkt, tim, net):
    if tim:
        sendp(pkt, inter=tim, count=100000, iface=net)
    else:
        sendp(pkt, inter=0, count=100000, iface=net)


def tear_drop_send(pkt1, pkt2, num, net, tim):
    if tim:
        if not num:
            while True:
                sendp(pkt1, inter=tim, count=1, iface=net)
                sendp(pkt2, inter=tim, count=1, iface=net)
        else:
            for i in range(num):
                sendp(pkt1, inter=tim, count=1, iface=net)
                sendp(pkt2, inter=tim, count=1, iface=net)
    else:
        tim = 0
        if not num:
            while True:
                sendp(pkt1, inter=tim, count=1, iface=net)
                sendp(pkt2, inter=tim, count=1, iface=net)
        else:
            for i in range(num):
                sendp(pkt1, inter=tim, count=1, iface=net)
                sendp(pkt2, inter=tim, count=1, iface=net)


def ping_of_death_send(pkt, tim, net):
    sendp(pkt, inter=tim, count=1, iface=net)