# Laboratorio: Monitorización de dispositivos Cisco con Python y Prometheus

## Objetivos

- Conectarse a dispositivos Cisco usando SSH desde Python.
- Obtener métricas de uso de CPU y estado de interfaces.
- Exponer estas métricas en un endpoint HTTP usando Prometheus.
- Aprender a usar archivos YAML para configuración de dispositivos.
- Visualizar las métricas desde el navegador o integrarlas con Prometheus.

...

## Requisitos

- 2 routers Cisco (físicos o simulados con GNS3, EVE-NG, etc.).
- Acceso SSH habilitado en los routers.
- Python 3 instalado.
- Librerías necesarias:

```bash
pip install netmiko pyyaml prometheus_client
```

## Estructura del proyecto

```sh
laboratorio-monitor-cisco/
├── exporter.py         # Script Python que expone métricas
├── devices.yaml        # Configuración de los routers
└── README.md           # Instrucciones del laboratorio
```

## Configuración de dispositivos (devices.yaml)

```sh
devices:
  - name: r1
    host: 192.168.1.1
    username: admin
    password: cisco
    secret: cisco
    device_type: cisco_ios

  - name: r2
    host: 192.168.1.2
    username: admin
    password: cisco
    secret: cisco
    device_type: cisco_ios

```

## Archivo exporter.py

```py
from prometheus_client import start_http_server, Gauge
from netmiko import ConnectHandler
import yaml
import time

# Cargar configuración desde YAML
def cargar_dispositivos():
    with open("devices.yaml") as f:
        return yaml.safe_load(f)["devices"]

# Definir métricas
uso_cpu = Gauge("uso_cpu_dispositivo", "Uso de CPU (%)", ["dispositivo"])
interfaces_arriba = Gauge("interfaces_arriba_dispositivo", "Número de interfaces en estado UP", ["dispositivo"])

# Recolectar métricas desde un router
def recolectar_metricas(dispositivo):
    try:
        conexion = ConnectHandler(**dispositivo)
        conexion.enable()

        nombre = dispositivo["name"]

        # Obtener uso de CPU
        salida_cpu = conexion.send_command("show processes cpu | include CPU utilization")
        porcentaje_cpu = int(salida_cpu.split(":")[1].split("%")[0].strip())
        uso_cpu.labels(dispositivo=nombre).set(porcentaje_cpu)

        # Contar interfaces UP
        salida_interfaces = conexion.send_command("show ip interface brief")
        cantidad_up = sum(
            1 for linea in salida_interfaces.splitlines()
            if "up" in linea.lower() and "administratively down" not in linea.lower()
        )
        interfaces_arriba.labels(dispositivo=nombre).set(cantidad_up)

        conexion.disconnect()
        print(f"[✔] Métricas actualizadas para {nombre}")
    except Exception as e:
        print(f"[✘] Error al consultar el dispositivo {dispositivo['name']}: {e}")

# Bucle principal
def main():
    dispositivos = cargar_dispositivos()
    start_http_server(8000)
    print("✅ Exportador iniciado en http://localhost:8000/metrics")

    while True:
        for dispositivo in dispositivos:
            recolectar_metricas(dispositivo)
        time.sleep(30)

if __name__ == "__main__":
    main()

```

## Instrucciones

Instrucciones

1. Inicia los routers y asegúrate de que respondan por SSH.
2. Coloca los archivos devices.yaml y exporter.py en el mismo directorio.
3. Ejecuta el exporter:

```sh
python exporter.py
```

4. Abre tu navegador en: http://localhost:8000/metrics
5. Verifica que aparecen métricas como:

```sh
# HELP uso_cpu_dispositivo Uso de CPU (%)
# TYPE uso_cpu_dispositivo gauge
uso_cpu_dispositivo{dispositivo="r1"} 5
interfaces_arriba_dispositivo{dispositivo="r1"} 10
```

## Desarrollar

- Agrega un nuevo router en devices.yaml (por ejemplo, r3).
- Modifica el script para recolectar una métrica adicional (ej. memoria).
- Usa curl localhost:8000/metrics desde terminal para obtener las métricas.
- Explica el funcionamiento del archivo YAML y cómo se utiliza en Python.
- (Opcional) Integrar Grafana con Prometheus para visualizar las métricas.

## Responder

1. ¿Qué otras métricas útiles se podrían monitorear?
2. ¿Qué ventajas ofrece Prometheus sobre herramientas?
3. ¿Qué diferencias hay entre SNMP y este tipo de monitoreo?

## Recursos adicionales

- [Documentación oficial de Netmiko](https://github.com/ktbyers/netmiko)

- [Prometheus client for Python](https://github.com/prometheus/client_python)
- [Documentacion de Prometeus Client for Python](https://prometheus.github.io/client_python/)
