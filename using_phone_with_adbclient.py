from ppadb.client import Client as AdbClient
from time import sleep

# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()

if len(devices) == 0:
    print('[ERROR] No devices.')
    quit()

device = devices[0]

print(f"Connected to {device}")

device.shell("input keyevent 26")
# Home (To turn the phone on and access the lock screen)
device.shell("input keyevent 3")
# PIN: 1 2 3 4 Enter
device.shell(
    "input keyevent 145 keyevent 146 keyevent 147 keyevent 148 && input keyevent 160")
# If to unlock your phone you have to type a PIN, do not use the "key_X" (X = Your character) and "key_enter", insted, use the "key_numpad_X" (X = your character) and "key_numpad_enter" to enter your PIN.
device.shell("input keyevent 3")  # Home
device.shell("input touchscreen swipe 500 200 200 200")
sleep(0.5)
device.shell("input touchscreen swipe 200 200 500 200")
sleep(0.5)
device.shell("input touchscreen tap 200 200")
sleep(0.5)
# "%s" to use space
device.shell('input text "gabriel%stressoldi%simages" && input keyevent 66')
sleep(5)
device.shell("input keyevent 27")  # Camera
sleep(2)
device.shell("input keyevent 3")  # Home

# To find adb key events, just search "adb key events" on the internet

# When connected to your phone, you can use adb key events and more from the terminal. Python file not needed.
