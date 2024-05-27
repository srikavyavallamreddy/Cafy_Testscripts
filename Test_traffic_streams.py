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

tgnObj = IXIA(server_ip=apiServerIp)
tgnObj.connect_to_session()


def test_get_port_traffic_streams():
    start = datetime.datetime.now()
    print("start_time:", start)
    traffic_item_name=tgnObj.get_port_traffic_streams('Ethernet - 003')
    print(traffic_item_name)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

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

def test_change_traffic_mac():
    start = datetime.datetime.now()
    print("start: ",start)
    traffic_mac = tgnObj.change_traffic_mac(traffic_item_name='Traffic Item 1',endpoint_name='EndpointSet-1',mac_dst='00:00:00:00:00:05',mac_src='00:00:00:00:00:03')
    print(traffic_mac)
    end = datetime.datetime.now()
    print("end: ",end)
    print("Time duration for API execution ",end - start)

def test_set_stream_frame():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.set_stream_frame('Traffic Item 2', {'ipv6':{'dst_ip':{'value': '10:0:1:2::20',
                'step': '1::1:0:0:1', 'count': '100','valueType': 'increment'}}})
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

def test_delete_traffic_items():
    start = datetime.datetime.now()
    print("start_time:", start)
    del_traffic = tgnObj.delete_traffic_items(traffic_item_list=['Traffic Item 3','Traffic Item 2'])
    print(del_traffic)
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

    
