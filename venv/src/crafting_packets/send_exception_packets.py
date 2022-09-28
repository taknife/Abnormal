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

from scapy.all import send


def send_packets(pkt):
    send(pkt)