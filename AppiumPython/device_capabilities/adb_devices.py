import os
import socket
import subprocess
import time


def get_adb_devices():
    # Run the adb devices command
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)

    # Check if the command was successful
    if result.returncode == 0:
        # Split the output into lines, filter out empty lines, and skip the first line (header)
        devices = [line for line in result.stdout.splitlines()[1:] if line.strip()]
        return devices
    else:
        print("Error executing adb command:", result.stderr)
        return []


def save_devices_to_file(filename):
    devices = get_adb_devices()
    if devices:
        with open("..//data//adb_devices.txt", 'w') as file:
            for device in devices:
                file.write(device + '\n')
        print(f"Device list saved to {filename}.")
    else:
        print("No devices found or an error occurred.")

def is_appium_running(port=4724):
    """Check if the Appium server is running on the specified port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex(('127.0.0.1', port)) == 0

def start_appium_server(port=4724):
    """Start the Appium server on the specified port in a new command prompt window in the user's home directory."""
    if is_appium_running(port):
        print(f"Appium server is already running on port {port}.")
        return

    # Automatically get the user's home directory
    user_home_directory = os.path.expanduser("~")

    # Create the command to run Appium in the new cmd window
    appium_command = f'start cmd /c "cd {user_home_directory} && appium -p {port}"'

    # Start the Appium server in a new command prompt window
    subprocess.Popen(appium_command, shell=True)

    # Allow some time for the server to start
    time.sleep(5)
    print(f"Appium server started on port {port}.")




