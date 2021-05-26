#!/bin/bash

sleep 0.5

guake -r mc
guake -e pwd
guake -e 'mc'
guake -e '~/tools/clion-2020.1.1/bin/clion.sh &'

guake --new-tab=tab1 -r roscore
guake -e pwd
guake -e 'roscore &'
guake -e '~/tools/clion-2020.1.1/bin/clion.sh &'

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

guake --new-tab=tab4 -r test1
guake -e pwd
guake -e 'cd ~/dev/ros_cyngn_ws/src'

guake --new-tab=tab5 -r test2
guake -e pwd
guake -e 'cd ~/dev/ros_cyngn_ws/src'

guake --new-tab=tab6 -r test3
guake -e pwd
guake -e 'cd ~/dev/ros_cyngn_ws/src'

guake --new-tab=tab7 -r test4
guake -e pwd
guake -e 'cd ~/dev/ros_cyngn_ws/src'




guake -s 3




