import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

def handler(freq_to_use, xf, ydata, message):
	print "f = ", freq_to_use
	print "2f = ", 2*freq_to_use
	print "3f = ", 3*freq_to_use
	print "4f = ", 4*freq_to_use
	mb2f4f = detect_max_between(2*freq_to_use + 40, 4*freq_to_use - 40, xf, ydata)
	mb3f5f = detect_max_between(3*freq_to_use + 40, 5*freq_to_use - 40, xf, ydata)
	print mb2f4f, mb3f5f
	if approximately_equal(mb2f4f, 3*freq_to_use) and approximately_equal(mb3f5f, 4*freq_to_use):
		print "Highest peak is the " + message +"."
	elif approximately_equal(mb2f4f, 3*freq_to_use) or approximately_equal(mb3f5f, 4*freq_to_use):
		print "Highest peak may be the " + message +"."
	else:
		print "Highest peak might be the " + message +"."

def approximately_equal(f1, f2):
	if abs(f2 - f1) <=10:
		return True
	return False

def detect_max_between(f1, f2, freqs, powers):
	maxpow = 0
	j = 0
	for i in range(len(freqs)):
		if freqs[i] >= f1 and freqs[i] <= f2 and powers[i] > maxpow:
			maxpow = powers[i]
			ret = freqs[i]
	return ret

input_data = wav.read('testf.wav')

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
#print xf[index1]

index2 = np.where(ydata == max(ydata[100:index1-4]))[0][0]
#print xf[index2]

#print ""


if abs(int(round(data[index2]/data[index1]))) == 2 and int(round(xf[index1]/xf[index2])) == 2:
	freq_to_use = xf[index2]
	handler(freq_to_use, xf, ydata, "first overtone")
else:
	freqsrounded = [int(round(freq)) for freq in xf]
	half = int(round(xf[index1]/2))
	for i in range(half - half/20, half + half/20):
		if i in freqsrounded:
			if ydata[freqsrounded.index(i)] >= ydata[index1]/3:
				freq_to_use = xf[index2]
				handler(freq_to_use, xf, ydata, "first overtone")
				break
	else:
		freq_to_use = xf[index1]
		handler(freq_to_use, xf, ydata, "fundamental frequency")

if(freq_to_use >= 85 and freq_to_use <= 165):
	print "Male voice"
elif(freq_to_use > 165 and freq_to_use <= 180):
	print "Ambiguous, mostly male"
elif(freq_to_use > 180 and freq_to_use <= 260):
	print "Female voice"
else:
	print "Not speech"

plt.show()