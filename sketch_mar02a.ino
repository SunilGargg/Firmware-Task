#include <EEPROM.h>
#include <SoftwareSerial.h>

#define RX_PIN 2
#define TX_PIN 3
#define BAUD_RATE 2400

SoftwareSerial mySerial(RX_PIN, TX_PIN);

void setup() {
  // Initialize serial communication
  Serial.begin(BAUD_RATE);
  mySerial.begin(BAUD_RATE);

  // Read data from serial and store it in EEPROM
  while (mySerial.available()) {
    char receivedChar = mySerial.read();
    if (receivedChar == '\0') { // End of transmission character
      break;
    }
    int address = mySerial.available() - 1; // Use the available EEPROM address
    EEPROM.write(address, receivedChar);
    delay(10); // Optional delay for EEPROM write
  }

  // Transmit data from EEPROM back to serial
  for (int i = 0; i < EEPROM.length(); ++i) {
    char data = EEPROM.read(i);
    mySerial.write(data);
    delay(10); // Optional delay for serial write
  }

  // Transmit end of transmission character
  mySerial.write('\0');

  // Print message to indicate data transmission is complete
  Serial.println("Data transmission complete.");
}

void loop() {
  // Empty loop since all transmission is done in setup
}
