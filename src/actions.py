from subprocess import Popen
import os.path
import pathlib

SCRIPT_PATH = os.path.join('src/bt.ps1')


def turn_on(systray):
    Popen(args=['powershell.exe', '-File', SCRIPT_PATH, '-BluetoothStatus', 'on'], shell=True)

def turn_off(systray):
    Popen(['powershell.exe', '-File', SCRIPT_PATH, '-BluetoothStatus', 'off'])
