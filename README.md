# Simple Network Scanner

Simple Python CLI tool for scanning a local network and detecting active hosts using ping.

## Features:

- Scans a selected IP range
- Detects active hosts in the network
- Displays scan progress
- Shows total scan time
- Prints a summary of active devices

## Requirements 

- Python 3.x
- Works on Windows (uses ping command)

## Usage

Run the script:
```bash
python network-scanner.py
```
Then provide:
- IPv4 base (e.g. 192.168.0.)
- Starting range (e.g. 1)
- Ending range (e.g. 20)

## Example 

Scanning 192.168.0.1...
[+] 192.168.0.1 is active
Scanning 192.168.0.2...
[-] 192.168.0.2 is inactive

======== Scan complete ========
Active hosts: 1
Time elapsed: 3.21 seconds

[+] 192.168.0.1

## Notes
- The script uses system ping, so results depend on network configuration
- Some devices may block ping requests

## Author

Radoslaw Cis
