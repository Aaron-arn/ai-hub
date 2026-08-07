"""IP tools: validate and parse IPv4 and IPv6 addresses and CIDR ranges."""

import ipaddress
import sys


def usage():
    print("Usage: python main.py validate <ip>")
    print("       python main.py describe <ip-or-network>")
    print("       python main.py cidr <network/prefix>")


def describe_address(ip):
    version = "IPv4" if ip.version == 4 else "IPv6"
    flags = []
    if ip.is_loopback:
        flags.append("loopback")
    if ip.is_link_local:
        flags.append("link-local")
    if ip.is_private:
        flags.append("private")
    if ip.is_global:
        flags.append("global")
    if ip.is_multicast:
        flags.append("multicast")
    if ip.is_reserved:
        flags.append("reserved")
    label = ", ".join(flags) if flags else "no special flags"
    return f"{ip} is a valid {version} address ({label})"


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        usage()
        sys.exit(1)
    command, target = args[0], args[1]
    try:
        if command == "validate":
            try:
                ipaddress.ip_address(target)
                print("Valid")
            except ValueError:
                try:
                    ipaddress.ip_network(target, strict=False)
                    print("Valid (network)")
                except ValueError:
                    print("Invalid")
        elif command == "describe":
            try:
                ip = ipaddress.ip_address(target)
                print(describe_address(ip))
            except ValueError:
                network = ipaddress.ip_network(target, strict=False)
                print(f"{network}: {network.num_addresses} addresses "
                      f"(first {network.network_address}, last {network.broadcast_address})")
        elif command == "cidr":
            network = ipaddress.ip_network(target, strict=False)
            print(f"network: {network.network_address}")
            print(f"broadcast: {network.broadcast_address}")
            print(f"prefix: /{network.prefixlen}")
            print(f"addresses: {network.num_addresses}")
        else:
            raise ValueError(f"unknown command: {command}")
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
