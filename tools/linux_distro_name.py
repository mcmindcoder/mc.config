#!/usr/bin/python3

import os
import subprocess

'''
Ubuntu:
  $ cat /etc/os-release | grep "^NAME="
  NAME="Ubuntu"


Mint:
  $ cat /etc/os-release | grep "^NAME="
  NAME="Linux Mint"
'''

cmd = 'cat /etc/os-release | grep "^NAME="'
output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = output.communicate()[0]
output = output.decode('utf-8').lower()
output = output[6:-2] # Remove NAME=""

if 'mint' in output:
	output = 'mint'

print(output)
