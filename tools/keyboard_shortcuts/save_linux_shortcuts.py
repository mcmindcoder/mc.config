#!/usr/bin/python

# gsettings get org.gnome.desktop.wm.keybindings switch-to-workspace-up
# gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-up '['<Control><Alt>Up']'

import subprocess
import datetime
import sys
import os

# Cinamon:  echo $XDG_CURRENT_DESKTOP == CINAMON
# Mate: echo $XDG_CURRENT_DESKTOP == MATE
XDG_CURRENT_DESKTOP = os.environ.get('XDG_CURRENT_DESKTOP', 'CINAMON')
OUT_SCRIPT_NAME='set_shortcuts_' +  datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.sh'
if(XDG_CURRENT_DESKTOP == 'MATE'):
	SCHEMADIR='org.mate.Marco.window-keybindings'
else:
	SCHEMADIR='org.gnome.desktop.wm.keybindings'


def get_shortcuts():
	keys = subprocess.Popen(['gsettings', 'list-keys', SCHEMADIR], stdout=subprocess.PIPE).communicate()[0]
	keys = keys.split('\n')

	shortcuts = {}
	for i in keys:
	    if len(i) > 0:
	        sc = subprocess.Popen(['gsettings', 'get', SCHEMADIR, i], stdout=subprocess.PIPE).communicate()[0]
	        sc = sc.replace('\n', '')
	        sc = sc.replace('@as ', '')
	        shortcuts[i] = sc

	return shortcuts        

def print_shortcuts(shortcusts):
	if shortcusts == None or len(shortcusts) == 0:
		print('No shortcuts found for schemadir: ' + SCHEMADIR)

	print('Found ' + str(len(shortcust)) + ' shortcuts:')
	j = 1
	for k,v in shortcust.items():
	    print(str(j) + '  ' + k + ' : ' + v)
	    j += 1 

def save_shortcuts(shortcusts):
	file = open(OUT_SCRIPT_NAME,'w')
	file.write("#!/bin/sh\n")
	for schema,shortcut in shortcusts.items():
		cmd = 'gsettings set ' + SCHEMADIR + ' ' + schema + ' "' + shortcut + '"\n'
		file.write(cmd)
	file.close()
	print('\nOutput script created: ' + OUT_SCRIPT_NAME)


if len(sys.argv) > 1:
	SCHEMADIR = sys.argv[1]
print('Detected dsktop: ' + XDG_CURRENT_DESKTOP)
print('Use schemadir: ' + SCHEMADIR)

shortcust = get_shortcuts()
print_shortcuts(shortcust)
save_shortcuts(shortcust)
