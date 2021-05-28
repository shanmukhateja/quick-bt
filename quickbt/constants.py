import os.path



# Strings
TITLE_APP = "Quick BT"
TITLE_BT_ON = "Turn Bluetooth On"
TITLE_BT_OFF = "Turn Bluetooth Off"

# Set BASE_PATH so project resources are correctly resolved
# TODO: Fix path determine logic, if applicable
if os.path.exists('./quickbt'):
    BASE_PATH = os.path.join('.')
else:
    path, _ = os.path.split(os.path.abspath(__file__))
    BASE_PATH = os.path.join(path, '../..')

# App icon
ICON_APP = os.path.join(BASE_PATH, 'icons/bluetooth.ico')