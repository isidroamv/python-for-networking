from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'ip':   '1.2.3.4',
    'username': 'user',
    'password': 'pass',
    'port' : 22,          # optional, defaults to 22
    'verbose': True,       # optional, defaults to False
}


net_connect = ConnectHandler(**cisco_881)

output = net_connect.send_config_set(['hostname host-prueba-sw', 'username test_course privilege 1 secret test'])
print output
