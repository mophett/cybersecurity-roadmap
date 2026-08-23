# Networking

This section documents my networking studies, which were split into **two weeks of focused learning and hands-on practice**.

The first week covered the fundamentals of computer networking and how devices communicate. The second week focused on deeper protocol behavior, addressing, ports, sockets, DNS, DHCP, and practical packet analysis.

---

## Week 1 — Networking Fundamentals

### Topics Studied

* What computer networks are and how they work
* LAN, WAN, and the Internet
* Client-server communication
* Network devices:

  * Router
  * Switch
  * Modem
  * Access Point
* MAC addresses
* IP addresses
* IPv4
* IPv6
* Subnets and subnet masks
* Default gateway
* Private and public IP addresses
* Loopback address
* Network interfaces
* Basic routing concepts

### Practical Work

Worked with network configuration and diagnostics using Linux tools:

```bash
ip addr
ip route
ping
```

Learned how to inspect interfaces, identify IP addresses, check routing information, and test connectivity.

---

## Week 2 — Networks II

The second week focused on the protocols and mechanisms that control communication between hosts.

### ARP

Learned:

* What ARP does
* IP-to-MAC address resolution
* ARP requests and replies
* Local network communication
* ARP cache

### ICMP

Learned:

* Purpose of ICMP
* Echo Request / Echo Reply
* How `ping` uses ICMP
* Basic error and diagnostic messages

### TCP

Studied TCP in detail:

* TCP connection establishment
* Three-way handshake

```text
SYN → SYN/ACK → ACK
```

* Source port
* Destination port
* Ephemeral ports
* Sequence numbers
* Acknowledgement numbers
* Retransmission
* TCP flags:

  * SYN
  * ACK
  * FIN
  * RST
  * PSH

Practiced observing TCP traffic with `tcpdump` and `netcat`.

Example:

```bash
nc -l 4444
```

```bash
sudo tcpdump -i lo -nn tcp port 4444
```

This helped connect the theory of TCP with real packets and understand how sequence and acknowledgement numbers change during communication.

### UDP

Learned:

* How UDP differs from TCP
* Connectionless communication
* Datagram-based transmission
* Lack of handshake
* No built-in retransmission
* Use cases for UDP

### DNS

Studied how domain names are translated into IP addresses.

Learned:

* DNS resolver
* DNS queries and responses
* A records
* AAAA records
* UDP port `53`
* TCP port `53`
* Recursive DNS resolution

Practiced with:

```bash
dig example.com
dig AAAA example.com
dig @1.1.1.1 example.com
```

### DHCP

Learned how hosts automatically obtain network configuration.

Studied the DORA process:

```text
Discover → Offer → Request → Acknowledge
```

Learned the role of DHCP in assigning:

* IP address
* Subnet mask
* Default gateway
* DNS servers

### Ports and Sockets

Learned:

* Port range: `0–65535`
* Well-known ports
* Registered ports
* Ephemeral ports
* Source and destination ports
* Sockets

A socket can be understood as an endpoint identified by an IP address and port.

---

## Tools Used

During the two weeks I practiced networking with:

```text
ip
ping
ss
tcpdump
Wireshark
dig
host
nslookup
curl
nc (netcat)
```

---

## What I Can Explain Now

After these two weeks, I can follow the basic path of network communication and explain what happens at different stages.

For example, when accessing a website, I can reason about:

```text
Domain Name
     ↓
DNS Resolution
     ↓
IP Address
     ↓
Routing
     ↓
ARP / Neighbor Resolution
     ↓
TCP Connection
     ↓
Ports / Sockets
     ↓
Application Communication
```

I can also inspect real network traffic and connect packet fields with the underlying protocol behavior.

---

## Progress

**Duration:** 2 weeks
**Focus:** Networking fundamentals + network protocols
**Status:** DONE

The next stage is to continue from networking fundamentals toward **web technologies, security, and practical security analysis**.
