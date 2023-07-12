#!/usr/bin/python3
"""
A module initializes the package
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
