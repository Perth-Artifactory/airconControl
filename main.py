#!/usr/bin/python3

import subprocess
from datetime import datetime

time_allowed = 3*3600

result = subprocess.run(['kasa', '--host', '10.60.210.98', '--type=plug'], stdout=subprocess.PIPE)
l = result.stdout.decode('utf-8')

for line in l.split("\n"):
    if "On since" in line:
        o = line[11:]
        if o != "None":
            dts = datetime.strptime(o, '%Y-%m-%d %H:%M:%S')
            delta = datetime.now() - dts
            if delta.seconds > time_allowed:
                subprocess.run(['kasa', '--host', '10.60.210.98', '--type=plug', 'off'], stdout=subprocess.PIPE)
