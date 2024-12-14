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