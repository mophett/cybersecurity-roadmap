# IP Classifier

A simple Python tool for classifying IPv4 addresses.

## Features

- Validates IPv4 addresses
- Detects private IPv4 addresses
- Detects public IPv4 addresses
- Checks IPv4 octets from `0` to `255`

## Run

```bash
python ip_classifier.py
cd ~/cybersecurity-roadmap

cat > projects/ip-classifier/README.md <<'EOF'

# IP Classifier

A simple Python tool for classifying IPv4 addresses.

## Features

* Validates IPv4 addresses
* Detects private IPv4 addresses
* Detects public IPv4 addresses
* Checks IPv4 octets from 0 to 255

## Run

```bash
python ip_classifier.py
```

## Example

```text
Enter IP: 192.168.1.10
IPv4
Private address
```

```text
Enter IP: 8.8.8.8
IPv4
Public address
```

