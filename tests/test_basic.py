from .context import sample
import os

# Run a bash script
os.popen('sh /home/oracle/scripts/start.sh')

import subprocess
shellscript = subprocess.Popen(["shellscript.sh"], stdin=subprocess.PIPE)

# Run a bash command
os.popen('sh command')
