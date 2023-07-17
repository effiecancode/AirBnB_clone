#!/usr/bin/python3
"""create an instance of the FileStorage module"""
# import os
# import sys
# fpath = os.path.join(os.path.dirname(__file__), 'engine')
# sys.path.append(fpath)
from engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
