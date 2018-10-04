#============
#Exercise 3-1
#============
#5/5 points (graded)
#Write a deterministic program, deterministicNumber, that returns an even number between 9 and 21.

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    # Your code here
	
	# My Answer
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10

import random
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randrange(10, 21, 2)