from math import * 
def f(mu,sig2,x):
	return 1/sqrt(2*sig2*pi) * exp(-0.5*(x-mu)**2/sig2)

print f(10.,4.,8.) 