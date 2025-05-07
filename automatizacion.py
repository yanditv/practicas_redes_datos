from netmiko import ConnectHandler

# Define los parámetros del dispositivo
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'tu_password',
}

# Conexión SSH
net_connect = ConnectHandler(**cisco_device)

# Ejecuta un comando
output = net_connect.send_command('show ip interface brief')
print(output)

# Cierra la conexión
net_connect.disconnect()
