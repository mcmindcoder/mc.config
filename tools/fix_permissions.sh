#!/bin/bash

echo Start updating permissions...

# apt
sudo chmod u+rwx,go+rx,go-w /etc/apt/sources.list.d/
sudo chmod u+rw,u-x,go+r,go-wx /etc/apt/sources.list.d/*

#python
sudo find /usr/local/lib/python2.7/dist-packages/ -type f -exec chmod u+rw,go+r {} \;
sudo find /usr/local/lib/python2.7/dist-packages/ -type f -exec chown root:staff {} \;
sudo find /usr/local/lib/python2.7/dist-packages/ -type d -exec chmod u+rwx,g+rs,o+rx {} \;
sudo find /usr/local/lib/python2.7/dist-packages/ -type d -exec chown root:staff {} \;

sudo find /usr/local/lib/python3.5/dist-packages/ -type f -exec chmod u+rw,go+r {} \;
sudo find /usr/local/lib/python3.5/dist-packages/ -type f -exec chown root:staff {} \;
sudo find /usr/local/lib/python3.5/dist-packages/ -type d -exec chmod u+rwx,g+rs,o+rx {} \;
sudo find /usr/local/lib/python3.5/dist-packages/ -type d -exec chown root:staff {} \;

#mint config
sudo chown -R $USER:$USER ~/.config

#ssh config
sudo chown -R $USER:$USER ~/.ssh
chmod 600 ~/.ssh/*

echo Permissions updated