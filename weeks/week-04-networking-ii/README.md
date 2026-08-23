# Networking II — Protocols and Packet Analysis

This week focused on the protocols and mechanisms responsible for communication between hosts.

The goal was to move from understanding network structure to understanding what actually happens inside network traffic.

The week included practical packet capture and analysis using `tcpdump` and Wireshark.

---

## Topics Studied

* ARP
* ICMP
* TCP
* UDP
* DNS
* DHCP
* Ports
* Sockets

---

## ARP

Studied how ARP resolves an IPv4 address to a MAC address on a local network.

Learned:

* Purpose of ARP
* IP-to-MAC address resolution
* ARP requests
* ARP replies
* Local network communication
* ARP cache

The basic exchange can be represented as:

```text
ARP Request
     ↓
ARP Reply
```

The practical capture allowed me to observe this exchange directly in Wireshark.

---

## ICMP

Studied the purpose of ICMP and its use in network diagnostics.

Focused on:

* Echo Request
* Echo Reply
* ICMP identifiers
* Sequence numbers
* TTL
* How `ping` uses ICMP

The basic exchange is:

```text
Echo Request
     ↓
Echo Reply
```

ICMP traffic was captured and analyzed in Wireshark.

---

## TCP

TCP was one of the main areas of practical analysis.

Studied:

* TCP connection establishment
* Three-way handshake
* Source ports
* Destination ports
* Ephemeral ports
* Sequence numbers
* Acknowledgement numbers
* TCP flags
* Connection termination

### Three-Way Handshake

```text
SYN
 ↓
SYN/ACK
 ↓
ACK
```

### TCP Flags

Studied:

```text
SYN
ACK
FIN
RST
PSH
```

I practiced observing TCP traffic with `tcpdump` and `netcat`.

Example:

```bash
nc -l 4444
```

```bash
sudo tcpdump -i lo -nn tcp port 4444
```

This allowed me to connect the TCP concepts studied theoretically with actual packets and observe fields such as ports, sequence numbers, and acknowledgement numbers.

---

## UDP

Studied UDP and how it differs from TCP.

Learned:

* Connectionless communication
* Datagram-based transmission
* Absence of a TCP-style handshake
* Lack of built-in retransmission
* Common use cases for UDP

UDP traffic was also observed during practical packet analysis.

---

## DNS

Studied how domain names are resolved into IP addresses.

Learned:

* DNS resolver
* DNS queries
* DNS responses
* A records
* AAAA records
* PTR queries
* UDP port `53`
* TCP port `53`
* Recursive DNS resolution

Practiced generating DNS queries with:

```bash
dig example.com
dig AAAA example.com
dig @1.1.1.1 example.com
```

DNS queries and responses were then observed in packet captures.

---

## DHCP

Studied how hosts can automatically obtain network configuration.

Focused on the DORA process:

```text
Discover
   ↓
Offer
   ↓
Request
   ↓
Acknowledge
```

Learned the role of DHCP in providing network configuration such as:

* IP address
* Subnet configuration
* Default gateway
* DNS server information

DHCPv6 traffic was also observed during packet analysis.

---

## Ports and Sockets

Studied how ports identify application endpoints on a host.

Learned:

* Port range `0–65535`
* Well-known ports
* Registered ports
* Ephemeral ports
* Source ports
* Destination ports
* Sockets

A socket can be understood as a communication endpoint associated with an IP address and port.

---

## Practical Packet Analysis

Traffic was captured locally and analyzed using `tcpdump` and Wireshark.

The main goal was to identify protocol behavior directly from captured packets.

I practiced finding:

* ARP requests and replies
* DNS queries and responses
* ICMP Echo Request / Echo Reply
* TCP handshakes
* TCP connections
* TCP flags
* Source and destination ports
* UDP traffic
* DHCPv6
* mDNS
* SSDP

---

## Wireshark Analysis

Wireshark was used to inspect individual packets and isolate protocols using display filters.

The analysis focused on understanding the relationship between:

```text
Packet
  ↓
Protocol
  ↓
Header Fields
  ↓
Communication
```

Rather than treating Wireshark as the main subject, it was used as a tool for understanding the underlying network protocols.

---

## Practical Project

The packet analysis performed during this week was organized into a separate project:

`projects/network-traffic-analysis/`

The project contains analyzed examples of:

* ARP
* DNS
* ICMP
* TCP
* UDP

with screenshots from the packet captures.

---

## Tools Used

```text
tcpdump
Wireshark
dig
host
nslookup
curl
nc
```

---

## What I Can Explain

After this week, I can explain:

* how ARP resolves local IPv4 addresses;
* how ICMP Echo Request and Reply work;
* how TCP establishes a connection;
* what SYN, ACK, FIN, RST, and PSH represent;
* what source and destination ports are;
* what ephemeral ports are;
* what sequence and acknowledgement numbers represent;
* how UDP differs from TCP;
* how DNS queries and responses work;
* what A, AAAA, and PTR records are;
* how DHCP uses the DORA process;
* what ports and sockets represent;
* how to identify these protocols in a packet capture.

A simplified view of the communication process is:

```text
Application
    ↓
Ports / Sockets
    ↓
TCP / UDP
    ↓
IP
    ↓
ARP / Neighbor Resolution
    ↓
Ethernet
```

---

## Progress

**Duration:** 1 week
**Focus:** Network protocols, ports, sockets, packet capture, and analysis
**Status:** DONE

The next stage is to move from networking into programming and begin working with Python.
