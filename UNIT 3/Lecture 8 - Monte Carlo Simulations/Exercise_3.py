#============
#Exercise 3
#============
#5/5 points (graded)
  
    if (len(L) == 0):
        return float('NaN')
    
    # compute mean first
    sumVals = 0
    for s in L:
        sumVals += len(s)
    meanVals = sumVals / len(L)

    # compute variance (average squared deviation from mean)
    sumDevSquared = 0
    for s in L:
        sumDevSquared += (len(s) - meanVals)**2
    variance = sumDevSquared / len(L)

    # standard deviation is the square root of the variance
    stdDev = variance**(.5)

    return stdDev

# using listcomps
def stdDevOfLengths(L):
    n = len(L)
    if (n == 0):
        return float('NaN')
    lengths    = [len(s) for s in L]
    mean       = sum(lengths) / n
    squaredDev = [(l-mean)**2 for l in lengths]
    variance   = sum(squaredDev) / n    
    return variance**(.5)


# using a separate function for std dev
def stdDev(X):
    mean = sum(X) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def stdDevOfLengths(L):
    n = len(L)
    if (n == 0):
        return float('NaN')
    X = []
    for s in L:
        X.append(len(s))
    return stdDev(X)