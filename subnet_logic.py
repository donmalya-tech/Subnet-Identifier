import ipaddress
import csv

def subnet_extra_info(ip, prefix):
    network = ipaddress.ip_network(f"{ip}/{prefix}", strict=False)

    if network.version == 4:
        hosts = list(network.hosts())
        first = hosts[0] if hosts else "N/A"
        last = hosts[-1] if hosts else "N/A"
        usable = max(network.num_addresses - 2, 0)
        broadcast = network.broadcast_address
        netmask = network.netmask
    else:  # IPv6
        first = network.network_address + 1
        last = network.network_address + network.num_addresses - 1
        usable = network.num_addresses
        broadcast = "N/A"
        netmask = "N/A"

    return {
        "Network": str(network),
        "Network ID": str(network.network_address),
        "Broadcast": str(broadcast),
        "Subnet Mask": str(netmask),
        "CIDR": f"/{network.prefixlen}",
        "First Host": str(first),
        "Last Host": str(last),
        "Total Addresses": network.num_addresses,
        "Usable Hosts": usable
    }


def calculate_subnets(network_ip, original_prefix, new_prefix, max_subnets=1000):
    import ipaddress

    base = ipaddress.ip_network(f"{network_ip}/{original_prefix}", strict=False)

    # Calculate how many subnets this would generate
    subnet_count = 2 ** (new_prefix - base.prefixlen)
    if subnet_count > max_subnets:
        raise ValueError(f"Too many subnets ({subnet_count}). Limit: {max_subnets}")

    results = []

    for subnet in base.subnets(new_prefix=new_prefix):
        if subnet.version == 4:
            first = subnet.network_address + 1
            last = subnet.network_address + subnet.num_addresses - 2
            usable = max(subnet.num_addresses - 2, 0)
            broadcast = subnet.broadcast_address
        else:
            first = subnet.network_address + 1
            last = subnet.network_address + subnet.num_addresses - 1
            usable = subnet.num_addresses
            broadcast = "N/A"

        results.append({
            "Subnet": str(subnet),
            "Network ID": str(subnet.network_address),
            "Broadcast": str(broadcast),
            "First Host": str(first),
            "Last Host": str(last),
            "Usable Hosts": usable
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
