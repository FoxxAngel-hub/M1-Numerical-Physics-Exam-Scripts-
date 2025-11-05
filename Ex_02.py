#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 08:26:13 2025

@author: ellena
"""

import numpy as np
import matplotlib.pyplot as plt

L = np.load('ID.npy')
S = 0.25*(np.roll(L, 1, axis=1)+np.roll(L, -1, axis=1)+np.roll(L, 1, axis=0)+np.roll(L, -1, axis=0))
Sx = 0.5*(np.roll(S, 1, axis=1)-np.roll(S, -1, axis=1))
Sy = 0.5*(np.roll(S, 1, axis=0)-np.roll(S, -1, axis=0))
D = np.sqrt(Sx**2+Sy**2)
mD = np.mean(D)
sD = np.std(D)
M = np.zeros([512,512])
cond = np.where(np.abs(D-mD)>=3*sD)
M[cond[0],cond[1]] = 1

plt.figure()
plt.subplot(121)
plt.imshow(L, cmap="gray")
plt.title("Original")
plt.subplot(122)
plt.imshow(M, cmap="gray")
plt.title("Edges")
plt.show()