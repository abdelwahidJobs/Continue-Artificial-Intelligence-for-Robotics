from math import * 
def f(mu,sig2,x):
	return 1/sqrt(2*sig2*pi) * exp(-0.5*(x-mu)**2/sig2)

def update(mean1,var1,mean2,var2):
	new_mean=(var2 *mean1 + var1*mean2) / (var1+var2)
	new_var= 1/(1/var1 + 1/var2)
	return[new_mean,new_var]

#print f(10.,4.,8.) 
print update(10.,8.,13.,2.)