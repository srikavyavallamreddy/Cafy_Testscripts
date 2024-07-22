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

    
    @pytest.mark.parametrize("mode", modes)
    def test_start_traffic(self, mode):
        """
        Unit test for start_traffic()
        """
        tgn_object = ApData.tgn_objects[mode]
        Helper.sleep(10, msg='waiting 10 seconds before start traffic')
        Helper.sleep(10, msg='waiting 10 seconds before start traffic')
        tgn_object.regenerate_traffic()
        Helper.sleep(5, msg='waiting 5 seconds after traffic regenerated')
        tgn_object.start_traffic(timer_ticks=40)

    
    @pytest.mark.parametrize("mode", modes)
    def test_stop_traffic(self, mode):
        """
        Unit test for stop_traffic()
        """
        tgn_object = ApData.tgn_objects[mode]
        Helper.sleep(60, msg='waiting for stop traffic')
        tgn_object.stop_traffic(timer_ticks=40)
        timeout_ticks = 3
        state = tgn_object.check_traffic_state(expected='stopped', timer_ticks=timeout_ticks)
        if state:
            log.info('Traffic has stopped')
        else:
            log.info('Traffic has not stopped yet')

    @pytest.mark.parametrize("mode", modes)
    def test_verify_traffic(self, mode):
        """
        verify all traffic
        """
        tgn_object = ApData.tgn_objects[mode]
        tgn_object.regenerate_traffic()
        Helper.sleep(5, msg='waiting 5 seconds after traffic regenerated')
        tgn_object.start_traffic(timer_ticks=40)
        Helper.sleep(30, msg='waiting for verify traffic')
        item_stats, flow_stats = tgn_object.verify_traffic(tolerance=3.5)
        log.info('Item stats: %s' %item_stats)
        log.info('Flow stats: %s' %flow_stats)

    
    @pytest.mark.parametrize("mode", modes)
    def test_verify_traffic_optimization_fix(self, mode):
        """
        verify all traffic
        """
        tgn_object = ApData.tgn_objects[mode]
        Helper.sleep(30, msg='waiting for verify traffic')
        item_stats, flow_stats = tgn_object.verify_traffic()
        log.info(f"Item stats: {item_stats}")
        log.info(f"Flow stats: {flow_stats}")

    @pytest.mark.parametrize("mode", modes)
    def test_verify_traffic_mc_rx_port(self, mode):
        """
        verify traffic mc rx port
        """
        tgn_object = ApData.tgn_objects[mode]
        if mode == 'IXIA':
            ports = {'all_ports': True,
                     'Ingress': {'tolerance': 5500},
                     'Egress1': {'tolerance': 90000}}
        elif mode == 'Spirent':
            ports = {'all_ports': True,
                     'AR-TenGigE0/0/0/18-Port 5/7': {'tolerance': 200000},
                     'DR-FortyGigE0/6/0/16-Port 9/17': {'tolerance': 500}}

        Helper.sleep(30, msg='waiting for verify traffic')
        headers = ['Traffic Item', 'Tx Port', 'Rx Port', 'IP :Source Address',
                   'IP :Destination Address', 'Tx Frames', 'Rx Frames',
                   'Frames Delta', 'Loss %', 'Expected', 'Tolerance', 'Status']
        item_stats, flow_stats = tgn_object.verify_traffic(mode='rx_port',
                                                           debug=None,
                                                           tolerance=100000,
                                                           tolerance_mode='frame',
                                                           ports=ports)
        log.info('Item stats: %s' %item_stats)
        log.info('Flow stats: %s' %flow_stats)

    @pytest.mark.parametrize("mode", modes)
    def test_verify_traffic_mc_tx_port(self, mode):
        """
        verify traffic mc tx port
        """
        tgn_object = ApData.tgn_objects[mode]
        if mode == 'IXIA':
            ports = {'all_ports': False, 'Ingress': {}}
            traffic_items = {'all_traffic_items': False, 'Traffic Item 1': {}}
        elif mode == 'Spirent':
            ports = {'all_ports': False, 'DR-FortyGigE0/6/0/16-Port 9/17': {}}
            traffic_items = {'all_traffic_items': False, 'DR-to-AR-BGP1':{}}

        Helper.sleep(30, msg='waiting for verify traffic')
        headers = ['Traffic Item', 'Tx Port', 'Rx Port', 'IP :Source Address',
                   'IP :Destination Address', 'Tx Frames', 'Rx Frames',
                   'Frames Delta', 'Loss %', 'Expected', 'Tolerance', 'Status']
        item_stats, flow_stats = tgn_object.verify_traffic(tolerance=3.2,
                                                           mode='tx_port',
                                                           ports=ports,
                                                           traffic_items=traffic_items,
                                                           headers=headers,
                                                           flow_per_stream=10)
        log.info('Item stats: %s' %item_stats)
        log.info('Flow stats: %s' %flow_stats)

    
    @pytest.mark.verify
    @pytest.mark.parametrize("mode", modes)
    def test_disable_traffic_item(self, mode):
        """
        Unit test for disable_traffic_item()
        """
        tgn_object = ApData.tgn_objects[mode]
        if mode == 'IXIA':
            traffic_item = Traffic_Item[0]
        elif mode == 'Spirent':
            traffic_item = 'DR-to-AR-BGP1'
        disable_traffic = tgn_object.disable_traffic_item([traffic_item])
        if not disable_traffic:
            pytest.fail(" Traffic Item/Items Not Disabled Successfully")

    @pytest.mark.verify
    @pytest.mark.parametrize("mode", modes)
    def test_enable_traffic_item(self, mode):
        """
        Unit test for enable_traffic_item()
        """
        tgn_object = ApData.tgn_objects[mode]
        if mode == 'IXIA':
            traffic_item = Traffic_Item[0]
        elif mode == 'Spirent':
            traffic_item = 'DR-to-AR-BGP1'
        enable_traffic = tgn_object.enable_traffic_item([traffic_item])
        Helper.sleep(10, msg='waiting 10 seconds after traffic enabled')
        print(enable_traffic)
        if not enable_traffic:
            pytest.fail(" Traffic Item/Items Not Enabled Successfully")
        

    @pytest.mark.second_run
    @pytest.mark.parametrize("mode", modes)
    def test_traffic_rate(self, mode):
        """
        Unit test for get_traffic_rate()
        """
        tgn_object = ApData.tgn_objects[mode]
        traffic_rate = tgn_object.get_traffic_rate()
        actual_keys = list(traffic_rate.keys())  # Convert dict_keys to a list of keys
        expected_keys = Traffic_Item
        if all(key in actual_keys for key in expected_keys):
            print("Get Traffic Item rate  Successfull")
        else:
            pytest.fail("Traffic Item/Items Not Enabled ")


    @pytest.mark.second_run
    @pytest.mark.parametrize("mode", modes)
    def test_change_traffic_frame_size(self, mode):
        """
        Unit test for change_traffic_frame_size
        """
        tgn_object = ApData.tgn_objects[mode]
        packetsize_fixed = {'type':'fixed', 'fixedSize':400}
        packetsize_auto = {'type':'auto'}
        packetsize_increment = {'type':'increment', 'incrementStep':2,'incrementFrom':400, 'incrementTo':500}
        packetsize_imix = {'type':'weightedPairs',
                           'weightedPairs':['70:7', '590:4', '1518:1']}
        if mode == 'IXIA':
            traffic_items = Traffic_Item[2]
            packet_sizes = [packetsize_fixed, packetsize_auto, packetsize_increment, packetsize_imix]
        if mode == 'Spirent':
            traffic_items = ['DR-to-AR-BGP1']
            packet_sizes = [packetsize_fixed, packetsize_auto, packetsize_increment]
            log.warning('IMIX option has not been implemented for Spirent yet')

        for packet_size in packet_sizes:
            tgn_object.change_traffic_frame_size(packet_size, traffic_items)
            Helper.sleep(10, msg='waiting 10 seconds after type changed to %s' %packet_size['type'])
            tgn_object.start_traffic(timer_ticks=240)
            Helper.sleep(30, msg='waiting for stop traffic')
            tgn_object.stop_traffic(timer_ticks=240)


    @pytest.mark.second_run
    @pytest.mark.parametrize("mode", modes)
    def test_change_traffic_rate(self, mode):
        """
        Unit test for change_traffic_rate()
        """
        tgn_object = ApData.tgn_objects[mode]
        traffic_items = None
        framepersec = {'type':'framesPerSecond', 'rate':200}
        rateperlinerate = {'type':'percentLineRate', 'rate':0.2}
        for traffic_rate in [framepersec, rateperlinerate]:
            tgn_object.change_traffic_rate(traffic_rate, traffic_items)
            Helper.sleep(10, msg='waiting 10 second after type changed to %s' %
                         traffic_rate['type'])
            tgn_object.start_traffic(timer_ticks=240)
            Helper.sleep(30, msg='waiting for stop traffic')
            tgn_object.stop_traffic(timer_ticks=240)