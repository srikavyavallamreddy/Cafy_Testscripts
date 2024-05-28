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

def test_new_blank_config():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.new_blank_config()
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)


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

def test_get_link_status():
    start = datetime.datetime.now()
    print("start_time:", start)
    port_list = tgnObj.get_link_status()
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
   

def test_get_list_port_name():
    start = datetime.datetime.now()
    print("start_time:", start)
    port_name=tgnObj.get_list_port_name()
    print(port_name)
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

def test_get_device_ip_info():
    start = datetime.datetime.now()
    print("start_time:", start)
    ip_address=tgnObj.get_device_ip_info("100.0.0.1", ip_version='ipv4', key='Address')
    print(ip_address)
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
    

def test_stop_all_protocols():
    start = datetime.datetime.now()
    print("start_time:", start)
    start_protocols=tgnObj.stop_all_protocols()
    print(start_protocols)
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

def test_set_device_count():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.set_device_count(device_count = 5,device_name='IPv4 Device Group 1')
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

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

def test_get_card_type():
    start = datetime.datetime.now()
    print("start_time:", start)
    card_type = tgnObj.get_card_type("10.39.65.156/2/15")
    print(card_type)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_add_device():
    start = datetime.datetime.now()
    print("start time :",start)
    device = tgnObj.add_device(port_list= ["10.39.65.156/2/15"])
    print(device)
    end = datetime.datetime.now()
    print("end time :",end)
    print("Time duration for API execution",end - start)

def test_add_device_bgp():
    start =  datetime.datetime.now()
    print("start time :",start)
    device = tgnObj.add_device(port_list= ["10.39.65.156/2/15"],ipv4_address_start = "10.9.0.1",bgp_v4_active = True)
    end = datetime.datetime.now()
    print("stop time :",end)
    print("Time duration for API execution ",end - start)
    
    