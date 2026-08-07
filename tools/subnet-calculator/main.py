"""Subnet calculator: compute network details from a CIDR block."""

import ipaddress
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <network/prefix>")
        print("Example: python main.py 192.168.1.0/24")
        sys.exit(1)
    cidr = sys.argv[1]
    try:
        network = ipaddress.ip_network(cidr, strict=False)
    except ValueError as exc:
        print(f"Error: invalid CIDR: {exc}")
        sys.exit(1)
    print(f"CIDR: {network}")
    print(f"Network: {network.network_address}")
    print(f"Broadcast: {network.broadcast_address}")
    print(f"Netmask: {network.netmask}")
    print(f"Wildcard: {network.hostmask}")
    print(f"Prefix: /{network.prefixlen}")
    total = network.num_addresses
    print(f"Total addresses: {total}")
    if total > 2:
        hosts = list(network.hosts())
        print(f"Usable hosts: {total - 2}")
        print(f"First host: {hosts[0]}")
        print(f"Last host: {hosts[-1]}")
    elif total == 2:
        print("Usable hosts: 0 (point-to-point link)")


if __name__ == "__main__":
    main()
