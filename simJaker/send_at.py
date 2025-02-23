import serial
import time

# Configure the serial connection
ser = serial.Serial('COM8', 115200, timeout=1)  # Replace COM3 with your port

def send_at_command(command, wait=1):
    """Send an AT command and return the response."""
    ser.write((command + '\r').encode())  # Windows uses \r for line endings
    time.sleep(wait)
    response = ser.read_all().decode(errors='ignore')  # Handle decoding issues gracefully
    print(f"Command: {command}\nResponse: {response}")
    return response

def send_sms_pdu(pdu):
    """Send an SMS in PDU mode."""
    # Step 1: Start the message sending process
    response = send_at_command('AT+CMGS=69', wait=2)  # Length of PDU is 23
    if '>' in response:
        # Step 2: Send the PDU followed by Ctrl+Z
        ser.write((pdu).encode())  # Send PDU
        ser.write(b'\x1A')  # Ctrl+Z to end the PDU
        time.sleep(5)  # Wait for the modem to process the message
        final_response = ser.read_all().decode(errors='ignore')
        print(f"Final Response: {final_response}")
        return final_response
    else:
        print("Error: Modem did not prompt for PDU.")
        return None

# Step 4: Initialize the modem
send_at_command('AT')
send_at_command('AT+CPIN?')
send_at_command('ATE1')
send_at_command('AT+CMEE=2')
send_at_command('AT+CSCA?')
send_at_command('AT+CMGF=0')

# Step 5: Send the SMS in PDU mode
pdu_message = '0041000C911253066008367FF63802700000330D0000000050534800000000000042230121020744382E3130353105160604313035312D0C1003830607911263656990312B00'

response = send_sms_pdu(pdu_message)

if response and '+CMGS' in response:
    print("SMS sent successfully!")
elif response and '+CMS ERROR' in response:
    print("SMS sending failed with error:", response)
else:
    print("Unexpected response:", response)