from glob import glob
files = glob('./config_files/*.txt')
list_ip = []
for data in files:
    with open(data, 'r') as file_ip:
        ip_line = file_ip.readlines()
        for ip in ip_line:
            if ip.find('ip address') == 1:
                list_ip.append(ip.strip('ipadres:\n '))



list_ip = list(set(list_ip))
for ip in list_ip:
    print(ip)