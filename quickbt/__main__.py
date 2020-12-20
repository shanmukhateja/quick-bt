from infi.systray import SysTrayIcon
from quickbt.actions.actions import *
from quickbt.constants import *

def init():
  # Context menu actions
  menu_options = (
      (TITLE_BT_ON, None, turn_on),
      (TITLE_BT_OFF, None, turn_off)
  )

  systray = SysTrayIcon(ICON_APP, TITLE_APP, menu_options)
  systray.start()

init()