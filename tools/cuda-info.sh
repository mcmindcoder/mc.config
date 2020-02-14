#!/bin/bash

echo
echo ---------------------------------
echo Linux Version
echo
uname -a

echo
echo ---------------------------------
echo CUDA Version
echo
#dpkg -s $(apt list --installed | grep cuda | tail -n 1 | cut -d '/' -f 1) | grep Version
dpkg -l | grep cuda
#nvcc --version

echo
echo ---------------------------------
echo Nvidia Driver Version
echo
nvidia-smi


