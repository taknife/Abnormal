# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project -> @File : Abnormal -> get_parser.py
# @Author   : Taknife
# @IDE      : PyCharm
# @Time     : 2022/9/29 1:01

"""
-------------------- Function --------------------
Desc: 
---------------------- End -----------------------
"""


import argparse


def show_parser():
    parser = argparse.ArgumentParser(
        add_help=False,
        description="View network card information."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--inter", action="store_true", help="show interface")
    group.add_argument("--route", type=int, choices=[4, 6], help="show route (ipv4/ipv6)")
    args = parser.parse_args()
    inter = args.inter
    route = args.route
    return inter, route


def custom_parser():
    pass


def ipv4_land_base_parser():
    parser = argparse.ArgumentParser(description='Land-Base Exception Packet Attack.')
    parser.add_argument("-m", "--smac", type=str, metavar="[XX:XX:XX:XX:XX:XX]", help="Construct source MAC address.")
    parser.add_argument("-d", "--dst", type=str, metavar="[xxx.xxx.xxx.xxx]", help="Target IP address.")
    parser.add_argument("--hide-mac", action="store_true", help="Hide source MAC address.")
    parser.add_argument("-n", "--num", type=int, metavar="number", help="Number of packets sent.")
    parser.add_argument("-t", "--time", type=int, metavar="second", default=0,
                        help="Time interval between sending request packets.")
    args = parser.parse_args()
    src = args.smac
    dst = args.dst
    num = args.num
    tim = args.time
    return smac, dst, num, tim


def ipv4_tear_drop_parser():
    pass


def module_parser():
    parser = argparse.ArgumentParser(
        prog="abnormal",
        usage=None,
        description="Exception package module:"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--show", action="store_true", help="View network card information.")
    group.add_argument("--ping-of-death", action="store_true", help="Construct ping of death attack packet. (ipv4)")
    group.add_argument("--land-base", action="store_true", help="Construct land base attack packet. (ipv4/ipv6)")
    group.add_argument("--tear-drop", action="store_true", help="Construct tear drop attack packet. (ipv4)")
    group.add_argument("--tcp-flag", action="store_true", help="Construct tcp flag attack packet. (ipv4/ipv6)")
    group.add_argument("--winnuke", action="store_true", help="Construct winnuke attack packet. (ipv4/ipv6)")
    group.add_argument("--smurf", action="store_true", help="Construct smurf attack packet. (ipv4)")
    group.add_argument("--ip-option", action="store_true", help="Construct ip option attack packet. (ipv4)")
    group.add_argument("--ip-spoof", action="store_true", help="Construct ip option attack packet. (ipv4/ipv6)")
    group.add_argument("--jolt2", action="store_true", help="Construct jolt2 attack packet. (ipv4)")
    group.add_argument("--tcp-sack", action="store_true", help="Construct tcp sack attack packet. (ipv4)")
    group.add_argument("--fraggle", action="store_true", help="Construct fraggle attack packet. (ipv6)")
    group.add_argument("--custom", action="store_true", help="Custom Package Structure. (ipv4/ipv6)")
    args = parser.parse_args()
    show = args.show
    pingofdeath = args.ping_of_death
    landbase = args.land_base
    teardrop = args.tear_drop
    tcpflag = args.tcp_flag
    winnuke = args.winnuke
    smurf = args.smurf
    ipoption = args.ip_option
    ipspoof = args.ip_spoof
    jolt2 = args.jolt2
    tcpsack = args.tcp_sack
    fraggle = args.fraggle
    custom = args.custom
    return show, pingofdeath, landbase, teardrop, tcpflag, winnuke, smurf, ipoption, ipspoof, jolt2, tcpsack, fraggle, custom