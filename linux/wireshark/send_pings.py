
# livepcap=/tmp/scapy.pcap
# rm $livepcap; touch $livepcap
# python send_pings.py & tail -f -n +1 $livepcap | tshark -r -
# This script will send pings to 8.8.8.8 spaces 1 sec apart
# And write the traffic to a pacp file

import time
import os

from scapy.all import PcapWriter, sr, IP, ICMP

livepcap = "/tmp/scapy.pcap"
with PcapWriter(livepcap, append=True, sync=True) as pkt_pipe:
    pkt = IP(dst="8.8.8.8") / ICMP()
    while True:
        ans, unans = sr(pkt, verbose=False, retry=0)
        packets = ans or unans
        pkt_pipe.write(packets)
        time.sleep(1)


https://tshark.dev/capture/sources/downloading_file/