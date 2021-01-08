#!/bin/sh
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/$USER/mc.config/files/keepass/lib
echo $LD_LIBRARY_PATH

BASEDIR=$(dirname "$0")
echo $BASEDIR
$BASEDIR/keepassxc