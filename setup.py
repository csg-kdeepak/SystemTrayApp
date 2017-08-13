# -*- coding: utf-8 -*-

from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\kdeepak\Devapps\Anaconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\kdeepak\Devapps\Anaconda3\tcl\tk8.6'

build_exe_options = {"packages": ["pywinauto", "read_ini", "os"],
                     "excludes": ["tkinter", "scipy", "numpy", "json", "PyQt5", "urllib", "email"],
                     "include_files": ["toolsetup.ini", "launch.ico"]}

target = Executable(
    script="SysTray.py",
    base="Win32GUI",
    icon="launch.ico"
    )

setup(
    name="sv_launch",
    version="1.0",
    description="launch sv application",
    author="the author",
    options={"build_exe": build_exe_options},
    executables=[target]
    )

