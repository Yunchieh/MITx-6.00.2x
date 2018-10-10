#===========
#Problem 4-1
#===========

#10.0/10.0 points (graded)
#You are given the following function and class and function specifications for the two coding problems on this page (also available in this file, die.py):

#die.py
#Write a function called makeHistogram(values, numBins, xLabel, yLabel, title=None), with the following specification:

def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a list of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axes
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
#Paste your entire function (including the definition) in the box.

#Restrictions:

#Do not paste import pylab in the box.
#You should only be using the pylab.hist, pylab.title, pylab.xlabel, pylab.ylabel, pylab.show functions from the pylab module.
#Do not leave any debugging print statements when you paste your code in the box.

def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a list of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axes
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins = numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title)
    pylab.show()

#===========	
#Problem 4-2
#===========

#20.0/20.0 points (graded)
#Write a function called getAverage(die, numRolls, numTrials), with the following specification:

def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """
#A run of numbers counts the number of times the same dice value shows up in consecutive rolls. For example:

#a dice roll of 1 4 3 has a longest run of 1
#a dice roll of 1 3 3 2 has a longest run of 2
#a dice roll of 5 4 4 4 5 5 2 5 has a longest run of 3
#When this function is called with the test case given in the file, it will return 5.312. Your simulation may give slightly different values.

#Paste your entire function (including the definition) in the box.

#Restrictions:

#Do not import or use functions or methods from pylab, numpy, or matplotlib.
#Do not leave any debugging print statements when you paste your code in the box.
#If you do not see the return value being printed when testing your function, close the histogram window.

def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """
	
    longest_runs = []
    for i in range(numTrials):
        rolls = [die.roll() for j in range(numRolls)]
        size = 1
        max_size = 0
        for i in range(len(rolls)-1):
            if rolls[i+1] == rolls[i]:
                size += 1
            else: 
                size = 1
            if max_size < size:
                max_size = size
        if max_size > 0:
            longest_runs.append(max_size)
        else:
            longest_runs.append(1)
    makeHistogram(longest_runs, numBins = 10, xLabel = 'Length of longest run', yLabel = 'frequency', title = 'Histogram of longest runs')
    return sum(longest_runs)/len(longest_runs)