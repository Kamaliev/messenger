import os


command = 'python -m nuitka --standalone --onefile --disable-console --enable-plugin=pyqt5 --windows-icon-from-ico=icon.png run.py'

os.system(command)