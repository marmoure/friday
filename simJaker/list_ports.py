import serial.tools.list_ports
import time


def get_modem_at_port():
    ports = serial.tools.list_ports.comports()
    modem = []
    for port in ports:
        print(f"Device: {port.device}")
        print(f"Name: {port.name}")
        print(f"Description: {port.description}")
        print("-" * 40)
        if "HUAWEI" in port.description:
            modem.append(port.device)
    for port in modem:
        print(f"Modem: {port}")
        if check_at_port(port):
            return port

def send_at_command(ser, command):
    ser.write((command + '\r').encode())
    time.sleep(1)  # Allow time for the modem to respond
    response = ser.read_all().decode()
    print(response)
    return response

def check_at_port(port):
    try:
        ser = serial.Serial(port, 9600, timeout=1)
        if send_at_command(ser, 'AT').strip() == "OK":
            ser.close()
            return True
    except serial.SerialException:
        return False
if __name__ == "__main__":
    port = get_modem_at_port()
    print(f"Modem port: {port}")