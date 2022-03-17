from ipaddress import IPv4Network, ip_address
from random import randint

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        self.ip = ip_address(randint(0x0B000000, 0xDF000000))
        self.mask = randint(8, 24)
        IPv4Network.__init__(self, (self.ip, self.mask), strict=False)

    def get(self):
        return int(self.ip)+int(self.mask)*2**32



lst = []
for i in range(50):
    x = IPv4RandomNetwork()
    if not x.is_private:
        lst.append(x)


def key_value(ip_ad):
    return ip_ad.get()

netlist = sorted(lst, key=key_value)

for i in netlist:
    print(i)



