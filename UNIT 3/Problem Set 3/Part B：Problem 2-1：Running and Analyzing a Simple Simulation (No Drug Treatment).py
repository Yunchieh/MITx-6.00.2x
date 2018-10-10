#==================================================================================
#Part B: Problem 2-1: Running and Analyzing a Simple Simulation (No Drug Treatment)
#==================================================================================

#10.0/10.0 points (graded)
#You should start by understanding the population dynamics before introducing any drug.

#Fill in the function simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials) that instantiates a Patient, simulates changes to the virus population for 300 time steps (i.e., 300 calls to update), and plots the average size of the virus population as a function of time; that is, the x-axis should correspond to the number of elapsed time steps, and the y-axis should correspond to the average size of the virus population in the patient. The population at time=0 is the population after the first call to update.

#Run the simulation for numTrials trials, where numTrials in this case can be up to 100 trials. Use pylab to produce a plot (with a single curve) that displays the average result of running the simulation for many trials. Make sure you run enough trials so that the resulting plot does not change much in terms of shape and time steps taken for the average size of the virus population to become stable. Don't forget to include axes labels, a legend for the curve, and a title on your plot.

#You should call simulationWithoutDrug with the following parameters:

#numViruses = 100

#maxPop (maximum sustainable virus population) = 1000

#maxBirthProb (maximum reproduction probability for a virus particle) = 0.1

#clearProb (maximum clearance probability for a virus particle) = 0.05

#Thus, your simulation should be instantiatating one Patient with a list of 100 SimpleVirus instances. Each SimpleVirus instance in the viruses list should be initialized with the proper values for maxBirthProb and clearProb.

#Hint: graphing

#Consult reference documentation on pylab as reference. Scroll down on the page to find a list of all the plotting commands in pylab.

#Hint: testing your simulation

#For further testing, we have provided the .pyc (compiled Python) files for the completed Patient and SimpleVirus classes (and for Problem 5, the ResistantVirus and TreatedPatient classes) that you can use to confirm that your code is generating the correct results during simulation.

#If you comment out your versions of these classes in ps3b.py, and add the following import statements to the top of your file, you can run the simulation using our pre-compiled implementation of these classes to make sure you are obtaining the correct results. This is a good way to test if you've implemented these classes correctly. Make sure to comment out the import statement and uncomment your implementations before moving to Problem 4.

#Notes:

#If you want to use numpy arrays, you should import numpy as np and use np.METHOD_NAME in your code.
#Use this code in the grader, to plot: 
pylab.plot(YOUR_Y_AXIS_VALUES, label = "SimpleVirus")
pylab.title("SimpleVirus simulation")
pylab.xlabel("Time Steps")
pylab.ylabel("Average Virus Population")
pylab.legend(loc = "best")
pylab.show()
        
#For Python 3.5: from ps3b_precompiled_35 import *

#For Python 3.6: from ps3b_precompiled_36 import *

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.
    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    viruses = [SimpleVirus(maxBirthProb, clearProb) for i in range(numViruses)]
    tot = [0]*300
    for trial in range(numTrials):
        patient = Patient(viruses, maxPop)
        for i in range(300):
            tot[i] += patient.update()            
    tot = [tot[i]/numTrials for i in range(300)]
    
    pylab.plot(tot, label = "SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()
	
#===================
#Part B: Problem 2-2
#===================

#5.0/5.0 points (graded)
#A good question to consider as you look at your plot is: about how long does it take before the population stops growing?

About 150 time-steps