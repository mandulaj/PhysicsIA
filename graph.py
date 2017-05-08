import numpy as np
import matplotlib.pyplot as plt
import csv


FILE_NAME = "data/10uF.csv"

data = None

with open(FILE_NAME, 'r') as f:
    csvFile = csv.reader(f)
    x = list(csvFile)
    data = np.array(x).astype('float').T

plt.figure()
plt.title("Bodeplot of frequency against amplitude")
plt.scatter((data[1]),np.log(data[2]))
plt.errorbar(data[1], np.log(data[2]), xerr=0.2, yerr=0.4)
plt.scatter((data[1]),np.log(data[3]))
plt.errorbar(data[1], np.log(data[2]), xerr=0.2, yerr=0.4)
plt.scatter((data[1]),np.log(data[4]))
plt.errorbar(data[1], np.log(data[2]), xerr=0.2, yerr=0.4)
plt.scatter((data[1]),np.log(data[5]))
plt.errorbar(data[1], np.log(data[2]), xerr=0.2, yerr=0.4)
plt.semilogx(0,0)
plt.grid(b=True, which='major', axis='both')
plt.show()
