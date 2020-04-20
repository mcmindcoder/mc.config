#!/bin/bash

sleep 0.5

guake -r roscore
guake -e pwd
guake -e 'roscore &'
guake -e '~/tools/CLion-2020.1/clion-2020.1/bin/clion.sh &'

guake --new-tab=tab2 -r vpn
guake -e pwd
guake -e 'cd ~/vpn'

guake --new-tab=tab3 -r cyngn-ubuntu
guake -e pwd
guake -e 'cd ~/cyngn-ubuntu'
guake -e 'git prb'

guake --new-tab=tab3 -r project
guake -e pwd
guake -e 'cd ~/dev/ros_cyngn_ws/'

guake --new-tab=tab3 -r code
guake -e pwd
guake -e 'cd ~/dev/ros_cyngn_ws/src'




guake -s 3




