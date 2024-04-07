import serial
import time

def calculate_speed(start_time, total_bits):
    current_time = time.time()
    elapsed_time = current_time - start_time
    speed = total_bits / elapsed_time
    return speed

# Open serial connection to MCU
ser = serial.Serial('COM3', 2400)

# Define the text data to be transmitted
text = """Finance Minister Arun Jaitley Tuesday hit out at former RBI governor Raghuram Rajan for predicting that the next banking crisis would be triggered by MSME lending, saying postmortem is easier than taking action when it was required. Rajan, who had as the chief economist at IMF warned of impending financial crisis of 2008, in a note to a parliamentary committee warned against ambitious credit targets and loan waivers, saying that they could be the sources of next banking crisis. Government should focus on sources of the next crisis, not just the last one.

In particular, government should refrain from setting ambitious credit targets or waiving loans. Credit targets are sometimes achieved by abandoning appropriate due diligence, creating the environment for future NPAs," Rajan said in the note." Both MUDRA loans as well as the Kisan Credit Card, while popular, have to be examined more closely for potential credit risk. Rajan, who was RBI governor for three years till September 2016, is currently."""

# Print the text data being transmitted
print("Data to be transmitted to MCU:", text)

# Start time to calculate transmission speed
start_time = time.time()
total_bits = 0

# Transmit data character by character
for char in text:
    ser.write(char.encode())
    total_bits += 8  # Each character is 8 bits
    time.sleep(0.01)  # Adjust this delay as necessary

print("Data transmitted to MCU.")

received_data = ""
# Receive and print data from MCU
while True:
    if ser.in_waiting > 0:
        received_char = ser.read().decode()
        if received_char == '\0':  # End of transmission character
            break
        received_data += received_char
    else:
        break

# Print received string
print("\nData received from MCU:", received_data)

# Close serial connection
ser.close()
