import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np
import wave

data = np.array(wav.read('../WAV files/six-sec_steve.wav')[1])

zcr_array = []

#Function to find zero crossing rate
def zcr(signal):
	zc = 0
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
		x = x+(signal[i]**2)
	x = np.sqrt(x)
	return x 

s, count, ind, variance = 0, 0, 0, 0
auto =[]

#for index in range(len(data)):
while ind+882<len(data):
	d = data[ind:ind+882]
	x=zcr(d)
	s = s + x
	zcr_array.append(x)
	ind += 882
	count+=1
	# auto.append(autocorcoef(d))

# Variance of ZCR
var_array = []
for i in range(0, (len(zcr_array)/50)):
	try:
		var_array.append(np.std(zcr_array[i*50:(i*50)+50])**2)
	except:
		continue

print "Mean of Variance of Zero Crossing Rate", np.mean(var_array)

rms_array = []
ind = 0
while ind+882<len(data):
	r = rms(data[ind:ind+882])
	rms_array.append(r)
	ind += 882

plt.plot(rms_array)

redline = [0]*50
ind = 50
while ind < len(rms_array):
	redline.append(np.mean(rms_array[ind-50:ind])/2)
	ind += 1

dips = 0
total = 0
for i in range(50, len(rms_array)):
	if rms_array[i] < redline[i]:
		dips += 1
	total += 1

print str(100.0*dips/total) + " % low energy frames"

plt.plot(redline)
#plt.show()

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