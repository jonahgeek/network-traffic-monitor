# Network Traffic Monitor Script

This script is designed to monitor network traffic and detect large downloads based on TCP packets with specific flags. It utilizes the `scapy` library to capture and analyze packets, focusing on TCP packets with ACK+PSH flags. If a packet with this combination of flags is found and the payload size is greater than 20MB, the script logs an alert message and prints details about the download.

## Prerequisites

- Python 3.x
- `scapy` library (install using `pip install scapy`)

## Usage

1. Install the required packages:

   ```bash
   pip install scapy
   ```

2. Run the script:

   ```bash
   python script.py
   ```

3. The script will start capturing network traffic and analyze TCP packets. If a packet with the ACK+PSH flags is detected and its payload size exceeds 20MB, an alert will be logged in the `download_alerts.log` file.

## How It Works

1. The script uses the `scapy` library to capture network packets.
2. It filters for TCP packets using the provided `filter` parameter.
3. For each TCP packet with ACK+PSH flags, the script extracts relevant information such as source IP, destination IP, source port, destination port, and payload length.
4. If the payload length is greater than 20MB, an alert is logged in the `download_alerts.log` file, and information about the download is printed.

## Configuration

You can customize the script by modifying the following parameters:

- `filter`: Change the packet filter as needed to capture specific types of network traffic.
- `payload_length_threshold`: Adjust the threshold for payload size that triggers an alert.

## Logs

The script logs download alerts to the `download_alerts.log` file in the same directory. Each alert message includes the timestamp and information about the detected download.

## Disclaimer

This script is provided as-is and may require further adaptation to suit specific network environments. Use it responsibly and ensure that you have the necessary permissions before monitoring network traffic.
