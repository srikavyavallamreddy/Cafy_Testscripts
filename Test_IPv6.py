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

def test_get_ipv6_traffic_class_information():
    start = datetime.datetime.now()
    print("start_time:", start)
    tgnObj.get_ipv6_traffic_class_information()
    end = datetime.datetime.now()
    print("stop time:", end)
    print("time duration for API execution", end - start)
    #Get IPv6 Traffic Class (TC) configuration for a given traffic stream
    #traffic item should have ipv6 header