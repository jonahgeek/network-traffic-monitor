from scapy.all import *

def packet_handler(packet):
    if packet.haslayer(TCP) and packet[TCP].flags == 24:  # 24 corresponds to ACK+PSH flags
        source_ip = packet[IP].src
        dest_ip = packet[IP].dst
        source_port = packet[TCP].sport
        dest_port = packet[TCP].dport
        payload_length = len(packet[TCP].payload)
        
        if payload_length > 20000000:  # Check if payload is greater than 20MB
            alert_message = f"Large download detected: {payload_length} bytes"
            with open("download_alerts.log", "a") as log_file:
                log_file.write(alert_message + "\n")
            print(alert_message)
        
        print(f"Download detected:")
        print(f"Source IP: {source_ip}")
        print(f"Destination IP: {dest_ip}")
        print(f"Source Port: {source_port}")
        print(f"Destination Port: {dest_port}")
        print(f"Payload Length: {payload_length} bytes")
        print("=" * 30)

if __name__ == "__main__":
    sniff(filter="tcp", prn=packet_handler)
