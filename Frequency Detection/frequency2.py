import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

input_data = wav.read('.wav')

# Number of samplepoints
N = len(input_data[1])#600
# sample spacing
T = 1.0 / input_data[0]

window_length = 4410

freqlist = []

for i in range(0, N - window_length, window_length):
	data = input_data[1][i:i+window_length]

	ps = np.abs(np.fft.fft(data*np.hanning(window_length)))**2
	freqs = np.fft.fftfreq(window_length, T)
	idx = np.argsort(freqs)

	freqs = freqs[idx]
	ps = ps[idx]

	freqs = freqs[len(freqs)/2:]
	ps = ps[len(ps)/2:]

	# plt.plot(freqs, ps)
	# plt.show()

	index = np.where(ps==max(ps))[0][0]

	try:
		princi = freqs[np.where(ps == max(ps[:index-10]))[0][0]]
		freqlist.append(princi)
	except:
		pass

	f = freqs[index]

	

print freqlist
print np.mean(freqlist)
print len(freqlist)