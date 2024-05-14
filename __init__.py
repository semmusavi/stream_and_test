"""
Special file __init__.py marks a directory as a Python module.
The file is executed once when any .py file is imported.
//
Python unittest require the presence of (even an empty) file.
"""

# load setup module when executed in parent directory
try:
    __import__('setup')
#
except ImportError:
    pass
