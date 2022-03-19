from glob import glob
from re import match
from ipaddress import IPv4Interface

# нахождение всех текстовых файлов
files = glob('./config_files/*.txt')

# Создание пустого словаря
dirnet = {'IP': [], 'Interface': [], 'Host': []}

# Функция определения IP, интерфейса и имени хоста
def refinder(info, dir_ip):
    ipfound = match(r"^( ip address) ((?:\d{1,3}\.?){4}) ((?:\d{1,3}\.?){4})", info)
    intfound = match("(?:^(interface) ([0-9a-zA-z]*))", info)
    hostfound = match('(?:^(hostname) ([0-9a-zA-z]*))', info)
    if bool(ipfound):
        dir_ip['IP'].append(str(IPv4Interface(ipfound.group(2) + '/' + ipfound.group(3))))
    if bool(intfound):
        dir_ip['Interface'].append(intfound.group(2))
    if bool(hostfound):
        dir_ip['Host'].append(hostfound.group(2))

# Идем по всем файлам и переносим информацию в словарь
for data in files:
    with open(data, 'r') as file:
        data_line = file.readlines()
        for netdata in data_line:
            refinder(netdata, dirnet)

# удаление повторяющихся элементов в списках
def no_reply(dirlist, key):
    dirlist[key] = list(set(dirlist[key]))


no_reply(dirnet, 'IP')
no_reply(dirnet, 'Interface')
no_reply(dirnet, 'Host')

# вывод информации
def printinfo(d, k):
    if k == 'IP':
        print('\n\tIP List:\n')
        for ip in d[k]:
            print(ip)
    if k == 'Interface':
        print('\n\tInterface:\n')
        for ip in d[k]:
            print(ip)
    if k == 'Host':
        print('\n\tHost:\n')
        for ip in d[k]:
            print(ip)

printinfo(dirnet, 'IP')
printinfo(dirnet, 'Interface')
printinfo(dirnet, 'Host')




