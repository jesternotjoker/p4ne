from pysnmp.hlapi import *

snmp_ver = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_interfaces = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')


result = getCmd(SnmpEngine(),
	CommunityData('public', mpModel=0),
	UdpTransportTarget(('10.31.70.107', 161)),
	ContextData(),
	ObjectType(ObjectIdentity(snmp_ver)))

result2 = nextCmd(SnmpEngine(),
	CommunityData('public', mpModel=0),
	UdpTransportTarget(('10.31.70.107', 161)),
	ContextData(),
	ObjectType(ObjectIdentity(snmp_interfaces)),
    lexicographicMode=False)

for r in result:
    for s in r[3]:
        print(s)

print('')

for r in result2:
    for s in r[3]:
        print(s)
