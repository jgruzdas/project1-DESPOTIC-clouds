########################################################################
# 
# single_cloud.py
#
#test code to compute and print 
#Temperatures, Abundances, and Luminosities of the emitters CO, C+, C, O
#using NL99_GC chemistry network included DESPOTIC2
#
########################################################################

########################################################################
# Program code
########################################################################

# Import the despotic library
from despotic import cloud_f

# Import standard python libraries
from numpy import *
from matplotlib.pyplot import *
from datetime import datetime
from datetime import timedelta
#from despotic.chemistry import NL99
from despotic.chemistry import NL99_GC

###

# Read the Test Cloud file
#testcloud = cloud(fileName='../cloudfiles/MilkyWayGMC.desp')
testcloud = cloud_f.cloud_f2(fileName='../cloudfiles/testcloud.desp')

#if want interactive mode:
#import code
#code.interact(local=locals())

#from despotic.chemistry import abundanceDict


# Lower the CR ionization rate so that a fully CO composition becomes
# possible
testcloud.rad.ionRate = 2e-17

# Raise the temperature to 20 K
testcloud.Tg = 20.0

#Simultaneous Chemical and Thermal Equilibria
abd=[]
#logNH = np.arange(23., 23.01, 0.025)
testcloud.colDen = 10.**23.
#testcloud.setChemEq(network=NL99_GC, evolveTemp='iterateDust', verbose=True)
testcloud.setChemEq(network=NL99_GC, evolveTemp='iterateDust')
abd.append(testcloud.chemnetwork.abundances)
#print abd


# Compute the luminosity of the CO lines
testcloudlineco = testcloud.lineLum('co')
# Compute the luminosity of the c+, c, o lines
testcloudlinecp = testcloud.lineLum('c+')
testcloudlinec = testcloud.lineLum('c')
testcloudlineo = testcloud.lineLum('o')

#print found gas and dust temperatures
print "Temperatures: "
print "Tg = ", testcloud.Tg
print "Td = ", testcloud.Td

# Print abundance of the species C+, C, O, CO
print ""
print "Abundances: "
xCO = []
xCp = []
xC = []
xO = []
for ab in abd:
    xCO.append(ab['CO'])
    xCp.append(ab['C+'])
    xC.append(ab['C'])
    xO.append(ab['O'])

print "CO = ", xCO
print "C+ = ", xCp
print "C = ", xC
print "O = ", xO
#print abd.abundances["CO"]

# Print luminosities of the species C+, C, O, CO
print ""
print "Luminosities: "
testcloudcoTBint=array([line['intTB'] for line in testcloudlineco])
testcloudcpTBint=array([line['intTB'] for line in testcloudlinecp])
testcloudcTBint=array([line['intTB'] for line in testcloudlinec])
testcloudoTBint=array([line['intTB'] for line in testcloudlineo])
print "CO first 5 J transitions: ", testcloudcoTBint[0:5]
print "C+: ", testcloudcpTBint[0]
print "C : ", testcloudcTBint[0]
print "O : ", testcloudoTBint[0]
#print testcloudlinecplus["C+"]








