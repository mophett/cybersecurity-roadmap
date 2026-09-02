def get_port_service(port):
    services = {
        22: "SSH",
        80: "HTTP",
        443: "HTTPS"
    }

    return services.get(port, "UNKNOWN")


def parse_ports(ports):
    for port in ports:
        service = get_port_service(port)
        print("Port:", port, "Service:", service)


ports = [22, 80, 443, 8080]

parse_ports(ports)