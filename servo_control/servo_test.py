import serial
import time

PORT = "COM3"   # 🔴 change this
BAUD = 9600

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

print("\nCommands:")
print("  0,90       → move servo")
print("  on / off   → relay control")
print("  all a b c  → move 3 servos")
print("  exit       → quit\n")


def send(cmd):
    ser.write((cmd + "\n").encode())
    time.sleep(0.1)

    while ser.in_waiting:
        print("Arduino:", ser.readline().decode().strip())


while True:
    user = input(">> ")

    if user == "exit":
        break

    # 🔹 relay commands
    elif user in ["on", "off"]:
        send(user)

    # 🔹 single servo
    elif "," in user:
        send(user)

    # 🔹 move 3 servos together
    elif user.startswith("all"):
        try:
            _, a0, a1, a2 = user.split()

            send(f"0,{a0}")
            send(f"1,{a1}")
            send(f"2,{a2}")

        except:
            print("Use: all 90 40 30")

    else:
        print("Invalid command")

ser.close()