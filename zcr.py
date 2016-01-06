import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np
import wave

data = np.array(wav.read('six-sec_kalam.wav')[1])

zcr_array = []

#Function to find zero crossing rate
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
	x = 0
	for i in range(len(signal)):
		x = x+(signal[i]*signal[i])
	x = np.sqrt(x)
	return x 

# Finding Autocorrelation coefficient of the signal
def autocorcoef(signal):
	signal = signal[len(signal)*0.06:len(signal)*0.8]
#	autocorr = np.corrcoef(d, d, rowvar = 1)    # Corrcoef function
	autocorr = np.correlate(signal, signal, mode='full')  # Correlate function
#	autocorr = autocorr[len(autocorr)*0.06:len(autocorr)*0.8]
#	print(autocorr)
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
	# auto.append(autocorcoef(d))

# Variance of ZCR
var_array = []
# for i in zcr_array:
for i in range(0, (len(zcr_array)/50)):
	try:
		var_array.append(np.std(zcr_array[i*50:(i*50)+50])**2)
	except:
		continue

print "Mean of Variance of Zero Crossing Rate", np.mean(var_array)

# plt.plot(auto)
# plt.show()

# Low Energy Frames 
# for i in signal:
# 	rms_array = rms_array.append(rms(data[ind:ind+44100]))
# 	mean(rms_array)
# 	ind+=44100
# 	plt.plot(mean)
#	plt.show()

# print "Zero Crossing Rate", zcr(data)
# print "RMS power", rms(data)
# print "Average Zero Crossing rate for 20 ms is", s/count
# print "Autocorrelation coefficient", max(auto)


# paradise avg zcr = 3330	380
# pakguy avg zcr = 1090		123
# paradise2 avg zcr = 3053  346
# jkrowling avg zcr = 1832  208
