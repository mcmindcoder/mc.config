#/bin/sh
sudo echo 'Start system configuration'

if [ -f "/usr/bin/ansible-playbook" ]; then
	echo Use /usr/bin/ansible-playbook
    sudo /usr/bin/python2 /usr/bin/ansible-playbook -v --connection=local main.yml -e 'ansible_python_interpreter=/usr/bin/python2'
    exit
fi

if [ -f "/usr/local/bin/ansible-playbook" ]; then
	echo Use /usr/local/bin/ansible-playbook
	sudo /usr/bin/python2 /usr/local/bin/ansible-playbook -v --connection=local main.yml -e 'ansible_python_interpreter=/usr/bin/python2'
    exit
fi


