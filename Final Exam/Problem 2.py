#=================
#Final - Problem 2
#=================

#Consider the following code:

import random, pylab
xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals

#For each of the following questions, select the best answer from the set of choices.

#Problem 2-1

#2.0/2.0 points (graded)
#The values in tVals are most closely:

Distributed with a Gaussian distribution 

#Problem 2-2

#2.0/2.0 points (graded)
#The values in xVals are most closely:

Uniformly distributed

#For each of the following expressions using the code above, match the following calls to pylab.plot with one of the graphs shown below.

#You can click on the following images to view a larger size.

#Problem 2-3

#2.0/2.0 points (graded)
#pylab.plot(xVals, zVals)

Graph 5

#Problem 2-4

#2.0/2.0 points (graded)
#pylab.plot(xVals, yVals)

Graph 4

#Problem 2-5

#2.0/2.0 points (graded)
#pylab.plot(xVals, sorted(yVals))

Graph 3

#Problem 2-6

#2.0/2.0 points (graded)
#pylab.plot(sorted(xVals), yVals)

Graph 2

#Problem 2-7

#2.0/2.0 points (graded)
#pylab.plot(sorted(xVals), sorted(yVals))

Graph 1
