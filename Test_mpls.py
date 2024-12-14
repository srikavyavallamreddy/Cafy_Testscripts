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

def test_get_traffic_mpls_exp_bits():
    start = datetime.datetime.now()
    print("start_time:", start)
    exp_bit= tgnObj.get_traffic_mpls_exp_bits(traffic_item_list=['Traffic Item 1'])
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