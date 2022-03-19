from glob import glob
from re import match
from ipaddress import IPv4Interface
from openpyxl import Workbook

# нахождение всех текстовых файлов
files = glob('./config_files/*.txt')

# Создание пустого словаря
listnet = []

# Функция определения IP, интерфейса и имени хоста
def refinder(info, lstnet):
    ipfound = match(r"^( ip address) ((?:\d{1,3}\.?){4}) ((?:\d{1,3}\.?){4})", info)
    if bool(ipfound):
        lstnet.append(str(IPv4Interface(ipfound.group(2) + '/' + ipfound.group(3))))

# Идем по всем файлам и переносим информацию в словарь
for data in files:
    with open(data, 'r') as file:
        data_line = file.readlines()
        for netdata in data_line:
            refinder(netdata, listnet)

# удаление повторяющихся элементов в списках
listnet = list(set(listnet))
# разделение на адреса и маски
for i in range(len(listnet)):
    listnet[i] = listnet[i].split('/')


# создание Excel таблицы
ip_file = Workbook()
ip_sheet = ip_file.create_sheet(title='List IP address', index=0)
ip_sheet['A1'] = 'IP'
ip_sheet['B1'] = 'Mask'
num_str = 2 # счетчик строк
for ind in range(len(listnet)):
    ip_sheet[f'A{num_str}'] = listnet[ind][0]
    ip_sheet[f'B{num_str}'] = listnet[ind][1]
    num_str += 1

ip_file.save('TableIP.xlsx')