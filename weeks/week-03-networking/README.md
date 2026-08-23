# Week 03 — Networking I

## Overview

This week focused on the fundamentals of computer networking and how devices communicate with each other.

The goal was to understand how devices are connected, how they are identified, how traffic moves between networks, and how Linux represents and manages network configuration.

---

## Topics Studied

### Network Fundamentals

* Computer networks
* LAN
* WAN
* Internet
* Client-server communication
* Network interfaces
* NIC
* Ethernet

### Network Devices

* Router
* Switch
* Modem
* Access Point

### Addressing

* MAC addresses
* IP addresses
* IPv4
* IPv6
* Private IP addresses
* Public IP addresses
* Loopback
* Network interfaces

### Subnetting and CIDR

* Subnets
* Subnet masks
* CIDR
* `/8`
* `/16`
* `/24`
* `/32`
* Number of addresses in a subnet
* Binary representation of IPv4 addresses
* Binary AND

### Routing and NAT

* Default gateway
* Routing
* Routing tables
* How packets move between networks
* NAT

### Private IPv4 Ranges

Studied the standard private IPv4 ranges:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

---

## Linux Networking Tools

Practiced using Linux networking utilities to inspect the system and troubleshoot connectivity.

### `ip addr`

Used to inspect network interfaces and assigned IP addresses.

### `ip link`

Used to inspect network interfaces and their link state.

### `ip route`

Used to inspect the routing table and default gateway.

### `ip neigh`

Used to inspect the local neighbor table.

### `ping`

Used to test network connectivity.

### `traceroute`

Used to examine the path traffic takes through a network.

### `ss`

Used to inspect network sockets and connections.

---

## Practical Work

I practiced analyzing my own local network and identifying the role of each component.

A simplified communication path was represented as:

```text
Laptop
   ↓
Router
   ↓
ISP
   ↓
Internet
```

I used Linux networking tools to inspect the local configuration and understand how the device connects to the local network, gateway, ISP, and Internet.

---

## Subnetting Practice

I practiced working with:

* binary representation of IPv4 addresses;
* subnet masks;
* CIDR notation;
* powers of two;
* binary AND;
* calculating the number of addresses in a subnet.

The goal was to understand what a subnet represents and how the subnet mask determines the network and host portions of an IPv4 address.

---

## What I Can Explain

After this week, I can explain:

* what a LAN and WAN are;
* the role of a NIC;
* the difference between a MAC address and an IP address;
* the difference between IPv4 and IPv6;
* what private and public IP addresses are;
* what a loopback address is;
* what a subnet is;
* what CIDR notation represents;
* what `/8`, `/16`, `/24`, and `/32` mean;
* how subnet masks are used;
* how binary AND relates to subnetting;
* what a default gateway does;
* what a routing table contains;
* how NAT fits into typical home networking;
* how a Linux system represents its network configuration.

A simplified view of the network path is:

```text
Device
  ↓
Local Network
  ↓
Router / Gateway
  ↓
ISP
  ↓
Internet
```

---

## Tools Used

```text
ip addr
ip link
ip route
ip neigh
ping
traceroute
ss
```

---

## Progress

**Duration:** 1 week
**Focus:** Networking fundamentals, addressing, subnetting, routing, and Linux network configuration
**Status:** DONE

The next stage is to move from networking fundamentals to protocol-level communication and packet analysis.
