import sys
import socket 
import subprocess
import re
import logging
import ipaddress

logging.basicConfig(level=logging.INFO)

if len(sys.argv) < 2:
    print("Usage: python analyzer.py <logfile>")
    sys.exit(1)

filename = sys.argv[1]

logging.info(f"Analyzing {filename}")

counts = {
    "INFO": 0,
    "ERROR": 0,
    "WARNING": 0
}

with open(filename, "r") as file:

    for line in file:

        for level in counts:
            if level in line:
                counts[level] += 1

        ips = re.findall(r"\d+\.\d+\.\d+\.\d+", line)

        for ip in ips:

            address = ipaddress.ip_address(ip)

            if address.is_private:
                print(f"PRIVATE IP: {ip}")
            else:
                print(f"PUBLIC IP: {ip}")

print("\nLog statistics:")

for level, count in counts.items():
    print(f"{level}: {count}")

hostname = input("\nEnter domain: ")

try:
    ip = socket.gethostbyname(hostname)
    print(f"{hostname} -> {ip}")
except socket.gaierror:
    print("Could not resolve domain")

print("\nNetwork information:")

result = subprocess.run(
    ["ip", "addr"],
    capture_output=True,
    text=True
)

print(result.stdout)