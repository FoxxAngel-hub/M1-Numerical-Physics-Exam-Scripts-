#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 08:50:37 2025

@author: ellena
"""

import numpy as np
import matplotlib.pyplot as plt

mu=90
lamb=0.13
c0=mu**4/(4*lamb)
A=1e8

Es = np.zeros(500)

def V(E,E2):
    return (-mu**2*E**2+lamb*E**4+c0+mu**2*E2**2-lamb*E2**4-c0)/A

N=1000
T0 = 10
delt=40
for i in range(N):
    T=T0*(1-(i/N))
    dEp = np.random.rand(500)
    dEp *= 2*delt
    dEp += -delt
    for j in range(500):
        P = np.exp(V(Es[j],Es[j]+dEp[j])/T)
        u = np.random.rand()
        if (u<P):
            Es[j] = Es[j]+dEp[j]

v = np.sqrt(mu**2/(2*lamb))
nE = np.linspace(min(Es), max(Es), 128)
error1 = np.abs(nE[0]-v)
error2 = np.abs(nE[0]+v)
index = np.zeros(2)
for i in range(128):
    nerr1 = np.abs(nE[i]-v)
    nerr2 = np.abs(nE[i]+v)
    if (error1 > nerr1):
        error1 = nerr1
        index[0] = i
    if (error2 > nerr2):
        error2 = nerr2
        index[1] = i
hmax = np.zeros(128)
h,b = np.histogram(Es, bins=128)
hmax[int(index[0])] = max(h)
hmax[int(index[1])] = max(h)
plt.figure()
plt.scatter(nE, h, label="Results")
plt.bar(nE, hmax, linestyle='--', label="Theoretical minimas")
plt.xlabel("E [GeV]")
plt.ylabel("Number of particles")
plt.title("Histogram of final energies")
plt.legend()
plt.show()