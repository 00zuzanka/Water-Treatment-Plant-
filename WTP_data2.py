import numpy as np
import matplotlib.pyplot as plt

filename_1 = 'adjusted_turbidity.csv'
filename_2 = 'BEFORE_filtration.csv'
filename_3 = 'AFTER_filtration.csv'

data_1 = np.loadtxt(filename_1, delimiter=',', usecols=[1,2,3,4])
data_2 = np.loadtxt(filename_2, delimiter=',', usecols=[1,2,3,4])
data_3 = np.loadtxt(filename_3, delimiter=',', usecols=[1,2,3,4])


# Turbidity before and after filtration
# BEFORE:
array_before_turbidity = np.array(data_1[:,0])  # convert list to array
mean_before_turbidity = np.mean(array_before_turbidity)    # compute mean value
std_before_turbidity = np.std(array_before_turbidity)      # compute std value
number_before_turbidity = len(array_before_turbidity)      # number of values
# AFTER:
array_after_turbidity = np.array(data_3[:,0])           # convert list to array
mean_after_turbidity = np.mean(array_after_turbidity)   # compute mean value
std_after_turbidity = np.std(array_after_turbidity)     # compute std value
number_after_turbidity = len(array_after_turbidity)    # number of values

# Scatterplot 1:
plt.scatter(np.ones(number_before_turbidity), array_before_turbidity, s=80, facecolor='none', edgecolor='r')
plt.scatter(np.ones(number_after_turbidity)*2,array_after_turbidity, s=80, facecolor='none', edgecolor='r')

# Boxplot 1:
plt.boxplot([array_before_turbidity, array_after_turbidity],labels=['Before', 'After'])
# Plot 1:
plt.title('Effect of Filtration on Water Turbidity')
plt.ylabel('[NTU]')
plt.savefig('Turbidity_filtration')
plt.show()


# Temperature before and after filtration
# BEFORE:
array_before_TE = np.array(data_2[:,1])     # convert list to array
mean_before_TE = np.mean(array_before_TE)   # compute mean value
std_before_TE = np.std(array_before_TE)     # compute std value
number_before_TE = len(array_before_TE)     # number of values
# AFTER:
array_after_TE = np.array(data_3[:,1])    # convert list to array
mean_after_TE = np.mean(array_after_TE)      # compute mean value
std_after_TE = np.std(array_after_TE)        # compute std value
number_after_TE = len(array_after_TE)        # number of values
# Scatterplot 2:
plt.scatter(np.ones(number_before_TE), array_before_TE, s=80, facecolor='none', edgecolor='r')
plt.scatter(np.ones(number_after_TE)*2, array_after_TE, s=80, facecolor='none', edgecolor='r')

# Boxplot 2:
plt.boxplot([array_before_TE,array_after_TE], labels=['Before', 'After'])
# Plot2:
plt.title('Effect of Filtration on Water Temperature')
plt.ylabel('[\u00b0C]')
plt.savefig('TE_filtration')
plt.show()


# Electrical Conductivity before and after filtration
# BEFORE:
array_before_EC = np.array(data_2[:,2])     # convert list to array
mean_before_EC = np.mean(array_before_EC)   # compute mean value
std_before_EC = np.std(array_before_EC)     # compute std value
number_before_EC = len(array_before_EC)     # number of values
# AFTER:
array_after_EC = np.array(data_3[:,2])    # convert list to array
mean_after_EC = np.mean(array_after_EC)   # compute mean value
std_after_EC = np.std(array_after_EC)     # compute std value
number_after_EC = len(array_after_EC)     # number of values
# Scatterplot 3:
plt.scatter(np.ones(number_before_EC), array_before_EC, s=80, facecolor='none', edgecolor='r')
plt.scatter(np.ones(number_after_EC)*2, array_after_EC, s=80, facecolor='none', edgecolor='r')

# Boxplot 3:
plt.boxplot([array_before_EC,array_after_EC], labels=['Before', 'After'])
# Plot3:
plt.title('Effect of Filtration on Electrical Conductivity of Water')
plt.ylabel('[$\mu$S/cm]')
plt.savefig('EC_filtration')
plt.show()


# pH before and after filtration
# BEFORE:
array_before_pH = np.array(data_2[:,3])     # convert list to array
mean_before_pH = np.mean(array_before_pH)   # compute mean value
std_before_pH = np.std(array_before_pH)     # compute std value
number_before_pH = len(array_before_pH)     # number of values
# AFTER:
array_after_pH = np.array(data_3[:,3])    # convert list to array
mean_after_pH = np.mean(array_after_pH)   # compute mean value
std_after_pH = np.std(array_after_pH)     # compute std value
number_after_pH = len(array_after_pH)     # number of values
# Scatterplot 4:
plt.scatter(np.ones(number_before_pH), array_before_pH, s=80, facecolor='none', edgecolor='r')
plt.scatter(np.ones(number_after_pH)*2, array_after_pH, s=80, facecolor='none', edgecolor='r')

# Boxplot 4:
plt.boxplot([array_before_pH, array_after_pH], labels=['Before', 'After'])
# Plot 4:
plt.title('Effect of Filtration on Water pH')
plt.ylabel('[pH]')
plt.savefig('pH_filtration')
plt.show()

# Data size check:
# print(len(array_before_turbidity), len(array_after_turbidity), len(array_before_TE), len(array_after_TE), len(array_before_EC), len(array_after_EC), len(array_before_pH), len(array_after_pH))

# RESULTS - MEDIANS:
#print(mean_before_turbidity, mean_after_turbidity,mean_before_TE,mean_after_TE, mean_before_EC, mean_after_EC, mean_before_pH, mean_after_pH)

results = [mean_before_turbidity, mean_after_turbidity, mean_before_TE, mean_after_TE, mean_before_EC, mean_after_EC, mean_before_pH, mean_after_pH]

formatted_results = ["%.1f" % value for value in results]
print("turbidity    | temp.   | conduct.  | pH ")
print(*formatted_results)
