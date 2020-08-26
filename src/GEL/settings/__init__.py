# from .base import *

live = False

try:
    from .development import *

except ImportError:
    live = True

if live:
    from .production import *
