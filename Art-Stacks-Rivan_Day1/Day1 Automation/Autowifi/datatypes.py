import netmiko
from netmiko import ConnectHandler

device_info = { 
 'device_type': 'cisco_iost_telnet',
 'host': '10.12.1.3',
 'password': 'pass',
 'secret': 'pass',
}

config= [
    'interface loopback1',
    'ip address 1.1.1.1 255.255.255.255',
    'end'
]

accesscli = ConnectHandler (**device_info)
accesscli.enable()

accesscli.send_config_set(config)

output = accesscli.send_config_set(config)
print(output)

siib=accesscli.send_command('show ip int br')
print(siib)