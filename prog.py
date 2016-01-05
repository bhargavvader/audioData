import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np

input_data = wav.read('test2.wav')
audio = input_data[1]
audio = audio - audio.mean()
rate = input_data[0]

plt.plot(audio)

plt.ylabel("Amplitude")
plt.xlabel("Array Index")

print "Maximum amplitude: ", max(audio)
print "Minimum amplitude: ", min(audio)
print "Average amplitude: ", np.mean(audio)
s = np.std(audio)
print "Variance: ", s**2
print "Standard deviation: ", s
lenS = len(audio)
print("Size of Audio file is:", lenS)

amplitude_threshold = 200
window_size = 200
time = lenS/rate
averages = []
print("Time of file is:", time)
#### identifying the beginning baseline details
for i in range(10,1000):
	if abs(audio[0:1000]).mean() > 1000:
		noise = 0
		break
	beg_sample = rate/(i/10)
	beg_audio = audio[:beg_sample]
	if beg_audio.max() > 500:
		# print(beg_audio.max(),i)
		continue
	if beg_audio.max() < 500:
		# print(beg_audio.max())
		noise = abs(beg_audio).mean()
		break
print(i, "This is the baseline")
print("Noise to be cancelled is: ", noise)
# plt.show()
audio = audio - noise

for i in range(0, len(audio) - window_size):
	averages.append(np.mean(audio[i:i+window_size]))


# print len(averages)
print('start checking')
for i in range(len(averages)):
	if averages[i] < amplitude_threshold and averages[i] > (0-amplitude_threshold):
		averages[i] = 'x'
	else:
		pass

c = 0
c_limit = 15000
# choose c_limit depending on samplign rate
# if c_limit = 10,000 - then if 10000 windows in a row are 'silence', then it is called a silence
# for example, if it is 10,000, then the gap it requires to find a silence is 200+10000, which is sampling rate is 44,100, is 0.25 of a second
break_in_silence = True

for i in range(len(averages)):
	if averages[i] == 'x':
		c += 1
		if c > c_limit:
			if break_in_silence == True:
				print i, 
				break_in_silence = False

			c = 0
	else:
		if break_in_silence == False:
			print "to", i
		break_in_silence = True
		c = 0

plt.show()