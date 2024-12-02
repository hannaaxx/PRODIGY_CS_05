import socket
import struct
import textwrap

def format_multi_line(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])

def unpack_ipv4(packet):
    ipv4_header = packet[:20]
    unpacked_header = struct.unpack('!BBHHHBBH4s4s', ipv4_header)
    version_ihl = unpacked_header[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF
    tos = unpacked_header[1]
    total_length = unpacked_header[2]
    identification = unpacked_header[3]
    flags_offset = unpacked_header[4]
    ttl = unpacked_header[5]
    protocol = unpacked_header[6]
    checksum = unpacked_header[7]
    src_ip = socket.inet_ntoa(unpacked_header[8])
    dst_ip = socket.inet_ntoa(unpacked_header[9])
    return {
        "Version": version,
        "Header Length": ihl,
        "TTL": ttl,
        "Protocol": protocol,
        "Source IP": src_ip,
        "Destination IP": dst_ip,
        "Data": packet[ihl * 4:]
    }

def main():
    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    conn.bind(("0.0.0.0", 0))
    conn.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    print("Listening for packets... (Press Ctrl+C to stop)")

    try:
        while True:
            raw_packet, addr = conn.recvfrom(65565)
            ipv4 = unpack_ipv4(raw_packet)
            print(f"\nSource IP: {ipv4['Source IP']}")
            print(f"Destination IP: {ipv4['Destination IP']}")
            print(f"Protocol: {ipv4['Protocol']}")
            print(f"Payload:\n{format_multi_line('\t', ipv4['Data'])}")
    except KeyboardInterrupt:
        print("\nPacket sniffing stopped.")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
