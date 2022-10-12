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


class moduleParser():
    __key = None
    __parser = None
    __subparser = None
    __land_base_subparser = None

    def __init__(self):
        self.__parser = argparse.ArgumentParser(
            prog="abnormal",
            usage=None,
            # description="Exception package module:"
        )
        self.__subparser = self.__parser.add_subparsers(
            help="Exception package module:"
        )
        self.__land_base_subparser = self.__subparser.add_parser("land-base", help="Construct land base attack message.")


    # 解析器，模块构造器，根模块的建立
    def module_parser(self):
        # 主解析器（查看设备网卡信息）
        group = self.__parser.add_mutually_exclusive_group()
        group.add_argument("--inter", action="store_true", help="Show interface.")
        group.add_argument("--route", type=int, choices=[4, 6], help="Show route ipv4/ipv6.")

        # 构造land base攻击报文
        self.land_base_parser()

        args = self.__parser.parse_args()
        return args

    def land_base_parser(self):
        self.__key = "land-base"
        self.__land_base_subparser.add_argument("-d", "--dst", type=str, metavar="xxx.xxx.xxx.xxx", help="Target target address.")
        self.__land_base_subparser.add_argument("-n", "--num", type=int, metavar="10", help="Number of packets sent.")
        self.__land_base_subparser.add_argument("-t", "--time", type=int, metavar="1", help="Transmission interval between each data packet.")