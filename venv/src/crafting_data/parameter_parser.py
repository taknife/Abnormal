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


class ModuleParser():
    __parser = None
    __subparser = None
    __ping_of_death_subparser = None
    __land_base_subparser = None
    __tear_drop_subparser = None
    __tcp_flag_subparser = None
    __winnuke_subparser = None
    __smurf_subparser = None
    __ip_option_subparser = None
    __ip_spoof_subparser = None
    __jolt2_subparser = None
    __tcp_sack_subparser = None
    __fraggle_subparser = None
    __custom_subparser = None


    def __init__(self):
        self.__parser = argparse.ArgumentParser(
            prog="abnormal",
            usage=None,
            # description="Exception package module:"
        )
        self.__subparser = self.__parser.add_subparsers(
            help="Exception package module:",
            dest="module_name"
        )
        self.__ping_of_death_subparser = self.__subparser.add_parser("ping-of-death", help="Construct ping of death attack message.")
        self.__land_base_subparser = self.__subparser.add_parser("land-base", help="Construct land base attack message.")
        self.__tear_drop_subparser = self.__subparser.add_parser("tear-drop", help="Construct tear drop attack message.")
        self.__tcp_flag_subparser = self.__subparser.add_parser("tcp-flag", help="Construct tcp flag attack message.")
        self.__winnuke_subparser = self.__subparser.add_parser("winnuke", help="Construct winnuke attack message.")
        self.__smurf_subparser = self.__subparser.add_parser("smurf", help="Construct smurf attack message.")
        self.__ip_option_subparser = self.__subparser.add_parser("ip-option", help="Construct ip option attack message.")
        self.__ip_spoof_subparser = self.__subparser.add_parser("ip-spoof", help="Construct ip spoof attack message.")
        self.__jolt2_subparser = self.__subparser.add_parser("jolt2", help="Construct jolt2 attack message.")
        self.__tcp_sack_subparser = self.__subparser.add_parser("tcp-sack", help="Construct tcp sack attack message.")
        self.__fraggle_subparser = self.__subparser.add_parser("fraggle", help="Construct fraggle attack message.")
        self.__custom_subparser = self.__subparser.add_parser("custom", help="Customized construction of attack packets.")


    # 解析器，模块构造器，根模块的建立
    def module_parser(self):
        # 主解析器（查看设备网卡信息）
        group = self.__parser.add_mutually_exclusive_group()
        group.add_argument("--inter", action="store_true", help="show interface.")
        group.add_argument("--route", type=int, choices=[4, 6], help="show route ipv4/ipv6.")
        group.add_argument("--version", action="version", version='%(prog)s beta v1.1')
        # group.add_argument("--version", action="version", version='%(prog)s 1.0')

        # ping of death 解析器
        self.ping_of_death_parser()
        # land base 解析器
        self.land_base_parser()
        # tear drop 解析器
        self.tear_drop_parser()
        # tcp flag 解析器
        self.tcp_flag_parser()
        # winnuke 解析器
        self.winnuke_parser()
        # smurf 解析器
        self.smurf_parser()
        # ip option 解析器
        self.ip_option_parser()
        # ip spoof 解析器
        self.ip_spoof_parser()
        # jolt2 解析器
        self.jolt2_parser()
        # tcp sack 解析器
        self.tcp_sack_parser()
        # fraggle 解析器
        self.fraggle_parser()
        # custom 解析器

        args = self.__parser.parse_args()

        return args


    # ping_of_death报文传参方法
    def ping_of_death_parser(self):
        pass


    # land base攻击报文传参方法
    def land_base_parser(self):
        group = self.__land_base_subparser.add_mutually_exclusive_group()
        self.__land_base_subparser.add_argument("-i", "--int", type=int, metavar="index", required=True, help="Network card index value.")
        self.__land_base_subparser.add_argument("-d", "--dst", type=str, metavar="xxx.xxx.xxx.xxx", required=True, help="Target target address.")
        group.add_argument("-m", "--smac", type=str, metavar="XX:XX:XX:XX:XX:XX", help="MAC address of packet sending source.")
        group.add_argument("--hide-srcmac", action="store_true", help="Hide Source MAC Address.")
        self.__land_base_subparser.add_argument("-n", "--num", type=int, metavar="number", help="Number of packets sent.")
        self.__land_base_subparser.add_argument("-t", "--time", type=float, metavar="second", help="Transmission interval between each data packet.")


    # tear drop攻击报文传参方法
    def tear_drop_parser(self):
        group_1 = self.__tear_drop_subparser.add_mutually_exclusive_group()
        group_2 = self.__tear_drop_subparser.add_mutually_exclusive_group()
        self.__tear_drop_subparser.add_argument("-i", "--int", type=int, metavar="index", required=True, help="Network card index value.")
        self.__tear_drop_subparser.add_argument("-d", "--dst", type=str, metavar="xxx.xxx.xxx.xxx", required=True, help="Target target address.")
        group_1.add_argument("-m", "--smac", type=str, metavar="XX:XX:XX:XX:XX:XX", help="MAC address of packet sending source.")
        group_1.add_argument("--hide-srcmac", action="store_true", help="Hide Source MAC Address.")
        group_2.add_argument("-s", "--src", type=str, metavar="xxx.xxx.xxx.xxx", help="Custom source IP address.")
        group_2.add_argument("--hide-srcip", action="store_true", help="Hide Source IP Address.")
        self.__tear_drop_subparser.add_argument("-r", "--frag", type=int, metavar="offset", help="Configure IP partition offset.")
        self.__tear_drop_subparser.add_argument("-p", "--proto", type=int, choices=[1, 6, 17], help="Select upper layer protocol.")
        self.__tear_drop_subparser.add_argument("-a", "--data", type=int, default=1480, metavar="size", help="Select the sending packet size.")
        self.__tear_drop_subparser.add_argument("-n", "--num", type=int, metavar="number", default=1, help="Number of packets sent.")
        self.__tear_drop_subparser.add_argument("-t", "--time", type=float, metavar="second", default=0, help="Transmission interval between each data packet.")


    # tcp flag攻击报文传参方法
    def tcp_flag_parser(self):
        group_1 = self.__tcp_flag_subparser.add_mutually_exclusive_group()
        group_2 = self.__tcp_flag_subparser.add_mutually_exclusive_group()
        self.__tcp_flag_subparser.add_argument("-i", "--int", type=int, metavar="index", required=True, help="Network card index value.")
        self.__tcp_flag_subparser.add_argument("-d", "--dst", type=str, metavar="xxx.xxx.xxx.xxx", required=True, help="Target target address.")
        group_1.add_argument("-m", "--smac", type=str, metavar="XX:XX:XX:XX:XX:XX", help="MAC address of packet sending source.")
        group_1.add_argument("--hide-srcmac", action="store_true", help="Hide Source MAC Address.")
        group_2.add_argument("-s", "--src", type=str, metavar="xxx.xxx.xxx.xxx", help="Custom source IP address.")
        group_2.add_argument("--hide-srcip", action="store_true", help="Hide Source IP Address.")
        self.__tcp_flag_subparser.add_argument("-f", "--flags", choices=["F", "FR", "SU", "SR", "SF"], help="Configure abnormal TCP identification bit.")
        self.__tcp_flag_subparser.add_argument("-n", "--num", type=int, metavar="number", help="Number of packets sent.")
        self.__tcp_flag_subparser.add_argument("-t", "--time", type=float, metavar="second", help="Transmission interval between each data packet.")
        # self.__tcp_flag_subparser.add_argument()


    # winnuke攻击报文传参方法
    def winnuke_parser(self):
        group_1 = self.__winnuke_subparser.add_mutually_exclusive_group()
        group_2 = self.__winnuke_subparser.add_mutually_exclusive_group()
        self.__winnuke_subparser.add_argument("-i", "--int", type=int, metavar="index", required=True, help="Network card index value.")
        self.__winnuke_subparser.add_argument("-d", "--dst", type=str, metavar="xxx.xxx.xxx.xxx", required=True, help="Target target address.")
        group_1.add_argument("-m", "--smac", type=str, metavar="XX:XX:XX:XX:XX:XX", help="MAC address of packet sending source.")
        group_1.add_argument("--hide-srcmac", action="store_true", help="Hide Source MAC Address.")
        group_2.add_argument("-s", "--src", type=str, metavar="xxx.xxx.xxx.xxx", help="Custom source IP address.")
        group_2.add_argument("--hide-srcip", action="store_true", help="Hide Source IP Address.")
        self.__winnuke_subparser.add_argument("-n", "--num", type=int, metavar="number", help="Number of packets sent.")
        self.__winnuke_subparser.add_argument("-t", "--time", type=float, metavar="second", help="Transmission interval between each data packet.")


    # smurf攻击报文传参方法
    def smurf_parser(self):
        self.__smurf_subparser.add_argument("-i", "--int", type=int, metavar="index", required=True, help="Network card index value.")
        self.__smurf_subparser.add_argument("-d", "--dst", type=str, metavar="xxx.xxx.xxx.xxx[/xx]", required=True, help="Target target address. (Mask default 24)")
        self.__smurf_subparser.add_argument("-n", "--num", type=int, metavar="number", help="Number of packets sent.")
        self.__smurf_subparser.add_argument("-t", "--time", type=float, metavar="second", help="Transmission interval between each data packet.")


    # ip-option攻击报文传参方法
    def ip_option_parser(self):
        pass


    # ip_spoof攻击报文传参方法
    def ip_spoof_parser(self):
        pass


    # jolt2攻击报文传参方法
    def jolt2_parser(self):
        pass


    # tcp sack攻击报文传参方法
    def tcp_sack_parser(self):
        pass


    # fraggle攻击报文传参方法
    def fraggle_parser(self):
        pass


    # 自定义构造攻击数据包
    def custom_parser(self):
        pass