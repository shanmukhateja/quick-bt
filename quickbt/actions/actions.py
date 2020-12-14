from subprocess import Popen
import os.path

SCRIPT_PATH = os.path.join('quickbt/bt.ps1')


def turn_on(systray):
    _action()

def turn_off(systray):
    _action('off')


def _action(state = 'on'):
    Popen(['powershell.exe', '-File', SCRIPT_PATH, '-BluetoothStatus', state], shell=True)