"""
Simutlates Newton's method for finding the root of a non-linear
function.
"""

def solve(fvals, x0, debug=False, max_iters=20, threshold=10e-14):
	"""
	This function returns a tuple consisting of the final iterate
	(the approximation of the root determined) and the 
	number of iterations taken 

	@param fvals -- a function that returns the values of f(x) and f'(x)
	for any input x
	
	@param x0 -- the initial guess

	"""
	iter_count = 0       # initialize iter counter to 0	

	x = x0

	if debug:
		print "Initial guess: x = %22.11e" % x

	while iter_count < max_iters:

		f, fp = fvals(x)

		# To signifiy the next x, we'll just continuously update x   
		# Newton's method for finding the roots of a non-linear function
		deltax = f/fp
		x = x - deltax	

		if debug:
			print "After %s iterations, x = %22.15e" % (iter_count, x)

		if abs(f) < threshold: #Do we want to continue?
			break
		
		#If we haven't converged by the end, print a warning
		if iter_count == max_iters - 1:
			f, fp = fvals(x)
			if abs(f) > threshold:
				print "*** Warning: has not yet converged"
				return x, iter_count
		else:
			iter_count += 1


	return x, iter_count


def fvals_sqrt(x):
    """
    Return f(x) and f'(x) for applying Newton to find a square root.
    """
    f = x**2 - 4.
    fp = 2.*x
    return f, fp

def test1(debug_solve=False):
    """
    Test Newton iteration for the square root with different initial
    conditions.
    """
    from numpy import sqrt
    for x0 in [1., 2., 100.]:
        print " "  # blank line
        x,iters = solve(fvals_sqrt, x0, debug=debug_solve)
        print "solve returns x = %22.15e after %i iterations " % (x,iters)
        fx,fpx = fvals_sqrt(x)
        print "the value of f(x) is %22.15e" % fx
        assert abs(x-2.) < 1e-14, "*** Unexpected result: x = %22.15e"  % x