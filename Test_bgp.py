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