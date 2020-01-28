#!/usr/bin/python3

# gsettings get org.gnome.desktop.wm.keybindings switch-to-workspace-up
# gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-up '['<Control><Alt>Up']'

import subprocess
import datetime
import sys
import os

# Cinamon:  echo $XDG_CURRENT_DESKTOP == X-Cinnamon
# Mate: echo $XDG_CURRENT_DESKTOP == MATE
XDG_CURRENT_DESKTOP = os.environ.get('XDG_CURRENT_DESKTOP', 'CINAMON')
OUT_SCRIPT_NAME = 'config_guake_' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.sh'
# OUT_SCRIPT_NAME = 'config_shortcuts.sh'
SCHEMADIR = 'org.apps.guake.keybindings'

class Shortcut:
    def __init__(self):
        self.schema = ''
        self.key = ''
        self.shortcut = ''

    def __str__(self):
        msg = self.schema + ' ' + self.key + ' "' + self.shortcut + '"'
        return msg


def get_shortcuts():
    schemas = subprocess.Popen(['gsettings', 'list-schemas'], stdout=subprocess.PIPE).communicate()[0]
    schemas = str(schemas)[2:-3].split('\\n')
    schemas = [i for i in schemas if i.startswith(SCHEMADIR)]
    schemas.sort()

    shortcuts = []
    for s in schemas:
        keys = subprocess.Popen(['gsettings', 'list-keys', s], stdout=subprocess.PIPE).communicate()[0]
        keys = str(keys)[2:-3].split('\\n')
        for k in keys:
            sc = Shortcut()
            sc.schema = s
            sc.key = k
            shortcuts.append(sc)

    for s in shortcuts:
        sc = subprocess.Popen(['gsettings', 'get', s.schema, s.key], stdout=subprocess.PIPE).communicate()[0]
        sc = str(sc)[2:-3]
        sc = sc.replace('@as ', '')
        s.shortcut = sc

    return shortcuts


def print_shortcuts(shortcuts):
    if shortcuts == None or len(shortcuts) == 0:
        print('No shortcuts found')

    print('Found ' + str(len(shortcust)) + ' shortcuts:')
    j = 1
    for s in shortcuts:
        print(str(j) + '  ' + str(s))
        j += 1


def save_shortcuts(shortcuts):
    file = open(OUT_SCRIPT_NAME, 'w')
    file.write("#!/bin/sh\n")
    for s in shortcuts:
        cmd = 'gsettings set ' + str(s) + '\n'
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
