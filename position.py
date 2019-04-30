"""
This program is a modified version of Exercise 2.7 in "A Primer on
Scientific Programming with Python", ed. 4, by Langtangen.

User specifies initial positive velocity v0 and position h0. Time interval from
t = 0 to t = 2v0/9.81 is uniformly partioned into n intervals, where n is specified
by user.

Program plots height as function of time and prints table
of time and height values. 
"""

import numpy as np
import matplotlib.pyplot as plt

def height(h0,v0,t):

    """
    height as function of initial height, initial velocity and time
    """
    
    return h0 + v0*t - (1/2)*9.81*(t**2) 


def tMax(v0):

    """
    t value where object returns to initial height
    """
    
    return 2*v0/9.81

def unif(n,T):

    """
    returns array of uniformly spaced points in time
    """
    
    unif_spaced = []

    i= 0

    while i in range(0, n + 1):
        unif_spaced.append(i*T/n)
        i += 1

    return np.array(unif_spaced)

"""
Maybe better to use following for statement.  Used while loop for purposes
of assignment.

    for i in range(0, n+1):
        unif_spaced.append(i*T/n)

    return np.array(unif_spaced)
"""

##################################

"""
User specifed values for h0, v0 and n
"""

h0 = 20
v0 = 10
T = tMax(v0)
n = 20

t_vals = unif(n,T)
y_vals = height(h0,v0,t_vals)

##################################

"""
Generating table of values
"""

i = 0

while i < len(t_vals):
    if i == 0:
        print(' time | height')
        print('---------------')
        print(f" {round(t_vals[i],2):.2f} | {round(y_vals[i],2):.2f}")
        i += 1
    else:
        print(f" {round(t_vals[i],2):.2f} | {round(y_vals[i],2):.2f}")
        i += 1
        
##################################

"""
Plotting figure
"""
        
plt.plot(t_vals,y_vals,'r')
plt.xlabel('time')
plt.ylabel('height')
plt.show()




