```bash
#!/bin/bash

echo "=== System Information ==="

echo "Hostname: $(hostname)"
echo "Kernel: $(uname -r)"
echo "User: $USER"
echo "Date: $(date)"

echo
echo "=== Disk Usage ==="

df -h /

echo
echo "=== Memory Usage ==="

free -h

echo
echo "=== Uptime ==="

uptime

echo
echo "=== Network ==="

hostname -I

echo
echo "=== Finished ==="
```
