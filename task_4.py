nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat_modify = nat.replace('Fast', 'Gigabit')
print(nat_modify)


mac = "AAAA:BBBB:CCCC"
mac_modify = mac.replace(':', '.')
print(mac_modify)

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
config_list = config.split()
vlans = config_list[-1]
vlans = vlans.split(',')
print(vlans)

vlans_list = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
vlans_set = set(vlans_list)
print(sorted(vlans_set))

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
command1 = command1.split()
command2 = command2.split()
com1_list = command1[-1].split(",")
com2_list = command2[-1].split(',')
com1_set = set(com1_list)
com2_set = set(com2_list)
result = com1_set.intersection(com2_set)
print(sorted(result))

mac_task7 = "AAAA:BBBB:CCCC"
mac_t = mac_task7.split(':')
mac_t1 = ''.join(mac_t)
binary_mac = bin(int(mac_t1, 16))
print(binary_mac)

ip = "192.168.3.1"
ip_mod = ip.split('.')
print(f'''
{ip_mod[0]:10}{ip_mod[1]:10}{ip_mod[2]:10}{ip_mod[3]:10}
{int(ip_mod[0]):12b}{int(ip_mod[1]):12b}{int(ip_mod[2]):12b}{int(ip_mod[3]):12b}
''')

