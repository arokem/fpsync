#!/usr/bin/env python
from __future__ import print_function
import sys

catch_string = 'is newer'

files = []
for line in sys.stdin:
    if line and line[0] in '.<>[':
        continue
    
    line = line.strip()
    if line.endswith(catch_string):
        files.append(line[:-(len(catch_string) + 1)])
    else:
        print(line)

if files:
    print()
    print('=' * 75)
    print('WARNING: These files were newer on the remote side,\n'
          '         and were therefore not updated.')
    print()
    print('\n'.join(files))
    print('=' * 75)
