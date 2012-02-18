#! /usr/bin/python


"""
expose os.path.abspath
to bash
"""


import sys # sys.argv
import os # os.system


relpath = sys.argv[1]

print os.path.abspath( relpath )


