import scapy.all as scapy
import re
import time
def ip(user_ip):
    target=scapy.ARP(pdst=user_ip)
    target_mac=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    ip_mac= target_mac / target
    answered=scapy.srp(ip_mac,timeout=10,verbose=False)[0]
    return answered[0][1].hwsrc

def check(target_ip):
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                       25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                       25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                       25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
    if not target_ip:
        print("no ip provided")
        return 0
    if re.search(regex,target_ip):
        print("ip accepted")
        return target_ip
    else:
        print("bad ip input try again")
        return 0

def main():
    target_ip=input(">>")
    target_ip=target_ip.strip()

    target_ip1=check(target_ip)
    while(target_ip1==0):
        target_ip=input(">>").strip()
        target_ip1 = check(target_ip)
    return target_ip














