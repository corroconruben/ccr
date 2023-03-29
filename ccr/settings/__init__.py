from .base import *
import socket

hostname = socket.gethostname()
if hostname =='ccr':
   from .prod import *
else:
   from .dev import *