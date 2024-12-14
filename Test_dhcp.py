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


def test_get_stream_dhcp_client_mac():
    start = datetime.datetime.now()
    print("start time: ",start)
    dhcp_mac = tgnObj.get_stream_dhcp_client_mac('Traffic Item 1')
    print(dhcp_mac)
    end = datetime.datetime.now()
    print("end time :",end)
    print("Time duration for API execution ",end - start)
    #ADD DHCP header in traffic item with valid mac address 

def test_set_stream_dhcp_client_mac():
    start = datetime.datetime.now()
    print("start time :",start)
    dhcp_mac = tgnObj.set_stream_dhcp_client_mac('Traffic Item 1','0xaa0a0a0a0a0a')
    print(dhcp_mac)
    end = datetime.datetime.now()
    print("end time :",end)
    print("Time duration for API execution ",end - start)

