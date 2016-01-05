import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np
from numpy.random import normal
import wave

data = np.array(wav.read('two-sec_rowling.wav')[1])
mean = np.mean(data)
print 'Mean', mean
cdata = (data-mean)**2
norm =0
for index in range(len(cdata)):
	norm+=cdata

dataf = (data-mean)/norm
dataf = dataf * np.hanning(len(data))

count, ind = 0,0

#for index in range(len(dataf)):
d = dataf[ind:ind+len(dataf)*0.375]
	# ind += len(dataf)*0.125
	# count +=1
autocorr = np.correlate(d, d, mode='full')  # Correlate function
#autocorr = np.corrcoef(d, d, rowvar = 1)    # Corrcoef function
autocorr /= autocorr.max()

plt.plot(autocorr)
plt.title('Autocorrelation plot')
plt.show()



