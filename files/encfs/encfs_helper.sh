#!/bin/bash
mntpoint=~/../master/.store/mountpoint
store=~/../master/.store/storage
lnpoint=~/Disk/Storage

cmd=$1

if [[ $cmd == "stop" ]]
then
  echo $mntpoint
  fusermount -u $mntpoint
  rm $lnpoint
  exit
fi

read -s -p "Enter password: " pass
echo 
if echo $pass | encfs -S  -o allow_other $store $mntpoint; then
  ln -s $mntpoint $lnpoint
else
	if [ "$(ls -A $DIR)" ]; then
		echo Directory $lnpoint is not empty
	else
		echo Remove $lnpoint
		rm $lnpoint
	fi
fi 
