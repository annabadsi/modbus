# Modbus RTU (RS-485) and TCP example

## Setup
- start each ([modbus-master](https://github.com/annabadsi/modbus/tree/master/modbus-master) and [modbus-slave](https://github.com/annabadsi/modbus/tree/master/modbus-slave)) on one Raspberry PI
- the [modbus-slave](https://github.com/annabadsi/modbus/tree/master/modbus-slave) has to be connected to an LED
- browse on your laptop (same network as the modbus-master) the webserver which were started by the modbus-master

### Setup RTU
- the Raspberry Pi UARTs may need to be configured, see [documentation](https://www.raspberrypi.org/documentation/configuration/uart.md), if so then restart afterwards

### Setup TCP
- both Raspberry PI must be connected with the same network
- to allow Port 22 use `sudo ufw allow 22` and reboot

## Structure

![structure1](https://raw.githubusercontent.com/annabadsi/modbus/master/img/structure1.PNG)

- 2x [Raspberry PI 3 B+](https://www.reichelt.de/raspberry-pi-3-b-4x-1-4-ghz-1-gb-ram-wlan-bt-raspberry-pi-3b-p217696.html?PROVID=2788&gclid=CjwKCAjwxrzoBRBBEiwAbtX1n1o4QIg8uV4L9559LD1cWGnWN1Uzz1JDwLJy6BZEkQ_UwnEOCxNHvxoCBtoQAvD_BwE&&r=1)
- 2x [RS-485 adapter](https://www.reichelt.de/raspberry-pi-shield-rs485-schnittstelle-rpi-rs485-p162304.html)
- 2x 120 Ohm resistance
- serial cable
- breadboard & led

![structure2](https://raw.githubusercontent.com/annabadsi/modbus/master/img/structure2.jpg)
