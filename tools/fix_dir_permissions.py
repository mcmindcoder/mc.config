#!/usr/bin/python3

import pwd
import sys
import grp
import os
import subprocess

DEBUG = False

def get_all_groups():
	groups = list()
	for g in grp.getgrall():
		if len(g[3]) > 0:
			groups.append(g[3][0])
	#print(groups)
	return groups


def get_user_groups(user):
	groups = set()
	for g in grp.getgrall():
		if user in g.gr_mem:
			groups.add(g.gr_name)
	#print(groups)
	return groups


def check_prerequisites(dir_path):	
	if not os.path.exists(dir_path):
		raise Exception('Directory does not exists ' + dir_path)


def add_user_to_group(user, group):
	cmd = 'sudo usermod -a -G ' + group + ' ' + username
	print('Execute: ' + cmd)
	if not DEBUG:
		os.system(cmd)


def set_file_permissions(file):
	perm = oct(os.stat(file).st_mode)
	newperm = str(perm[-3])
	newperm = newperm + newperm + '0'
	print('Execute: sudo chmod ' + str(newperm) + ' "' + file + '"')
	if not DEBUG:
		# os.chmod(file, int(newperm, base=8))
		# os.system('sudo chmod ' + str(newperm) + ' ' + ' "' + file + '"')
		res = subprocess.check_output(['sudo', 'chmod', str(newperm), file], stderr=subprocess.STDOUT)
		print(res)


def update_permissions(path):
	excludes = [
		path + '/.cache'
	]

	cnt = 0
	# r=root, d=directories, f = files
	for r, d, f in os.walk(path):
		for file in d:
			file = os.path.join(r, file)
			skip = False

			for e in excludes:
				if file.startswith(e):
					skip = True
					break

			if not skip and not os.path.islink(file):
				set_file_permissions(file)
				cnt += 1

		for file in f:
			file = os.path.join(r, file)
			skip = False

			for e in excludes:
				if file.startswith(e):
					skip = True
					break

			if not skip and not os.path.islink(file):
				set_file_permissions(file)
				cnt += 1

	return cnt
	

def main():
	print('Fix directory permissions')

	if len(sys.argv) != 2:
		raise Exception('Usage: fix_dir_permissions.py <folder>')
	dir_path = sys.argv[1]
	print('Directory to fix permissions for: ' + str(dir_path))

	check_prerequisites(dir_path)


	print('Modify permissions at: ' + dir_path)
	cnt = update_permissions(dir_path)
	print('Total files modified: ' + str(cnt))
	print()


def test():
	update_permissions('mc', '/home/master/_CONFIG')
	exit(0)


if __name__ == '__main__':
	#test()
	main()