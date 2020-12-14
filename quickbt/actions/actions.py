from subprocess import Popen
import os.path

SCRIPT_PATH = os.path.join('quickbt/bt.ps1')


def turn_on(systray):
    Popen(args=['powershell.exe', '-File', SCRIPT_PATH, '-BluetoothStatus', 'on'])

def turn_off(systray):
    Popen(['powershell.exe', '-File', SCRIPT_PATH, '-BluetoothStatus', 'off'])
