#!/usr/bin/python3

# gsettings get org.gnome.desktop.wm.keybindings switch-to-workspace-up
# gsettings set org.gnome.desktop.wm.keybindings switch-to-workspace-up '['<Control><Alt>Up']'

import argparse
import subprocess
import datetime
import sys
import os

OUT_SCRIPT_NAME = 'gconfig_' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.sh'


class GConfEntry:
    def __init__(self, schema='', key='', value=''):
        self.schema = schema
        self.key = key
        self.value = value

    def __str__(self):
        msg = self.schema + ' ' + self.key + ' "' + self.value + '"'
        return msg

    def __eq__(self, other):
        if not isinstance(other, GConfEntry):
            return False
        if self.schema != other.schema:
            return False
        if self.key != other.key:
            return False
        if self.value != other.value:
            return False
        return True


def save_gconf_schema(schema, recursively):
    config = get_gconf_schema(schema, recursively)
    if not config:
        raise Exception('Schema does not exists: ' + schema)
    save_gconf(config)
    return config


def get_gconf_schema(schema, recursively):
    schemas = subprocess.Popen(['gsettings', 'list-schemas'], stdout=subprocess.PIPE).communicate()[0]
    schemas = str(schemas)[2:-3].split('\\n')
    if recursively:
        schemas = [i for i in schemas if i.startswith(schema)]
        schemas.sort()
    elif schema in schemas:
        schemas = [schema]
    else:
        return None

    config = []
    for s in schemas:
        keys = subprocess.Popen(['gsettings', 'list-keys', s], stdout=subprocess.PIPE).communicate()[0]
        keys = str(keys)[2:-3].split('\\n')
        for k in keys:
            sc = GConfEntry()
            sc.schema = s
            sc.key = k
            config.append(sc)

    for s in config:
        sc = subprocess.Popen(['gsettings', 'get', s.schema, s.key], stdout=subprocess.PIPE).communicate()[0]
        sc = str(sc)[2:-3]
        sc = sc.replace('@as ', '')
        s.value = sc

    return config


def print_gconf(config):
    if config == None or len(config) == 0:
        print('No shortcuts found')

    print('Found ' + str(len(config)) + ' item:')
    j = 1
    for s in config:
        print(str(j) + '  ' + str(s))
        j += 1


def save_gconf(config):
    file = open(OUT_SCRIPT_NAME, 'w')
    file.write("#!/bin/sh\n")
    for s in config:
        cmd = 'gsettings set ' + str(s) + '\n'
        file.write(cmd)
    file.close()
    
    subprocess.Popen(['chmod', 'ug+x', OUT_SCRIPT_NAME], stdout=subprocess.PIPE).communicate()[0]

    print('\nOutput script created: ' + OUT_SCRIPT_NAME)


def save_gconf_key(schema, key):
    gc = GConfEntry(schema, key, get_gconf_key(schema, key))
    if not gc.value:
        raise Exception('Key does not exists: ' + str(gc))
    config = [gc]
    save_gconf(config)
    return config


def get_gconf_key(schema, key):
    val = subprocess.Popen(['gsettings', 'get', schema, key], stdout=subprocess.PIPE).communicate()[0]
    if len(val) == 0:
        return None
    val = str(val)[2:-3]
    val = val.replace('@as ', '')
    return val


SCHEMAS = {
    'pck': 'org.cinnamon.desktop.keybindings',
    'pgk': 'org.gnome.desktop.wm.keybindings',
    'pmk': 'org.mate.Marco.window-keybindings',
    'pts': 'org.cinnamon.desktop.interface',
}


def main():
    parser = argparse.ArgumentParser(description='Save gsettings to shell script')
    parser.add_argument('-v', action='store_true', help='Verbose')
    parser.add_argument('-k', type=str, nargs=2, metavar=('SCHEMA', 'KEY'), help='Save single gsettings key')
    parser.add_argument('-s', type=str, nargs=1, metavar='SCHEMA', help='Save all gsettings keys inside schema')
    parser.add_argument('-r', type=str, nargs=1, metavar='SCHEMA', help='Save all gsettings keys inside schema recursively')
    parser.add_argument('-pck', action='store_true', help='Store recursively ' + SCHEMAS['pck'])
    parser.add_argument('-pgk', action='store_true', help='Store recursively ' + SCHEMAS['pgk'])
    parser.add_argument('-pmk', action='store_true', help='Store recursively ' + SCHEMAS['pmk'])
    parser.add_argument('-pts', action='store_true', help='Store key ' + SCHEMAS['pts'])
    args = parser.parse_args()

    if args.pck:
        schema = SCHEMAS['pck']
        conf = save_gconf_schema(schema, True)
    elif args.pgk:
        schema = SCHEMAS['pgk']
        conf = save_gconf_schema(schema, True)
    elif args.pmk:
        schema = SCHEMAS['pmk']
        conf = save_gconf_schema(schema, True)
    elif args.pts:
        schema = SCHEMAS['pts']
        key = 'text-scaling-factor'
        conf = save_gconf_key(schema, key)
    elif args.k != None:
        schema = args.k[0]
        key = args.k[1]
        conf = save_gconf_key(schema, key)
    elif args.s != None:
        schema = args.s[0]
        conf = save_gconf_schema(schema, False)
    elif args.r != None:
        schema = args.r[0]
        conf = save_gconf_schema(schema, True)
    else:
        parser.print_help()
        exit(0)

    if args.v:
        print_gconf(conf)


if __name__ == '__main__':
    main()
