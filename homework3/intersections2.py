"""
An optimized version of intersections.py that uses the fsolve
function from the scipy library
"""


from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

from newton import solve
from newton import fvals_sqrt

def find_intersection(f, g, x0, max_iters=20, tolerance=10e-12, debug=False):
	
	return fsolve(lambda x: f(x) - g(x), x0, xtol = tolerance, full_output=True)



def test1():
	"""
	Test find_intersection of two functions using different
	initial conditions
	"""

	g1vals = lambda x: x*np.cos(np.pi*x)
	g2vals = lambda x: 1.- 0.6*x**2

	x = np.linspace(-10, 10, 1000)
	plt.figure(1)
	plt.clf()
	plt.plot(x, g1vals(x), 'b', x, g2vals(x), 'r')
	plt.legend(['g1', 'g2'])

	for x0 in [-2.2, -1.6, -0.8, 1.45]:
		res = find_intersection(g1vals, g2vals, x0)
		print "%s" % res[3]
		print "solve returns x = %22.15e after %s calls" % (res[0][0], res[1]['nfev'])
		fx = g1vals(res[0][0]) - g2vals(res[0][0])
		print "   f(x) = %22.15e" % fx
		plt.plot(res[0][0], g1vals(res[0][0]), "ko")

	plt.axis([-5, 5, -4, 4])
	plt.grid()
	plt.show()

def test2():
	g1vals = lambda x: np.sin(x)
	g2vals = lambda x: 1-x**2

	x = np.linspace(-10, 10, 1000)
	plt.figure(1)
	plt.clf()
	plt.plot(x, g1vals(x), 'b', x, g2vals(x), 'r')
	plt.legend(['g1', 'g2'])

	for x0 in [-2.2, -1.6, -0.8, 1.45]:
		res = find_intersection(g1vals, g2vals, x0)
		print "%s" % res[3]
		print "solve returns x = %22.15e after %s calls" % (res[0][0], res[1]['nfev'])
		fx = g1vals(res[0][0]) - g2vals(res[0][0])
		print "   f(x) = %22.15e" % fx
		plt.plot(res[0][0], g1vals(res[0][0]), "ko")

	plt.axis([-5, 5, -4, 4])
	plt.grid()
	plt.show()

#def test_newton():


