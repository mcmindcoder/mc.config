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


def check_prerequisites(users):
	for u in users:
		try:
			pwd.getpwnam(u)
		except KeyError:
			raise Exception('User ' + u + ' does not exist')

		groups = get_user_groups(u)
		if not u in groups:
			raise Exception('User group ' + u + ' does not exist')

		home = '/home/' + u
		if not os.path.exists(home):
			raise Exception('Home dir does not exists ' + home)


def add_user_to_group(user, group):
	cmd = 'sudo usermod -a -G ' + group + ' ' + username
	print('Execute: ' + cmd)
	if not DEBUG:
		os.system(cmd)


def ensure_groups(users):
	for u in users:
		groups = get_user_groups(u)

		for uu in users:
			if uu not in groups:
				print('Add user ' + u + ' to group ' + uu)
				add_user_to_group(u, uu)

def set_file_owner(file, user):
	uid = pwd.getpwnam(user).pw_uid
	gid = grp.getgrnam(user).gr_gid
	print('Execute: sudo chown ' + str(uid) + ':' + str(gid) + ' "' + file + '"')
	if not DEBUG:
		# os.chown(file, uid, gid)
		# os.system('sudo chown ' + str(uid) + ':' + str(gid) + ' "' + file + '"')
		res = subprocess.check_output(['sudo', 'chown', str(uid) + ':' + str(gid), file], stderr=subprocess.STDOUT)
		print(res)


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


def update_permissions(user, path):
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
				set_file_owner(file, user)
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
				set_file_owner(file, user)
				set_file_permissions(file)
				cnt += 1

	return cnt
	

def main():
	print('Fix user permissions')

	users = sys.argv[1:]
	if len(users) < 2:
		raise Exception('You need to enter at least 2 linux users')
	print('Users to fix access for: ' + str(users))

	check_prerequisites(users)
	ensure_groups(users)

	for u in users:
		home = '/home/' + u
		print('Modify permissions at: ' + home)
		cnt = update_permissions(u, home)
		print('Total files modified: ' + str(cnt))
		print()


def test():
	update_permissions('mc', '/home/master/_CONFIG')
	exit(0)


if __name__ == '__main__':
	#test()
	main()