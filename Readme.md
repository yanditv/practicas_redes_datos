# Práctica: Automatización de Configuración Básica de un Router Cisco con Netmiko

## Objetivo

El estudiante aprenderá a:

- Establecer una conexión SSH automatizada a un router Cisco.
- Ejecutar comandos de diagnóstico (`show`).
- Enviar configuraciones básicas al dispositivo.
- Documentar los resultados obtenidos en un archivo.

---

## Requisitos

- Python 3 instalado
- Biblioteca Netmiko (`pip install netmiko`)
- Acceso a un router Cisco real o virtual (por ejemplo, con GNS3, Eve-NG o Cisco Packet Tracer con soporte SSH)
- Usuario y contraseña configurados en el router para acceso SSH

---

## Actividades

### 1. Conexión SSH

Crear un script en Python que se conecte por SSH al router y obtenga la salida del comando:

```bash
show version
```

### 2. Diagnóstico de interfaces

Agregar código al script para ejecutar el comando:

```bash
show ip interface brief
```

### 3. Enviar configuración

Automatizar la configuración de una nueva interfaz loopback con los siguientes comandos:

```
configure terminal
interface Loopback0
ip address 10.10.10.1 255.255.255.0
description Loopback configurada con Netmiko
end
```

### 4. Guardar configuración

Ejecutar el comando:

```bash
write memory
```

### 5. Exportar resultados

Guardar la salida de los comandos en un archivo `.txt` que incluya la fecha y hora de ejecución.

---

## Preguntas a responder

- ¿Qué ventajas ofrece Netmiko frente a configurar manualmente cada dispositivo?
- ¿Qué medidas de seguridad debes considerar al usar automatización por SSH?
- ¿Cómo podrías escalar este script para automatizar múltiples dispositivos?

---

## Entregables

- Código fuente en Python (.py)
- Captura de pantalla del resultado en consola
- Archivo `.txt` con la salida de comandos
- Breve reflexión (1 párrafo) sobre lo aprendido

---

## Recursos recomendados

- [Documentación oficial de Netmiko](https://github.com/ktbyers/netmiko)
