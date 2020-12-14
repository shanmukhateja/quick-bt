import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os", "pkg_resources"],
    "excludes": ["tkinter"],
    "include_msvcr": True,
    "build_exe": "dist",
    "include_files": ["./icons", ("quickbt/bt.ps1", "quickbt/bt.ps1")]
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Quick BT",
      version="0.1",
      description="Toggle BT device from system tray icon",
      options={"build_exe": build_exe_options},
      executables=[Executable("quickbt/__main__.py",targetName="quick-bt", base=base, icon="./icons/bluetooth.ico")])
