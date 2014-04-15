# -*- coding: UTF-8 -*-
"""
Demonstration script for quadratic interpolation.

To build our A matrix, it's best to define it in terms of
the x data points. 

The example function that we're trying to fit here 
is p(x) = c + cx + cx^2 ... and so while we could express a matrix
as a system of equations representation for each of our known x,y pairs,
like so...

c - 1c + 1c^2 = 1
c + 0c + 0c^2 = -1
c + 2c + 4c^2 = 7

... it's WAY better just to A) express the matrix in terms of ANY xi value,
and B) grow a matrix dynamically with a list comprehension,
using each xi value and manipulating it on the three levels 
we have for our function.

Concretely, the first row of the array computes on the first xi value,
and lets [0][0] default to the constant one, 
		 [0][1] multiply it by the constant 1  
	 and [0][2] apply the squaring constant 

We can now apply this matrix to any amount of x,y pairs and output the
optimal solution for the quadratic funciton p(x) = c + cx + cx^2


Modified by: Brian Sipple
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import solve

# Set up linear system to interpolate through data points:

# Data points:
# xi = np.array([-1., 0., 2])
# yi = np.array([1., -1., 7.])

# Lets try (−1,0), (1,4), (2,3) instead
xi = np.array([-1, 1, 2])
yi = np.array([0, 4, 3])



# It would be better to define A in terms of the xi points.
#A = np.array([ [1., x*1., x**2] for x in xi ])

# in addition to list expressions, we can use the np.vstack method:
A = np.vstack( [np.ones(3), xi, xi**2]).T
			  				
b = yi

# Solve the system:
c = solve(A,b)

print "The polynomial coefficients are:"
print c

# Plot the resulting polynomial:
x = np.linspace(-2,3,1001)   # points to evaluate polynomial
y = c[0] + c[1]*x + c[2]*x**2

plt.figure(1)       # open plot figure window
plt.clf()           # clear figure
plt.plot(x,y,'b-')  # connect points with a blue line

# Add data points  (polynomial should go through these points!)
plt.plot(xi,yi,'ro')   # plot as red circles
plt.ylim(-2,8)         # set limits in y for plot

plt.title("Data points and interpolating polynomial")

plt.savefig('hw2a.png')   # save figure as .png file
