#!/usr/bin/env python
# encoding: utf-8
"""
bcalc.py

Created by Colin Wheeler on 2009-02-08.
Copyright (c) 2009 Niblonian Soft. All rights reserved.
"""

import sys
import getopt
import math

help_message = '''
Usage: ./BinomialProbability.py [Number of successes] [Number of Trials] [Probability of Success]
Example:./bcalc.py 3 10 .20
'''

class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg

def factorial(n):
	if n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		return result

def main(argv=None):
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
		except getopt.error, msg:
			raise Usage(msg)
	
		# option processing
		for option, value in opts:
			if option in ("-h", "--help"):
				raise Usage(help_message)
		
		X = int(argv[1])   #number of successes we are trying to calculate the probability of
		n = int(argv[2])   #number of trials
		p = float(argv[3])   #probability of success
		q = (1.0 - p) # probability of failure
		
		n_min_X = n - X
		n_fact = factorial(n) # n!
		X_fact = factorial(X) # X!		

		probability = ( n_fact / ( factorial(n_min_X) * X_fact ) ) * (math.pow(p,X)) * (math.pow(q,n_min_X))

		print ""
		print "Binomial Probability Calculator v1.0.0"
		print "X = ", X, " Number of successes we are trying to calculate the probability of"
		print "n = ", n, " Number of trials"
		print "p = ", p, " Probability of success"
		print " "
		print "Binomial Probability: ", probability
		print ""
	
	except Usage, err:
		print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
		print >> sys.stderr, "\t for help use --help"
		return 2


if __name__ == "__main__":
	sys.exit(main())
