import scipy.io.wavfile as wav

input_data = wav.read('testf.wav')

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

# Number of samplepoints
N = len(input_data[1])#600
# sample spacing
T = 1.0 / input_data[0]

yf = scipy.fftpack.fft(input_data[1])
yf = yf[10:]
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
print(max(2.0/N * np.abs(yf[:N/2])))
print(xf)
plt.plot(xf, 2.0/N * np.abs(yf[:N/2]))
plt.show()