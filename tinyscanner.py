import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port, protocol):
    try:
        if protocol == "tcp":
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((host, port))
                if result == 0:
                    try:
                        service = socket.getservbyport(port, "tcp")
                    except:
                        service = "Unknown"
                    return f"Port {port} is open (Service: {service})"
                else:
                    return f"Port {port} is closed"
        elif protocol == "udp":
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.settimeout(1)
                s.sendto(b"", (host, port))
                try:
                    s.recvfrom(1024)
                    return f"Port {port} is open (UDP)"
                except socket.timeout:
                    return f"Port {port} is closed"
    except Exception as e:
        return f"Error scanning port {port}: {e}"

def parse_args():
    parser = argparse.ArgumentParser(description="A simple port scanner")
    parser.add_argument("host", help="Target host to scan")
    parser.add_argument("-p", "--ports", required=True, help="Port or range of ports to scan (e.g., 80 or 80-100)")
    parser.add_argument("-t", "--tcp", action="store_true", help="Use TCP protocol")
    parser.add_argument("-u", "--udp", action="store_true", help="Use UDP protocol")
    return parser.parse_args()

def main():
    args = parse_args()
    protocol = "tcp" if args.tcp else "udp" if args.udp else None
    if not protocol:
        print("Error: You must specify either -t (TCP) or -u (UDP).")
        return

    host = args.host
    port_range = args.ports

    # Parse port range
    if "-" in port_range:
        start_port, end_port = map(int, port_range.split("-"))
        ports = range(start_port, end_port + 1)
    else:
        ports = [int(port_range)]

    print(f"Scanning {host} on ports {port_range} using {protocol.upper()}...")

    # Use ThreadPoolExecutor for concurrent scanning
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(lambda p: scan_port(host, p, protocol), ports)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
