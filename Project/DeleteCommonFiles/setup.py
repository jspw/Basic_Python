#setup.py
from cx_Freeze import setup, Executable
setup(
    name = "Delete Common Files",
    version = "1.0.0",
    options = {"build_exe": {
        'packages': ["os","sys","ctypes","win32con"],
        'include_files': ['del.jpg'],
        'include_msvcr': True,
    }},
    executables = [Executable("DelFiles.py",base="Win32GUI")]
    )