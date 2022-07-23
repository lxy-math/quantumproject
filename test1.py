# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 23:05:07 2022

@author: lxy
"""

import tensorcircuit as tc
import tensorflow as tf
import math
import numpy as np

tc.set_backend("tensorflow")

X = tc.gates._x_matrix  # same as tc.gates.xgate().tensor.numpy()
Y = tc.gates._y_matrix  # same as tc.gates.ygate().tensor.numpy()
Z = tc.gates._z_matrix  # same as tc.gates.zgate().tensor.numpy()
H = tc.gates._h_matrix  # same as tc.gates.hgate().tensor.numpy()
S = tc.gates._s_matrix
T = tc.gates._t_matrix

print(f"{X=}\n")
print(f"{Y=}\n")
print(f"{Z=}\n")
print(f"{H=}\n")
print(f"{S=}\n")
print(f"{T=}\n")

theta = math.pi / 2

rx = tc.gates.rx_gate(theta).tensor.numpy()
ry = tc.gates.ry_gate(theta).tensor.numpy()
rz = tc.gates.rz_gate(theta).tensor.numpy()

# print(f"{rx=}\n")
# print(f"{ry=}\n")
# print(f"{rz=}\n")

rx_square = rx**2
ry_square = ry**2
rz_square = rz**2

print(f"{rx_square=}\n")
print(f"{ry_square=}\n")
print(f"{rz_square=}\n")