#!/bin/bash

sleep 0.5

guake -r Tab1
guake -e pwd
guake -e 'ls -la'

guake --new-tab=tab2 -r Tab2
guake -e pwd
guake -e 'ls -la'

guake --new-tab=tab3 -r Tab3
guake -e pwd
guake -e 'ls -la'




