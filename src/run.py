'''
run.py

author:

Azusa Kaze
Salmoon Sake
-------------------------------------------------------------------------------

程序的入口，請從這邊開始執行。
'''
import os
os.chdir(os.path.dirname(os.path.dirname(__file__)))

from libs.interface.app import APP

APP()
