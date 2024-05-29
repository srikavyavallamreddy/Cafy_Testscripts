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

def test_set_isis_sr_mpls():
    start = datetime.datetime.now()
    print("start timen :",start)
    sr_mpls = tgnObj.set_isis_sr_mpls(device_list=["IPv4 Device Group 2"])
    print(sr_mpls)
    end = datetime.datetime.now()
    print("stop time ",end)
    print("Time duration for API execution ",end - start)
    