from math import * 
def f(mu,sig2,x):
	return 1/sqrt(2*sig2*pi) * exp(-0.5*(x-mu)**2/sig2)

def update(mean1,var1,mean2,var2):
	new_mean=(var2 *mean1 + var1*mean2) / (var1+var2)
	new_var= 1/(1/var1 + 1/var2)
	return[new_mean,new_var]

def predict(mean1,var1,mean2,var2):
	new_mean=mean2+mean1
	new_var= var2+var1
	return [new_mean,new_var]
#print f(10.,4.,8.) 

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.
for i in range(len(measurements)):
	[mu , sig] =update(mu,sig,measurements[i],measurement_sig)
	print 'update' , [mu, sig]
	[mu , sig] =predict(mu,sig,motion[i],motion_sig)
	print 'predict' , [mu, sig]