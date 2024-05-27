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

def test_change_igmp_source_list_2():
    start = datetime.datetime.now()
    print("start_time:", start)
    igmp_src = tgnObj.change_igmp_source_list(device_list=['IPv4 Device Group 1','IPv4 Device Group 2'],igmp_source_list=['12.10.10.1','12.10.10.2','12.10.10.3','12.10.10.4','12.10.10.5'], port_list=['Ethernet - 001','Ethernet - 002'])
    print(igmp_src)
    
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)

