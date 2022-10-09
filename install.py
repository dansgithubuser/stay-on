#! /usr/bin/env python3

import os

DIR = os.path.dirname(os.path.realpath(__file__))

script_path = os.path.join(DIR, 'main.py')
out_path = os.path.join(DIR, 'out.txt')
err_path = os.path.join(DIR, 'err.txt')
with open('/etc/crontab', 'a') as f:
    f.write(f'*/5 * * * * root python3 {script_path} > {out_path} 2> {err_path}\n')
