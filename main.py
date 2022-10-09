#! /usr/bin/env python3

#===== imports =====#
import datetime
import os
import subprocess
import sys

#===== consts =====#
DIR = os.path.dirname(os.path.realpath(__file__))
REQUESTS_PATH = 'requests/stay-on-until.txt'
STATE_PATH = 'stay-on-until.txt'

NOW = datetime.datetime.now(tz=datetime.timezone.utc)

#===== setup =====#
os.chdir(DIR)

#===== helpers =====#
def read_time_from(path):
    if not os.path.exist(path):
        return None
    with open(path) as f:
        s = f.read()
    return datetime.datetime.fromisoformat(s)

def write_time_to(path, t):
    with open(path, 'w') as f:
        f.write(t.isoformat())

#===== main =====#
# check for new request to stay on
if t := read_time_from(REQUESTS_PATH):
    # only accept request to stay on < 90 min
    if t - NOW < datetime.timedelta(minutes=90):
        # only change our state if new request is longer than previous
        t_prev = read_time_from(STATE_PATH)
        if not t_prev or t_prev < t:
            write_time_to(STATE_PATH, t)
            write_time_to('requests/staying-on-until.txt', t)

# honor a previous request to stay on
if t := read_time_from(STATE_PATH):
    if NOW < t:
        sys.exit()

# stay on if we booted less than 5 minutes ago
with open('/proc/uptime') as f:
    if float(f.read().split()[0]) < 300:
        sys.exit()

# turn off
subprocess.run('poweroff', check=True)
