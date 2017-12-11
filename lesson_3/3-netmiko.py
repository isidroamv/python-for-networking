from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'ip':   '0.0.0.0',
    'username': 'user',
    'password': 'pass',
    'port' : 22,          # optional, defaults to 22
    'verbose': True,       # optional, defaults to False
}


net_connect = ConnectHandler(**cisco_881)
output = net_connect.send_command('show run | include ip route')
print output
#lines_splited =output.splitlines()

#for line in lines_splited:
#    if "version" in line:
#        print("La version", line)
#        break

