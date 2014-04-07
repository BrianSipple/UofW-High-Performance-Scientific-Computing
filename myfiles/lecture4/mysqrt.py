"""
An algorithm for finding the square root of an integer, x

Start by initializing s as a guess. 
If we take the average of s + x/s for enough iterations, we will
always converge on the square root.

Why: If our guess, s, is too small, x/s will be larger than the true square root
	 If our guess, s, is too large, x/s will be smaller than the true squeare root
	 If it's just right, x/s will be the square root.

Therefore, continuous average iterations will hone in on the true square root!

Enhancements: max_iteration and tolerance -- cap the iterations, but check the delta of s at each 
			  iteration and break from the loop if delta is less than our tolerance level.


"""

def sqrt2(number, guess, max_iterations=200, tolerance=1.e-14, debug=False):
	
	from numpy import nan

	# Defensive measures
	if number == 0.:
		return 0.
	elif number < 0:
		print ("*** Error, x must be nonnegative!")
		return nan

	assert number > 0., "Unrecognized input!"

	s = guess

	for k in range(max_iterations):
		if debug:
			print ("Before iteration: %s, s = %20.15f" % (k, s))
		s0 = s
		s = 0.5 * (s + number/s)
		delta_s = s - s0
		if abs(delta_s / number) < tolerance:
			break
	print ("After %s iterations, s = %20.15f" % (k+1, s))
	return s 

def test():
	from numpy import sqrt

	xvalues = [0., 2., 100., 10000., 1.e-4]
	for x in xvalues:
		print ("Testing with x = {:20.15e}".format(x))
		s = sqrt2(x, 4)
		s_numpy = sqrt(x)
		print ("  s = {:20.15e},  numpy.sqrt = {:20.15e}" \
				.format(s, s_numpy))
		assert abs(s - s_numpy) < 1e-14, \
				"Disagreement for x = {:20.15e}".format(x)





if __name__ == "__main__":
	sqrt2(16., 1)
