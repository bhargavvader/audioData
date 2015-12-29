import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

input_data = wav.read('amitabh_bacchan.wav')

# Number of samplepoints
N = len(input_data[1])#600
# sample spacing
T = 1.0 / input_data[0]

#N = 4410

#print input_data[0]

data = input_data[1][0:N]

yf = scipy.fftpack.fft(data*np.hanning(N))
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

plt.plot(xf, 2.0/N * np.abs(yf[:N/2]))
ydata = 2.0/N * np.abs(yf[:N/2])

index1 = np.where(ydata == max(ydata[100:]))[0][0]
print xf[index1]

index2 = np.where(ydata == max(ydata[100:index1-4]))[0][0]
print xf[index2]

print ""

print data[index1]
print data[index2]

if abs(int(round(data[index2]/data[index1]))) == 2 and int(round(xf[index1]/xf[index2])) == 2:
	print "Highest peak may be the first overtone."

else:
	freqsrounded = [int(round(freq)) for freq in xf]

	half = int(round(xf[index1]/2))

	for i in range(half - half/20, half + half/20):
		if i in freqsrounded:
			if ydata[freqsrounded.index(i)] >= ydata[index1]/3:
				print "Highest peak might be the first overtone."
				break
	else:
		print "Highest peak may be the fundamental frequency."

plt.show()