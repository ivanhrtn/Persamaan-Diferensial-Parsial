# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:48:13 2021

@author: Lenovo
"""

"""
The ODE d_{tt} u = c^2 d_{xx} u is trasnformed to a first-order ODE by introducing
v = du/dt: 
            d/dt (u, v) = (v, c^2 d_{xx} u)
"""
import numpy as np
import matplotlib.pyplot as plt


class wave_eq:
    def __init__(self,init_m,init_n):
        self.M = init_m
        self.N = init_n
        self.x_grid = np.linspace(0,1,self.M)
        dx = self.x_grid[1]-self.x_grid[0]
        self.x_grid = np.hstack((-dx, self.x_grid, self.x_grid[-1]+dx ))
        self.t_grid = np.linspace(0, 1, self.N + 2)
        self.solution = []


    def forward_euler_solver(self,g):
        M = self.M
        N = self.N 

        h = self.x_grid[1] - self.x_grid[0]
        k = self.t_grid[1] - self.t_grid[0]

        r = k/h
        u = np.zeros(shape = (M+2,N+2))

        u[:,0] = g(self.x_grid)

        print(N,M,len(self.t_grid))
        for i in range(N+1):
            print('time step {}/{}'.format(i+1,N+1))
            if (i == 0):
                u[1:-1,i+1]   = u[1:-1,i] +  (r**2)   *(u[2:,i]   - 2*u[1:-1,i] + u[:-2,i])
            else:
                u[1:-1,i+1]   = 2*u[1:-1,i] - u[1:-1,i-1] + (r**2)*(u[2:,i]   - 2*u[1:-1,i] + u[:-2,i])

            u[ 0,i+1]  = u[-3,i+1]
            u[-1,i+1]  = u[ 2,i+1]

        self.solution = u


def init_c_g(x):
    return np.cos(2*np.pi*x)

    
def analytical_sol(t,x):
    return 0.5 *( np.cos(2*np.pi*(x-t)) + np.cos(2*np.pi*(x+t)) )

obj = wave_eq(init_m=100, init_n=1000)
obj.forward_euler_solver(g=init_c_g)

#%%
nt = obj.solution.shape[1]
ylim = [np.min(obj.solution), np.max(obj.solution)]

for i in range(1,nt,200):
    plt.figure()
    plt.plot(obj.x_grid, obj.solution[:,i])
    plt.plot(obj.x_grid, analytical_sol(obj.t_grid[i], obj.x_grid))
    plt.ylim(ylim)
    plt.grid()
    plt.xlabel(r'$x$')
    plt.ylabel(r'$u$')