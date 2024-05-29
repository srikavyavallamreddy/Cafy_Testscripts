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
    print("start: ",start)
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

def test_set_igmp_mld_rate():
    start = datetime.datetime.now()
    print("start time :",start)
    igmp_rate = tgnObj.set_igmp_mld_rate(device_type='mld', rate=4000)
    print(igmp_rate)
    end = datetime.datetime.now()
    print("stop time :",end)
    print("Time duration for API execution",end - start)