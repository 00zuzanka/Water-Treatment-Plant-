import numpy as np
import matplotlib.pyplot as plt

filename_1 = 'adjusted_turbidity.csv'
filename_2 = 'BEFORE_filtration.csv'
filename_3 = 'AFTER_filtration.csv'

data_1 = np.loadtxt(filename_1, delimiter=',', usecols=[1,2,3,4])
data_2 = np.loadtxt(filename_2, delimiter=',', usecols=[1,2,3,4])
data_3 = np.loadtxt(filename_3, delimiter=',', usecols=[1,2,3,4])

#turbidity_before_filtration
array_before_turbidity = np.array(data_1[:,0])  # convert list to array
mean_before_turbidity = np.mean(array_before_turbidity)    # compute mean value
std_before_turbidity = np.std(array_before_turbidity)      # compute std value
number_before_turbidity = len(array_before_turbidity)      # number of values
# Scatterplot 1:
plt.scatter(np.ones(number_before_turbidity), array_before_turbidity, s=80, facecolor='none', edgecolor='r')
# Boxplot 1:
plt.boxplot([array_before_turbidity],labels=['Sample dataset'])
# Plot 1:
plt.title('Water Turbidity before Filtration')
plt.ylabel('[NTU]')
plt.savefig('Turbidity_before_filtration')
plt.show()


#Temperature_before_filtration
array_before_TE = np.array(data_2[:,1])     # convert list to array
mean_before_TE = np.mean(array_before_TE)   # compute mean value
std_before_TE = np.std(array_before_TE)     # compute std value
number_before_TE = len(array_before_TE)     # number of values
# Scatterplot 2:
plt.scatter(np.ones(number_before_TE), array_before_TE, s=80, facecolor='none', edgecolor='r')
# Boxplot 2:
plt.boxplot([array_before_TE], labels=['Sample dataset'])
# Plot2:
plt.title('Water Temperature before Filtration')
plt.ylabel('[\u00b0C]')
plt.savefig('TE_before_filtration')
plt.show()

#EC_before_filtration
array_before_EC = np.array(data_2[:,2])     # convert list to array
mean_before_EC = np.mean(array_before_EC)   # compute mean value
std_before_EC = np.std(array_before_EC)     # compute std value
number_before_EC = len(array_before_EC)     # number of values
# Scatterplot 3:
plt.scatter(np.ones(number_before_EC), array_before_EC, s=80, facecolor='none', edgecolor='r')
# Boxplot 3:
plt.boxplot([array_before_EC], labels=['Sample dataset'])
# Plot3:
plt.title('Electrical Conductivity of Water before Filtration')
plt.ylabel('[$\mu$S/cm]')
plt.savefig('EC_before_filtration')
plt.show()

#pH_before_filtration
array_before_pH = np.array(data_2[:,3])     # convert list to array
mean_before_pH = np.mean(array_before_pH)   # compute mean value
std_before_pH = np.std(array_before_pH)     # compute std value
number_before_pH = len(array_before_pH)     # number of values
# Scatterplot 4:
plt.scatter(np.ones(number_before_pH), array_before_pH, s=80, facecolor='none', edgecolor='r')
# Boxplot 4:
plt.boxplot([array_before_pH], labels=['Sample dataset'])
# Plot4:
plt.title('Water pH before Filtration')
plt.ylabel('[pH]')
plt.savefig('pH_before_filtration')
plt.show()

#turbidity_after_filtration
array_after_turbidity = np.array(data_3[:,0])           # convert list to array
mean_after_turbidity = np.mean(array_after_turbidity)   # compute mean value
std_after_turbidity = np.std(array_after_turbidity)     # compute std value
number_after_turbidity = len(array_after_turbidity)    # number of values
# Scatterplot 5:
plt.scatter(np.ones(number_after_turbidity),array_after_turbidity, s=80, facecolor='none', edgecolor='r')
# Boxplot 5:
plt.boxplot([array_after_turbidity], labels=['Sample dataset'])
# Plot5:
plt.title('Water Turbidity after filtration')
plt.ylabel('[NTU]')
plt.savefig('turbidity_after_filtration')
plt.show()

#Temperature_after_filtration
array_after_TE = np.array(data_3[:,1])    # convert list to array
mean_after_TE = np.mean(array_after_TE)      # compute mean value
std_after_TE = np.std(array_after_TE)        # compute std value
number_after_TE = len(array_after_TE)        # number of values
# Scatterplot 6:
plt.scatter(np.ones(number_after_TE), array_after_TE, s=80, facecolor='none', edgecolor='r')
# Boxplot 6:
plt.boxplot([array_after_TE], labels=['Sample dataset'])
# Plot 6:
plt.title('Water Temperature after Filtration')
plt.ylabel('[\u00b0C]')
plt.savefig('TE_after_filtration')
plt.show()

#EC_after_filtration
array_after_EC = np.array(data_3[:,2])    # convert list to array
mean_after_EC = np.mean(array_after_EC)   # compute mean value
std_after_EC = np.std(array_after_EC)     # compute std value
number_after_EC = len(array_after_EC)     # number of values
# Scatterplot 7:
plt.scatter(np.ones(number_after_EC), array_after_EC, s=80, facecolor='none', edgecolor='r')
# Boxplot 7:
plt.boxplot([array_after_EC], labels=['Sample dataset'])
# Plot 7:
plt.title('Electrical Conductivity of Water after Filtration')
plt.ylabel('[$\mu$S/cm]')
plt.savefig('EC_after_filtration')
plt.show()

#pH_after_filtration
array_after_pH = np.array(data_3[:,3])    # convert list to array
mean_after_pH = np.mean(array_after_pH)   # compute mean value
std_after_pH = np.std(array_after_pH)     # compute std value
number_after_pH = len(array_after_pH)     # number of values
# Scatterplot 8:
plt.scatter(np.ones(number_after_pH), array_after_pH, s=80, facecolor='none', edgecolor='r')
# Boxplot 8:
plt.boxplot([array_after_pH], labels=['Sample dataset'])
# Plot 8:
plt.title('Water pH after Filtration')
plt.ylabel('[pH]')
plt.savefig('pH_after_filtration')
plt.show()