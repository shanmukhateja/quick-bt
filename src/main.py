from infi.systray import SysTrayIcon
from actions import *

# Constants
TITLE_APP = "Quick BT"
TITLE_BT_ON = "Turn Bluetooth On"
TITLE_BT_OFF = "Turn Bluetooth Off"

ICON_APP = "./icons/bluetooth.ico"

# Context menu actions
menu_options = (
    (TITLE_BT_ON, None, say_hello),
    (TITLE_BT_OFF, None, do_nothing)
)

systray = SysTrayIcon(ICON_APP, TITLE_APP, menu_options)
systray.start()
