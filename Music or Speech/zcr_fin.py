import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np
import wave

music, speech = 0, 0
data = np.array(wav.read('six-msec_jefferson2.wav')[1])

zcr_array = []

# Function to find zero crossing rate
def zcr(signal):
	zc = 0;
	for i in range(len(signal)):
   		if signal[i]*signal[i-1] < 0:
   			zc = zc+1
   	return zc

def avg(signal):
	avg = sum(signal)/len(signal)
	return avg

# Function to find rms value of signal
def rms(signal):
	x, temp = 0, 0
	for i in range(len(signal)):
		temp1 = temp
		temp = signal[i]*signal[i]
		if temp<0:
			x = x+temp1
			temp = temp1
		else:
			x = x+temp
	x = np.sqrt(x)
	return x 

# Finding Autocorrelation coefficient of the signal
def autocorcoef(signal):
	signal = signal[len(signal)*0.06:len(signal)*0.8]
#	autocorr = np.corrcoef(d, d, rowvar = 1)    # Corrcoef function
	autocorr = np.correlate(signal, signal, mode='full')  # Correlate function
	return max(autocorr)

s, count, ind, variance = 0, 0, 0, 0
auto =[]

#for index in range(len(data)):
while ind+882<len(data):
	d = data[ind:ind+882]
	x=zcr(d)
	s = s + x
	zcr_array.append(x)
	ind += 441
	count+=1
	auto.append(autocorcoef(d))

# Variance of ZCR
var_array = []
# for i in zcr_array:
for i in range(0, (len(zcr_array)/50)):
	try:
		var_array.append(np.std(zcr_array[i*50:(i*50)+50])**2)
	except:
		continue

var_mean = np.mean(var_array)

ind, i = 0, 0
rms_array = []
fifty = []
signal_rms = []

# Low Energy Frames
while i<=(len(data)-882):
	signal_rms.append(rms(data[i:i+882]))
	i+=441

plt.plot(signal_rms)

print "Mean of Variance of Zero Crossing Rate", var_mean
print "Mean of rms values", np.mean(signal_rms)
var_rms = np.std(signal_rms)**2
print "Variance of rms values", var_rms

fifty = [0]*50

i=50

# Calculating 50% local mean rms power
while i<=(len(signal_rms)):
	fifty.append(np.mean(signal_rms[i-50:i])*0.9)
	i+=1

plt.plot(fifty)
# plt.show()


# print "Zero Crossing Rate", zcr(data)
# print "RMS power", rms(data)
# print "Average Zero Crossing rate for 20 ms is", s/count
# print "Autocorrelation coefficient", max(auto)