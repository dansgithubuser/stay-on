#! /usr/bin/env python3

import argparse
import datetime
import os

parser = argparse.ArgumentParser()
parser.add_argument('path', help='Where to put the stay-on-until.txt file.')
args = parser.parse_args()

if not args.path.endswith('stay-on-until.txt'):
    path = os.path.join(args.path, 'stay-on-until.txt')
else:
    path = args.path

hour_from_now = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=1).isoformat()
with open(path, 'w') as f:
    f.write(hour_from_now)
print(f'staying on until {hour_from_now} (~1 hour)')
