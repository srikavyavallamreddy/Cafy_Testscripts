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
    print(ipv4_tos)
    end = datetime.datetime.now()
    print("end: ",end)
    print("Time duration for API execution ",end - start)

def test_change_ipv4_tos_2():
    start = datetime.datetime.now()
    print("start: ",start)
    ipv4_tos = tgnObj.change_ipv4_tos(traffic_item_list=["Traffic Item 1"],cfg_dict={'valueType':'increment','fieldValue':'000 Routine','startValue':'2','stepValue':'1','countValue':'15'})
    print(ipv4_tos)
    end = datetime.datetime.now()
    print("end: ",end)
    print("Time duration for API execution ",end - start)

def test_change_ipv4_tos_2():
    start = datetime.datetime.now()
    print("start: ",start)
    ipv4_tos = tgnObj.change_ipv4_tos(traffic_item_list=["Traffic Item 1"],cfg_dict={'valueType':'increment','fieldValue':'000 Routine','startValue':'2','stepValue':'1','countValue':'15'})
    print(ipv4_tos)
    end = datetime.datetime.now()
    print("end: ",end)
    print("Time duration for API execution ",end - start)

def test_get_frame_l4_information():
    start = datetime.datetime.now()
    print("start_time:", start)
    get_frame = tgnObj.get_frame_l4_information()
    print(get_frame)
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

def test_create_ipv4_interface():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.create_ipv4_interface(router_id='192.0.0.1',ipv4_address='100.10.1.1',
                              ipv4_gateway='10.10.1.2', ipv4_gateway_mac='00:00:01:00:00:01',
                              ipv4_prefix_length='24')
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)