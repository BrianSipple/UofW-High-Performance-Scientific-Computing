
"""
Demonstration module for quadratic interpolation.
Update this docstring to describe your code.

Modified by: Brian Sipple
"""


import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import solve

def quad_interp(xi,yi):
    """
    Quadratic interpolation.  Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for i = 0,1,2.
    Returns c, an array containing the coefficients of
      p(x) = c[0] + c[1]*x + c[2]*x**2.

    """


    # check inputs and print error message if not valid:

    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have length 3"
    assert len(xi)==3 and len(yi)==3, error_message

    # Set up linear system to interpolate through data points:


    #A = np.array([ [1., x*1., x**2] for x in xi ])

    # in addition to list expressions, we can use the np.vstack method:
    A = np.vstack( [np.ones(3), xi, xi**2]).T

    b = yi

    ### Fill in this part to compute c ###

    c = solve(A, b)

    return c


def plot_quad(xi, yi):
    """
    Takes two numpy arrays xi and yi of length 3 and calls quad_interp
    to compute c, and then plots both the interpolating polynomial
    and the data points, and saves the resulting figure
    as 'quadratic.png'
    """
    c = quad_interp(xi, yi)
    
    x = np.linspace(xi.min()-1, xi.max()+1, 1000)   #points to evaluate the polynomial (making sure here that we cover the entire range!)
    y = c[0] + c[1]*x + c[2]*x**2

    plt.figure(1)         # open the plot figure view
    plt.clf()             # clear the figure
    plt.plot(x, y, 'b-')  #connect the points with a blue line

    #add data points (polynomial should go through these points!)
    plt.plot(xi, yi, 'ro')      #plot as red circles
    plt.ylim( y.min() - ( (y.max()-y.min())/4 ), y.max() + ( (y.max()-y.min())/4 ) )

    plt.title("Data points and interpolating polynomial")

    plt.savefig('quadratic.png')   # save figure as .png file")



def cubic_interp(xi, yi):
    """
    Solves an interpolation problem if the inputs xi and 
    yi are of length 4, and if we determine the cubic polynomial
    of p(x) = c + cx + cx^2 + cx^3
    """
    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have length 4"
    assert len(xi)==4 and len(yi)==4, error_message

    #A = np.vstack( [np.ones(4), xi, xi**2, xi**3] ).T 
    A = np.array([ [1., x*1., x**2, x**3] for x in xi ])
    b = yi
    c = solve(A,b)

    return c




def plot_cubic(xi, yi):
    """
    Takes two numpy arrays xi and yi of length 4 and calls cubic_interp
    to compute c, and then plots both the interpolating polynomial
    and the data points, and saves the resulting figure
    as 'cubic.png' 
    """

    c = cubic_interp(xi, yi)
    
    x = np.linspace(xi.min()-1, xi.max()+1, 1000)   #points to evaluate the polynomial (making sure here that we cover the entire range!)
    y = c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3

    plt.figure(1)         # open the plot figure view
    plt.clf()             # clear the figure
    plt.plot(x, y, 'b-')  #connect the points with a blue line

    #add data points (polynomial should go through these points!)
    plt.plot(xi, yi, 'ro')      #plot as red circles
    plt.ylim( y.min() - ( (y.max()-y.min())/4 ), y.max() + ( (y.max()-y.min())/4 ) )

    plt.title("Data points and interpolating polynomial")

    plt.savefig('cubic.png')   # save figure as .png file")



def poly_interp(xi, yi):
    """
    Generalization of the above functions that computes a 
    polynomial function for arrays xi and yi of any 
    length (assuming they're the same length, that is)
    """

    error_message = "xi and yi must be of the same length"
    assert len(xi) == len(yi), error_message

    error_message = "xi and yi must be of the type ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    size = len(xi)

    A = []                      # Start with an empty list
    for j in range(len(xi)):    # Loop through the polynomial exponents
        A.append(xi**j)         # Add the Numpy array xi**j to A
    A = np.array(A).T           # Turn A into a Numpy array and transpose

    #exponents = range(2, len(xi), 1)    #get a list of all the exponents that we'll be using for the matrix

    #for i in exponents:
     #   A.append(xi**i)

    b = yi
    c = solve(A, b)

    print "The coefficients are: "
    print c
    return c




def test_quad1():
    """
    Test code, no return value or exception if test runs properly.
    """
    xi = np.array([-1.,  0.,  2.])
    yi = np.array([ 1., -1.,  7.])
    c = quad_interp(xi,yi)
    c_true = np.array([-1.,  0.,  2.])
    print "c =      ", c
    print "c_true = ", c_true
    # test that all elements have small error:
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c,c_true)
        


def test_quad2():
    """
    Test code, no return value or exception if test runs properly.
    (although be on the lookout for a plot)
    """
    xi = np.array([16, 51, 72])
    yi = np.array([223, 2, 121])

    c = quad_interp(xi,yi)

    x = np.linspace(xi.min()-1, xi.max()+1, 1000)
    y = c[0] + c[1]*x + c[2]*x**2

    plt.figure(1)         # open the plot figure view
    plt.clf()             # clear the figure
    plt.plot(x, y, 'b-')  #connect the points with a blue line

    #add data points (polynomial should go through these points!)
    plt.plot(xi, yi, 'ro')      #plot as red circles
    plt.ylim( y.min() - ( (y.max()-y.min())/4 ), y.max() + ( (y.max()-y.min())/4 ) )

    plt.title("Data points and interpolating polynomial")


def test_cubic():
    """
    Test code, no return value or exception if test runs properly.
    (although be on the lookout for a plot)
    """
    xi = np.array([23, 231, 2343, 23423])
    yi = np.array([3, 33, 333, 3333])


    c = cubic_interp(xi,yi)

    x = np.linspace(xi.min()-1, xi.max()+1, 1000)
    y = c[0] + c[1]*x + c[2]*x**2 + c[3]*x**3

    plt.figure(1)         # open the plot figure view
    plt.clf()             # clear the figure
    plt.plot(x, y, 'b-')  # connect the points with a blue line

    #add data points (polynomial should go through these points!)
    plt.plot(xi, yi, 'ro')      #plot as red circles
    plt.ylim( y.min() - ( (y.max()-y.min())/4 ), y.max() + ( (y.max()-y.min())/4 ) )

    plt.title("Data points and interpolating polynomial")




def poly_test():
    xi = np.array([-1., 0., 2., 3.])
    yi = np.array([1., 2., 3., 0.])

    c = poly_interp(xi, yi)
    c_true = np.array([2.,1.33333333,0.08333333, -0.25])

    print "c found = ", c
    print "c true = ", c_true

    #test that all elements that have a small error
    assert np.allclose(c, c_true), \
        "Incorrect result, c found = %s, expected = %s" % (c, c_true)


def plot_poly(xi, yi):

    c = poly_interp(xi, yi)

    x = np.linspace(xi.min()-1, xi.max()+1, 1000)
    
    size = len(c)
    
    y = c[size-1]
    for j in range(size-1, 0, -1):
        y = y*x + c[j-1]
    

    plt.figure(1)         # open the plot figure view
    plt.clf()             # clear the figure
    plt.plot(x, y, 'b-')  #connect the points with a blue line

    #add data points (polynomial should go through these points!)
    plt.plot(xi, yi, 'ro')      #plot as red circles
    plt.ylim( y.min() - ( (y.max()-y.min())/4 ), y.max() + ( (y.max()-y.min())/4 ) )

    plt.title("Data points and interpolating polynomial")

    print y


if __name__=="__main__":
    # "main program"
    # the code below is executed only if the module is executed at the command line,
    #    $ python demo2.py
    # or run from within Python, e.g. in IPython with
    #    In[ ]:  run demo2
    # not if the module is imported.
    print "Running test..."
    test_quad1()

