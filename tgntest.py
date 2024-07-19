#**************************************************
# Copyright (c) 2018 Cisco Systems, Inc.
# All rights reserved.
#**************************************************
"""
This is the unit test suite for the cafykit TGN library.
It covers testing for both Spirent and IXIA.
"""
from datetime import datetime
import os, getpass
import pytest
from logger.cafylog import CafyLog
from logger.cafylog import CafyLog
from utils.helper import Helper
from utils.cafyexception import CafyException
log = CafyLog()
import time

# For PyTest Parametrize
modes = ["IXIA"]

from ixiaMaster import IXIA
apiServerIp = '127.0.0.1'
tgn_object = IXIA(server_ip=apiServerIp)
tgn_object.connect_to_session()

port_name = []


@pytest.mark.setup
class ApData:
    zap = {}
    tgn_objects = {}
    log = CafyLog()

@pytest.mark.setup
def setup_module():
    """
    Instantiate Spirent/IXIA
    :return:
    """
    ApData.tgn_objects['IXIA'] = tgn_object

@pytest.mark.random_order(disabled=True)
class TestTGN():

    # To avoid execution of testcases in random order
    pytestmark = pytest.mark.random_order(disabled=True)


    @pytest.mark.setup
    @pytest.mark.first_level
    @pytest.mark.parametrize("mode", modes)
    def test_get_list_ports_name(self, mode):
        """
        Unit test for get_list_port_name()
        """
        global port_name
        tgn_object = ApData.tgn_objects[mode]
        port_name = tgn_object.get_list_port_name()
        log.info('Port names are: %s' %port_name)

    @pytest.mark.first_level
    @pytest.mark.parametrize("mode", modes)
    def test_get_port_traffic_streams(self, mode):
        """
        Unit test for get_port_traffic_streams()
        """
        global Traffic_Item
        tgn_object = ApData.tgn_objects[mode]
        Traffic_Item = tgn_object.get_traffic_items()
        for port in port_name:
            streams = tgn_object.get_port_traffic_streams(port)
            log.info('Streams with port %s are: %s' %(port, streams))

    # @pytest.mark.setup
    # @pytest.mark.parametrize("mode", modes)
    # def test_load_config(self, mode):
    #     """
    #     Unit test for load_config()
    #     """
    #     tgn_object = ApData.tgn_objects[mode]
    #     cfg_file = "/tmp/traffic_fail.xml"
    #     ports = ("//1.0.0.2/1/1", "//1.0.0.2/1/2")
    #     ports = tgn_object.load_config(config_file=cfg_file,
    #                                    port_tuple=ports,
    #                                    debug_print=True, reserve_ports=True)
    #     log.info('Configuration loaded successfully')

    @pytest.mark.parametrize("mode", modes)
    def test_get_interfaces(self, mode):
        """
        Unit test for get_interfaces()
        """
        tgn_object = ApData.tgn_objects[mode]
        interfaces = tgn_object.get_interfaces()
        log.info('Interfaces are %s' %interfaces)

    @pytest.mark.parametrize("mode", modes)
    def test_get_interfaces_by_name(self, mode):
        """
        Unit test for get_interfaces_by_name()
        """
        tgn_object = ApData.tgn_objects[mode]
        interfaces_names = tgn_object.get_interfaces_by_name()
        log.info('Names of interfaces are %s' %interfaces_names)
    
    @pytest.mark.parametrize("mode", modes)
    def test_start_all_protocols(self, mode):
        """
        Unit test for start_all_protocols()
        """
        tgn_object = ApData.tgn_objects[mode]
        tgn_object.start_all_protocols()
        Helper.sleep(80, msg='waiting for all protocols start')

    @pytest.mark.parametrize("mode", modes)
    def test_get_link_status(self, mode):
        """
        Unit test for get_link_status()
        """

        tgn_object = ApData.tgn_objects[mode]
        link_status_info = tgn_object.get_link_status(print_info=True)
        for port_info in link_status_info:
            port_name = port_info[0].split(':')[1].strip()  # Extracts 'Ethernet - 003'
            port_state = port_info[1].split(':')[1].strip().lower()  # Extracts 'up' and converts to lowercase
            # Assertion to verify each port state is 'up'
            assert port_state == 'up', f"Port {port_name} is not up. State is {port_state}"


    @pytest.mark.first_level
    @pytest.mark.parametrize("mode", modes)
    def test_get_active_streams(self, mode):
        """
        Unit test for get_active_streams()
        """
        tgn_object = ApData.tgn_objects[mode]
        active_streams = tgn_object.get_active_streams()
        log.info('Active streams are: %s' %active_streams)
        for stream in active_streams:
            assert stream in Traffic_Item, f"Stream '{stream}' not found in Traffic_Item list"

    @pytest.mark.parametrize("mode", modes)
    def test_get_streamblock_preview(self, mode):
        """
        To Get Streamblock preview details
        """
        if mode == "IXIA":
            pytest.skip("This is Spirent specific API")
        if mode == "Spirent":
            tgn_object = ApData.tgn_objects[mode]
            tgn_object.get_streamblock_preview()

    @pytest.mark.parametrize("mode", modes)
    def test_modify_ignore_link_status(self, mode):
        """
        Enable or disable ignore link status
        """
        tgn_object = ApData.tgn_objects[mode]
        tgn_object.modify_ignore_link_status(status="disable")
        tgn_object.modify_ignore_link_status(status="enable")
    
    @pytest.mark.parametrize("mode", modes)
    def test_modify_streamblock_params(self, mode):
        """
        To modify TCP packet header for given streams
        """
        if mode == "IXIA":
            pytest.skip("This is Spirent specific API")
        if mode == "Spirent":
            tgn_object = ApData.tgn_objects[mode]
            payload_var={"payload_fill_constant":50, "payload_fill_type":"DECR"}
            tgn_object.modify_streamblock_params(traffic_item_list=['Traffic-1', 'Traffic-2'], cfg_dict=payload_var)
    
    @pytest.mark.parametrize("mode", modes)
    def test_set_port_transmit_deviation(self, mode):
        """
        To Set the Transmit deviation type for given ports
        """
    
        tgn_object = ApData.tgn_objects[mode]
        tgn_object.set_port_transmit_deviation(deviation_value=20)
        tgn_object.start_all_protocols()
        Helper.sleep(80, msg='waiting for all protocols start')
    

    @pytest.mark.parametrize("mode", modes)
    def test_set_port_transmit_deviation_with_incr(self, mode):
        """
        To Set the Transmit deviation type for given ports
        """
    
        tgn_object = ApData.tgn_objects[mode]
        tgn_object.set_port_transmit_deviation(deviation_value=10, operation="increment", wait_interval=5, repetition=2)
        tgn_object.start_all_protocols()
        Helper.sleep(80, msg='waiting for all protocols start')

    