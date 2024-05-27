import sys
import datetime
import sys,os,re
import time, datetime , pprint,collections
import json
import pandas as pd
from ixnetwork_restpy import *
from itertools import islice, product
#C:\Users\kavyvall\tutorial-env\Cafy
sys.path.append('C:\\tutorial-env\Cafy')
from ixia_latest import IXIA
#apiServerIp  = "10.39.71.219"
apiServerIp = '127.0.0.1'

#tgnObj = IXIA(tgn_server_type='linux', server_ip=apiServerIp)
#tgnObj.connect_to_session(sid='testbed_srsettur')
tgnObj = IXIA(server_ip=apiServerIp)
tgnObj.connect_to_session()


def test_set_vlan():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.set_device_vlan_count(device_name='IPv4 Device Group 1', vlan_count=2)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_set_device_vlan():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.set_vlan(device_name='IPv4 Device Group 1'  ,vlan_id = 20,enable_vlan =True )
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)


def test_get_port_traffic_streams():
    start = datetime.datetime.now()
    print("start_time:", start)
    traffic_item_name=tgnObj.get_port_traffic_streams('Ethernet - 003')
    print(traffic_item_name)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    """ 
    output:
    Getting Traffic Streams based on Port
     ['Traffic Item 1']
    True
    """

def test_get_all_traffic_streams():
    start = datetime.datetime.now()
    print("start_time:", start)
    traffic_items=tgnObj.get_all_traffic_streams(getEnabledTrafficItemsOnly=True)
    print(traffic_items)
    for traffic_item in traffic_items:
        print(traffic_item.Name)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_new_blank_config():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.new_blank_config()
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_get_ipv4_tos_information():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.get_ipv4_tos_information()
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    #Get IPv4 Type of Service (ToS) configuration for a given traffic stream
    #traffic item should have ipv4 header

def test_change_ipv4_tos():
    start = datetime.datetime.now()
    print("start: ",start)
    ipv4_tos = tgnObj.change_ipv4_tos(traffic_item_list=["Traffic Item 1"],cfg_dict={'valueType':'increment','fieldValue':'001 Priority'})
    # tgnObj.change_ipv4_tos(traffic_item_list=["Traffic Item 1"],cfg_dict={'valueType':'increment','fieldValue':'000 Routine','startValue':'2','stepValue':'1','countValue':'15'})
    print(ipv4_tos)
    end = datetime.datetime.now()
    print("end: ",end)
    print("Time duration for API execution ",end - start)

def test_change_ipv6_traffic_class_single():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.change_ipv6_traffic_class(traffic_item_list=["Traffic Item 3"],cfg_dict={'valueType':'singleValue','singleValue':'10'})
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_change_ipv6_traffic_class_list():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.change_ipv6_traffic_class(cfg_dict={'valueType':'valueList','valueList':[10,12,14,15]})
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_change_traffic_frame_size_1():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.change_traffic_frame_size(cfg_dict={'type': 'fixed', 'fixedSize': '140'},traffic_item_list=['Traffic Item 2'])
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_change_traffic_frame_size_2():
    start = datetime.datetime.now()
    print("start: ",start)
    traffic_frame = tgnObj.change_traffic_frame_size(cfg_dict={'type': 'auto'},traffic_item_list=['Traffic Item 2'])
    print(traffic_frame)
    end = datetime.datetime.now()
    print("end: ",end)
    print("time duration for API execution ",end - start)

def test_config_multicast_group():
    start = datetime.datetime.now()
    print("start: ",start)
    multicast_group = tgnObj.config_multicast_group('ipv4',group_name='IPv4 Device Group 1',start_ip='200.1.0.0', count='13',mld_version='version1')
    print(multicast_group)
    end = datetime.datetime.now()
    print("end: ",end)
    print("time duration for API execution ",end - start)

def test_config_multicast_group():
    start = datetime.datetime.now()
    print("start: ",start)
    multicast_group = tgnObj.config_multicast_group('ipv4',group_name='IPv4 Device Group 1',start_ip='200.1.0.0', count='13',mld_version='version1')
    print(multicast_group)
    end = datetime.datetime.now()
    print("end: ",end)
    print("time duration for API execution ",end - start)

def test_change_traffic_mac():
    start = datetime.datetime.now()
    print("start: ",start)
    traffic_mac = tgnObj.change_traffic_mac(traffic_item_name='Traffic Item 1',endpoint_name='EndpointSet-1',mac_dst='00:00:00:00:00:05',mac_src='00:00:00:00:00:03')
    print(traffic_mac)
    end = datetime.datetime.now()
    print("end: ",end)
    print("Time duration for API execution ",end - start)

def test_get_port_mtu():
    start = datetime.datetime.now()
    print("start : ",start)
    port_mtu = tgnObj.get_port_mtu('10.39.65.156/2/15')
    print(port_mtu)
    end =  datetime.datetime.now()
    print("end : ",end)
    print("Time duration for API execution: ",end - start)

def test_set_port_mtu():
    start = datetime.datetime.now()
    print("start: ",start)
    set_port = tgnObj.set_port_mtu('10.39.65.156/2/15',1300,direction='increment',step=2)
    print(set_port)
    end = datetime.datetime.now()
    print("end: ",end)
    print("Time duration for API execution ",end - start)

def test_get_traffic_mpls_exp_bits():
    start = datetime.datetime.now()
    print("start_time:", start)
    exp_bit=tgnObj.get_traffic_mpls_exp_bits(traffic_item_list=['Traffic Item 1'])
    print(exp_bit)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_set_traffic_mpls_exp_bits():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.set_traffic_mpls_exp_bits(exp_value = 4, traffic_item_list=["Traffic Item 2"])
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_set_traffic_mpls_exp_bits_all():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.set_traffic_mpls_exp_bits(exp_value = 4)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_set_stream_mpls_label_all():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.set_stream_mpls_label(cfg_dict = {'valueType':'singleValue', 'value' : 20})
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_set_stream_mpls_label_trafficitem():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.set_stream_mpls_label(cfg_dict = {'valueType':'increment', 'value' : 40, 'mpls_label_index': 1 }, traffic_item_list= ['Traffic Item 1','Traffic Item 2'])
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_get_stream_mpls_label():
    start = datetime.datetime.now()
    print("start_time:", start)
    mpls_label=tgnObj.get_stream_mpls_label(traffic_item_list= ['Traffic Item 3'])
    print(mpls_label)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_set_stream_frame():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.set_stream_frame('Traffic Item 2', {'ipv6':{'dst_ip':{'value': '10:0:1:2::20',
                'step': '1::1:0:0:1', 'count': '100','valueType': 'increment'}}})
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    
def test_get_ipv6_traffic_class_information():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.get_ipv6_traffic_class_information()
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    #Get IPv6 Traffic Class (TC) configuration for a given traffic stream
    #traffic item should have ipv6 header
    

def test_get_link_status():
    start = datetime.datetime.now()
    print("start_time:", start)
    port_list = tgnObj.get_link_status()
    print(port_list)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_get_traffic_items():
    start = datetime.datetime.now()
    print("start_time:", start)
    port_list = tgnObj.get_traffic_items()
    print(port_list)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_get_sessions():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.get_sessions()
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    #Get Sessions is Not Supported on Ixia Windows Lab Server

def test_get_frame_l4_information():
    start = datetime.datetime.now()
    print("start_time:", start)
    get_frame = tgnObj.get_frame_l4_information()
    print(get_frame)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    """output:
     Checking L4 Information is Available in TrafficItem
     Stream with L4 Header:['Traffic Item 1']
     True"""

def test_get_list_ports():
    start = datetime.datetime.now()
    print("start_time:", start)
    port_list=tgnObj.get_list_ports()
    print(port_list)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_get_port_name_from_location():
    start = datetime.datetime.now()
    print("start_time:", start)
    port_name=tgnObj.get_port_name_from_location("10.39.65.156/2/11")
    print(port_name)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    """
    output:
     Getting Port Name from Location
    Ethernet - 003"""

def test_get_list_port_name():
    start = datetime.datetime.now()
    print("start_time:", start)
    
    
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    """
    output:
    vport name list
    ['Ethernet - 003', 'Ethernet - 004', 'Ethernet - 005']
    """

def test_get_active_streams():
    start = datetime.datetime.now()
    print("start_time:", start)
    traffic_items=tgnObj.get_active_streams()
    print(traffic_items)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_get_traffic_items():
    start = datetime.datetime.now()
    print("start_time:", start)
    traffic_items=tgnObj.get_traffic_items()
    print(traffic_items)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_get_device_names():
    start = datetime.datetime.now()
    print("start_time:", start)
    device_names=tgnObj.get_device_names()
    print(device_names)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_get_router_ids():
    start = datetime.datetime.now()
    print("start_time:", start)
    router_ids=tgnObj.get_router_ids(device_list=['IPv4 Device Group 1','IPv4 Device Group 2'])
    print(router_ids)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_change_traffic_transmission_mode():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.change_traffic_transmission_mode(config={'type': 'custom', 'interBurstGap': 25, 'burstPacketCount': 25},traffic_item_list=["Traffic Item 1"])
    #tgnObj.change_traffic_transmission_mode(config={'type': 'auto', 'interBurstGap': 34, 'interBurstGapUnits':'miliseconds'},traffic_item_list=["Traffic Item 1"])
    #rate = tgnObj.change_traffic_transmission_mode(config={'type': 'fixedFrameCount', 'startDelay': 15, 'startDelayUnits':'seconds'},traffic_item_list=["Traffic Item 1"])
    
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)


def test_regenerate_traffic():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.regenerate_traffic()
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_start_traffic():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.start_traffic()
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_stop_traffic():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.stop_traffic()
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_get_device_ip_info():
    start = datetime.datetime.now()
    print("start_time:", start)
    ip_address=tgnObj.get_device_ip_info("100.0.0.1", ip_version='ipv4', key='Address')
    print(ip_address)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_enable_traffic_item():
    start = datetime.datetime.now()
    print("start_time:", start)
    transmission_mode=tgnObj.enable_traffic_item(traffic_item_list='Traffic Item 1')
    print(transmission_mode)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_enable_traffic_item_list():
    start = datetime.datetime.now()
    print("start_time:", start)
    transmission_mode=tgnObj.enable_traffic_item(traffic_item_list=['Traffic Item 1','Traffic Item 2'])
    print(transmission_mode)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_disable_traffic_item():
    start = datetime.datetime.now()
    print("start_time:", start)
    transmission_mode=tgnObj.disable_traffic_item(traffic_item_list=['Traffic Item 1','Traffic Item 2'])
    print(transmission_mode)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_start_all_protocols():
    start = datetime.datetime.now()
    print("start_time:", start)
    start_protocols=tgnObj.start_all_protocols()
    print(start_protocols)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    """
    OUTPUT:
    Starting all Protocols
    True"""

def test_stop_all_protocols():
    start = datetime.datetime.now()
    print("start_time:", start)
    start_protocols=tgnObj.stop_all_protocols()
    print(start_protocols)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    """
    OUTPUT:
    stopping all Protocols
    True"""

def test_verify_arp_status():
    start = datetime.datetime.now()
    print("start_time:", start)
    verify_arp=tgnObj.verify_arp_status()
    print(verify_arp)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    """
    OUTPUT:
    Verification of Arp Started
    Arp Verification Successful
    True"""

def test_start_arp_on_devices():
    start = datetime.datetime.now()
    print("start_time:", start)
    start_arp=tgnObj.start_arp_on_devices()
    print(start_arp)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    """
    OUTPUT:even the protocol is not running its returning true. but in API server pointed errors i.e., error in sending ARP for IPV4
    True"""

def test_start_arp_and_verify():
    start = datetime.datetime.now()
    print("start_time:", start)
    verify_arp=tgnObj.start_arp_and_verify()
    print(verify_arp)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_get_traffic_transmission_mode():
    start = datetime.datetime.now()
    print("start_time:", start)
    transmission_mode=tgnObj.get_traffic_transmission_mode(traffic_item_list=['Traffic Item 1','Traffic Item 2'])
    print(transmission_mode)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_set_device_count():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.set_device_count(device_count = 25,device_name='IPv4 Device Group 1')
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_clear_traffic_stats():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.clear_traffic_stats()
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_send_ping():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.send_ping(src_ip_address='100.1.0.1',dest_ip_address='100.1.0.11')
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_enable_ping():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.enable_ping()
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_ospf_start():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.ospf_start(port=['Ethernet - 003','Ethernet - 004'],host_ip=['1.1.1.1','1.1.1.2'])
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_ospf_stop():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.ospf_stop(port=['Ethernet - 003','Ethernet - 004'],host_ip=['1.1.1.1','1.1.1.2'])
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_set_device_count():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.set_device_count(device_count = 5,device_name='IPv4 Device Group 1')
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_set_ospf_route_count():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.set_ospf_route_count(route_count=30,network_group="Network Group 1",ip_type='ipv4',router_id='192.0.0.1')
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_get_ospf_route_count():
    start = datetime.datetime.now()
    print("start_time:", start)
    ospf_count=tgnObj.get_ospf_route_count(network_group="Network Group 1",ip_type='ipv4',router_id='192.0.0.1')
    print(ospf_count)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)


def test_get_ospf_router_status():
    start = datetime.datetime.now()
    print("start_time:", start)
    ospf_count=tgnObj.get_ospf_router_status(['192.0.0.1','193.0.0.1'])
    print(ospf_count)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_verify_dhcp_client_bind():
    start = datetime.datetime.now()
    print("start_time:", start)
    dhcp_client_bind = tgnObj.verify_dhcp_client_bind(device="DHCPv4 Client Device Group 1",protocol = "ipv4")
    print(dhcp_client_bind)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    """OUTPUT:
    Idle and Bound items of deviceGroup while dhcp client protocol is runnig
    """

def test_create_ipv4_interface():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.create_ipv4_interface(router_id='192.0.0.1',ipv4_address='100.10.1.1',
                              ipv4_gateway='10.10.1.2', ipv4_gateway_mac='00:00:01:00:00:01',
                              ipv4_prefix_length='24')
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)


def test_igmp_start():
    start = datetime.datetime.now()
    print("start_time:", start)
    igmp_start = tgnObj.igmp_start(port=['10.39.65.156/2/15', '10.39.65.156/2/16'])
    print(igmp_start)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_igmp_stop():
    start = datetime.datetime.now()
    print("start_time:", start)
    igmp_stop = tgnObj.igmp_stop(port=['10.39.65.156/2/15', '10.39.65.156/2/16'])
    print(igmp_stop)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_get_igmp_group_member():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.get_igmp_group_member('192.0.0.1',device_name='IPv4 Device Group 1')
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)


def test_config_igmp_group_member():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.config_igmp_group_member(router_id="192.0.0.1",mcast_group_config={'count':'3'},mcast_source_config={'count':'2'},device_name ='IPv4 Device Group 1')
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_change_igmp_source_list():
    start = datetime.datetime.now()
    print("start_time:", start)
    igmp_src = tgnObj.change_igmp_source_list(device_list=['IPv4 Device Group 1'],igmp_source_list=['12.10.10.1'], port_list=['Ethernet - 001'])
    print(igmp_src)
    #tgnObj.change_igmp_source_list(device_list=['IPv4 Device Group 1','IPv4 Device Group 2'],igmp_source_list=['12.10.10.1','12.10.10.2','12.10.10.3','12.10.10.4','12.10.10.5'], port_list=['Ethernet - 001','Ethernet - 002'])
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)


def test_bgp_start():
    start = datetime.datetime.now()
    print("start_time:", start)
    bgp_start = tgnObj.bgp_start()
    print(bgp_start)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_bgp_stop():
    start = datetime.datetime.now()
    print("start_time:", start)
    bgp_stop = tgnObj.bgp_stop()
    print(bgp_stop)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_bgp_ngp_flap():
    start = datetime.datetime.now()
    print("start_time:", start)
    bgp_start = tgnObj.bgp_ngp_flap(bgp_peer_name_list=["BGP Peer 1","BGP Peer 2"],action='False')
    #bgp = tgnObj.bgp_ngp_flap(bgp_peer_name_list=["BGP Peer 1","BGP Peer 2"],up_time_in_sec=6, down_time_in_sec=1)
    print(bgp_start)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    """BGP protocol state flapping fime (it will change bgp state from up and down)"""

def test_set_bgp_route_count_all():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.set_bgp_route_count_all(route_count=30, ip_type="ipv4")
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_set_bgp_route_count():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.set_bgp_route_count(route_count=20, ports=["Ethernet - 001"],network_group="Network Group 5",prefix_step=3)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    #verify under ipv4 address pools in network topology

def test_activate_devices():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.activate_devices(device_list=['IPv4 Device Group 1'])
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_deactivate_devices():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.deactivate_devices(device_list=['Device Group 5','IPv4 Device Group 1','IPv4 Device Group 2'])
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_delete_traffic_items():
    start = datetime.datetime.now()
    print("start_time:", start)
    del_traffic = tgnObj.delete_traffic_items(traffic_item_list=['Traffic Item 3','Traffic Item 2'])
    print(del_traffic)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_pim_start():
    start = datetime.datetime.now()
    print("start_time:", start)
    pim_start = tgnObj.pim_start(port=["Ethernet - 001","Ethernet - 002"],mode="sm")
    print(pim_start)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_pim_stop():
    start = datetime.datetime.now()
    print("start_time:", start)
    pim_stop = tgnObj.pim_stop()
    print(pim_stop)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_get_card_type():
    start = datetime.datetime.now()
    print("start_time:", start)
    card_type = tgnObj.get_card_type("10.39.65.156/2/15")
    print(card_type)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)


def test_change_port_transmit_mode():
    start = datetime.datetime.now()
    print("start_time:", start)
    port_mode = tgnObj.change_port_transmit_mode(port='10.39.65.156/2/15', transmit_mode='sequential')
    #port_mode = tgnObj.change_port_transmit_mode(port=['10.39.65.156/2/16'], transmit_mode='interleaved')
    print(port_mode)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    
def test_duplicate_traffic_item():
    start = datetime.datetime.now()
    print("start_time:", start)
    duplicate_traffic = tgnObj.duplicate_traffic_item(traffic_item=['Traffic Item 2'],count=1)
    print(duplicate_traffic)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_enable_network_group():
    start = datetime.datetime.now()
    print("start_time:", start)
    enable_network_group = tgnObj.enable_network_group(network_group_list=['Network Group 1'],enable = True)
    print(enable_network_group)
    disable_network_group = tgnObj.enable_network_group(network_group_list=['Network Group 1'],enable = False)
    print(disable_network_group)
    end = datetime.datetime.now()
    print("stop time: ",end)
    print("time duration for API execution: ",end - start)

def test_modify_network_group_address_count():
    start = datetime.datetime.now()
    print("start time :",start)
    network_group_count = tgnObj.modify_network_group_address_count(network_group='Network Group 1', ip_type='ipv4', address_count=3)
    print(network_group_count)
    end = datetime.datetime.now()
    print("stop tiem: ",end)
    print("tiem duration for API execution",end - start)


#ISIS PROTOCOL:
#######################################################################################################

def test_set_isis_route_count_all():
    start = datetime.datetime.now()
    print("start_time:", start)
    isis_route_count_all = tgnObj.set_isis_route_count_all(route_count=50, ip_type="ipv4")
    print(isis_route_count_all)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_set_isis_route_count_1():
    start = datetime.datetime.now()
    print("start_time:", start)
    isis_route_count = tgnObj.set_isis_route_count(route_count=20,network_group="Network Group 1",prefix_step=2,ip_type='ipv6')
    print(isis_route_count)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_set_isis_route_count_2():
    start = datetime.datetime.now()
    print("start : ",start)
    isis_route_count = tgnObj.set_isis_route_count_all(route_count=50, ip_type="ipv4")
    print(isis_route_count)
    end = datetime.datetime.now()
    print("end: ",end)
    print("Time duration for API execution", end - start)

def test_get_isis_route_count():
    start =  datetime.datetime.now()
    print("start: ",start)
    isis_details=tgnObj.get_isis_route_count(network_group="Network Group 8",ip_type='ipv4')
    print(isis_details)
    end = datetime.datetime.now()
    print("end: ",end)
    print("Time duration for API execution ", end - start)

#MLD PROTOCOL
###########################################################################
def test_mld_start():
    start = datetime.datetime.now()
    print("start: ",start)
    mld_start = tgnObj.mld_start(port = ['10.39.65.156/2/15','10.39.65.156/2/16'])
    print(mld_start)
    end = datetime.datetime.now()
    print("end: ",end)
    print("Time duration for API execution ",end - start)

def test_mld_stop():
    start = datetime.datetime.now()
    print("start: ",satrt)
    mld_stop = tgnObj.mld_stop(port = ['10.39.65.156/2/15','10.39.65.156/2/16'])
    print(mld_stop)
    end = datetime.datetime.now()
    print("end: ",end)
    print("Time duration for API execution",end - start)

def test_get_mld_group_member():
    start = datetime.datetime.now()
    print("start_time:", start)
    igmp_member=tgnObj.get_mld_group_member('192.0.0.1',device_name='IPV6 Device Group 1')
    print(igmp_member)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_config_mld_group_member():
    start = datetime.datetime.now()
    print("start_time:", start)
    config_mld_group = tgnObj.config_mld_group_member(router_id="192.0.0.1",mcast_group_config={'count':'6'},mcast_source_config={'count':'2'},device_name ='IPv6 Device Group 1')
    print(config_mld_group)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_change_mld_source_list():
    start = datetime.datetime.now()
    print("start_time:", start)
    mld_src_list = tgnObj.change_mld_source_list(device_list=['IPv6 Device Group 1'],mld_source_list=['ff12:1::2'],port_list=['Ethernet - 001'])
    print(mld_src_list)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

   

#LDP PROTOCOL
################################################################################

def test_ldp_start():
    start = datetime.datetime.now()
    print("start: ",start)
    ldp_start = tgnObj.ldp_start(port=['Ethernet - 001','Ethernet - 002'])
    print(ldp_start)
    end = datetime.datetime.now()
    print("end: ",end)
    print("Time duration for API execution ",end - start)

def test_ldp_stop():
    start = datetime.datetime.now()
    print("start: ",satrt)
    ldp_stop = tgnObj.ldp_start(port=['Ethernet - 001','Ethernet - 002'])
    print(ldp_stop)
    end = datetime.datetime.now()
    print("end: ",end)
    print("Time duration for API execution",end - start)
