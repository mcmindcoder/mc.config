#/bin/sh
sudo echo 'Start system configuration'
sudo /usr/bin/python2 /usr/local/bin/ansible-playbook -v --connection=local main.yml -e 'ansible_python_interpreter=/usr/bin/python2'