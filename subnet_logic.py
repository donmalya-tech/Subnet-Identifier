import ipaddress
import csv


def subnet_extra_info(ip, prefix):
    network = ipaddress.ip_network(f"{ip}/{prefix}", strict=False)
    hosts = list(network.hosts())

    return {
        "Network": str(network),
        "Network ID": str(network.network_address),
        "Broadcast": str(network.broadcast_address) if network.version == 4 else "N/A",
        "Subnet Mask": str(network.netmask) if network.version == 4 else "N/A",
        "CIDR": f"/{network.prefixlen}",
        "First Host": str(hosts[0]) if hosts else "N/A",
        "Last Host": str(hosts[-1]) if hosts else "N/A",
        "Total Addresses": network.num_addresses,
        "Usable Hosts": max(network.num_addresses - 2, 0) if network.version == 4 else network.num_addresses
    }


def calculate_subnets(network_ip, original_prefix, new_prefix):
    base = ipaddress.ip_network(f"{network_ip}/{original_prefix}", strict=False)

    if new_prefix <= original_prefix:
        raise ValueError("New prefix must be greater than original prefix")

    results = []

    for subnet in base.subnets(new_prefix=new_prefix):
        hosts = list(subnet.hosts())
        results.append({
            "Subnet": str(subnet),
            "Network ID": str(subnet.network_address),
            "Broadcast": str(subnet.broadcast_address) if subnet.version == 4 else "N/A",
            "First Host": str(hosts[0]) if hosts else "N/A",
            "Last Host": str(hosts[-1]) if hosts else "N/A",
            "Usable Hosts": max(subnet.num_addresses - 2, 0)
        })

    return results


def calculate_subnets_by_hosts(network_ip, prefix, required_hosts):
    network = ipaddress.ip_network(f"{network_ip}/{prefix}", strict=False)

    bits = 0
    while (2 ** bits - 2) < required_hosts:
        bits += 1

    new_prefix = network.max_prefixlen - bits

    if new_prefix <= prefix:
        raise ValueError("Not enough address space")

    return calculate_subnets(network_ip, prefix, new_prefix)


def export_subnets_to_csv(subnets, filename):
    if not subnets:
        raise ValueError("No data to export")

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=subnets[0].keys())
        writer.writeheader()
        writer.writerows(subnets)


def validate_ip_and_prefix(ip, prefix):
    try:
        ipaddress.ip_network(f"{ip}/{prefix}", strict=False)
        return True
    except ValueError:
        return False
