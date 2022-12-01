#!/usr/bin/env python3

import sys, re, operator, csv

new_ip_dict_list = {}

def get_dict_ips():

    whitelist_ips = ['10.34.0.1','10.34.0.2','10.34.0.3']
    test_ip_dict_list = {}
    with open('/var/log/asterisk/messages','r') as f:
        text = f.readlines()
        for t in text:
            ips = re.findall(r"'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):.\d+'",t.rstrip('\n'))
            for ip in ips:
                if ip not in whitelist_ips:
                    if ip not in test_ip_dict_list:
                        test_ip_dict_list[ip]=1
                    else:
                        test_ip_dict_list[ip]+=1

    test_ip_dict_list = dict(sorted(test_ip_dict_list.items(), key=operator.itemgetter(1),reverse=True))
    return test_ip_dict_list

def help():
    print("""
Usage: 
'filename.py --help' to het more help
'filename.py --ips' will give list of ips with count in decending order.
'filename.py --ips --save' will save to home directory in CSV format named ips.csv
'filename.py --iptables' will give list of ips to DROP in iptables.
'filename.py --iptables --save' will save to home directory in TXT format named iptabes.txt
            """)

def print_ips(sep_del):
    ip_output = ""
    new_ip_dict_list = get_dict_ips()
    for keys,values in new_ip_dict_list.items():
        ip_output+=keys + sep_del + str(values) + '\n'
    return ip_output.rstrip('\n')

def print_iptables():
    iptables_output = ""
    new_ip_dict_list = get_dict_ips()
    for keys,values in new_ip_dict_list.items():
        iptables_output+="-A INPUT -s {}/32 -j DROP\n".format(keys)
    return iptables_output.rstrip('\n')

if len(sys.argv) > 1:
    if len(sys.argv) > 2:
        if sys.argv[1] == '--ips' and sys.argv[2] == '--save':
            header = "ip_address,count\n"
            header+=print_ips(',')
            with open("/root/ips.csv", "w") as text_file:
                text_file.write(header)
            print('file saved to "/root/ips.csv"')
        elif sys.argv[1] == '--iptables' and sys.argv[2] == '--save':
            with open("/root/iptables.txt", "w") as text_file:
                text_file.write(print_iptables())
                print('file saved to "/root/iptables.txt"')
        else:
            help()
    elif len(sys.argv) == 2:
        if sys.argv[1] == '--ips':
            print(print_ips('\t'))
        elif sys.argv[1] == '--iptables':
            print(print_iptables())
        elif sys.argv[1] == '--help':
            help()
        else:
            help()
    else:
        help()
else:
    help()





