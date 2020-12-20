from subprocess import Popen
from quickbt.constants import PS_SCRIPT_PATH


def turn_on(systray):
    _action()

def turn_off(systray):
    _action('off')


def _action(state = 'on'):
    Popen(['powershell.exe','-WindowStyle','Hidden', '-File', PS_SCRIPT_PATH, '-BluetoothStatus', state], shell=True)