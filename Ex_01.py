#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 08:06:30 2025

@author: ellena
"""

import numpy as np
import matplotlib.pyplot as plt

r = 5
R = np.linspace(2*r, 20*r, num=50)
Vth = 2*np.pi**2*r**2*R
V = np.zeros(50)

N=5000
for i in range(np.size(R)):
    l=R[i]+r
    x=np.random.rand(N)*l
    y=np.random.rand(N)*l
    z=np.random.rand(N)*l
    M=np.zeros(N)
    for j in range(N):
        dist=(np.sqrt(x[j]*x[j]+y[j]*y[j])-R[i])**2+z[j]*z[j]
        M[j] = dist
    Msuccess = np.size(np.where(M<=r*r))
    V[i] = (2*l)**3*Msuccess/N

plt.figure()
plt.plot(R, Vth, label="Theory")
plt.scatter(R, V, label="Monte-Carlo", marker="o")
plt.xlabel("R")
plt.ylabel("Torus Volume")
plt.legend()
plt.show()