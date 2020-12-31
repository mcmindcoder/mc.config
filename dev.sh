#/bin/sh
echo 'Start system configuration'
echo

ARGS="$*"
if [ -f "/usr/bin/ansible-playbook" ]; then
	sudo echo Use /usr/bin/ansible-playbook
	/usr/bin/python3 /usr/bin/ansible-playbook $ARGS --connection=local dev.yml -e 'ansible_python_interpreter=/usr/bin/python3'
	exit
elif [ -f "/usr/local/bin/ansible-playbook" ]; then
	sudo echo Use /usr/local/bin/ansible-playbook
	/usr/bin/python3 /usr/local/bin/ansible-playbook $ARGS --connection=local dev.yml -e 'ansible_python_interpreter=/usr/bin/python3'
	exit
else
	echo 'Error: ansible is not installed' >&2
	echo 'Run sudo apt install ansible' >&2
	exit 1
fi


