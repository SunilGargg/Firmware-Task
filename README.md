# Firmware-Task
The repo contains implementation of the firmware task https://nymblelabs.notion.site/Firmware-Task-5177116a6cb94643871d8cf39c1f345f 

The goal of the project is to transmit a piece of text between a PC and an MCU using UART communication, while measuring the speed of the data transmission in bits per second (bps). 

- **sketch_mar02a.ino**: Firmware for the Arduino Uno microcontroller. It receives a text message sent from the PC via UART, stores the data in EEPROM, and then transmits the message back to the PC via UART after the reception is complete. To run this, set up an Arduino project and configure the required UART communication settings.

- **data.py**: The PC-side code written using the `pyserial` library. It handles sending the text message to the MCU and receiving it back. The data transfer speed is printed in real-time during both transmission and reception.

*Note: The basic UART transmission and reception functionality are complete, but additional EEPROM functionality and optimizations can be added as needed.*
