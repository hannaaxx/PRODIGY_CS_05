# Packet Sniffer Tool

A lightweight and educational packet sniffer that captures and analyzes network packets. This tool demonstrates the basics of packet inspection by displaying critical information such as source/destination IP addresses, protocols, and payload data.

## Features
- Captures IPv4 packets from the network.
- Displays essential packet information:
  - Source and destination IP addresses.
  - Protocol number.
  - Payload (data portion of the packet).
- Outputs payload data in a human-readable format.

## Prerequisites
- Python 3.x installed.
- Administrative/root privileges to execute the script.

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/packet-sniffer.git
   cd packet-sniffer
Run the script:

bash
Copy code
sudo python3 packet_sniffer.py
Stop the script using Ctrl+C.

Ethical Use
This tool is intended strictly for educational purposes. Misuse of this tool for unauthorized packet capturing may violate local laws and regulations. Use it only in environments where you have explicit permission to monitor network traffic.

Example Output
vbnet
Copy code
Listening for packets... (Press Ctrl+C to stop)

Source IP: 192.168.1.5
Destination IP: 93.184.216.34
Protocol: 6
Payload:
    0x4500003c1c4640004006b1e6c0a80105...
Limitations
Captures only IPv4 traffic.
Limited protocol decoding; extend the script for comprehensive analysis.
Contribution
Feel free to fork this repository and contribute enhancements.

License
This project is licensed under the MIT License. See the LICENSE file for details.

yaml
Copy code

---

### Uploading to GitHub
1. Initialize a GitHub repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Packet Sniffer Tool"
   git branch -M main
   git remote add origin https://github.com/hannaaxx/packet-sniffer.git
   git push -u origin main
