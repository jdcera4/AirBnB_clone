#!/usr/bin/python3
''' module for models/__init__ '''
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
