import numpy as np
from stdev_code import stdev_p
from stdev_code import stdev_s
from random import uniform
import time

# data generator, use uniform random generator
data=[]
index=0
while index<1000:
    data.append(uniform(0,50000000000))
    index+=1

# get real value by numpy
target_population = np.std(data, ddof=0)
target_sample = np.std(data, ddof=1)

time_p = time.time()
real_population = stdev_p(data) # calculated value by code

time_p = time.time()-time_p
time_s = time.time()
real_sample=stdev_s(data)
time_s = time.time()-time_s

# compare two floats
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


print "Real stdev_p by Numpy is:" + str(real_population)
print "Calculated stdev_p by your code is:" + str(target_population)
print "Time spent for stdev_p is:" + str(time_p)+' s'
print "Real stdev_s by Numpy is:" + str(real_sample)
print "Calculated stdev_s by your code is:" + str(target_sample)
print "Time spent for stdev_s is:" + str(time_s)+' s'

if isclose(real_population,target_population):
    print 'Population STDEV is correct'

if isclose(real_population,target_population)==False:
    print 'Population STDEV is wrong'

if isclose(real_sample,target_sample):
    print 'Sample STDEV is correct'

if isclose(real_sample,target_sample)==False:
    print 'Sample STDEV is wrong'

if time_p>=1:
    print 'Population STDEV is time out'

if time_s>=1:
    print 'Sample STDEV is time out'