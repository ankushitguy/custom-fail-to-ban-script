# custom-fail-to-ban-script

This script will filter through the message log of asterisk and filter out the "register failed attempt" IP's with sorted according to most hits on server.
also it generate iptables commands to block them.



```sh
# custom-fail-to-ban-script
Usage:
'filename.py --help' to het more help
'filename.py --ips' will give list of ips with count in decending order.
'filename.py --ips --save' will save to home directory in CSV format named ips.csv
'filename.py --iptables' will give list of ips to DROP in iptables.
'filename.py --iptables --save' will save to home directory in TXT format named iptabes.txt
```
