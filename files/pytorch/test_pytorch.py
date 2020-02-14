#!/usr/bin/python3

from __future__ import print_function
import torch

x = torch.rand(5, 3)
print('Random tensor:')
print(x)

has_cuda = torch.cuda.is_available()
print('CUDA available: ' + str(has_cuda))

print('PyTorch installed correctly!')