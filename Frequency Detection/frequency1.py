import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

input_data = wav.read('low_pitched_voice.wav')

# Number of samplepoints
N = len(input_data[1])#600
# sample spacing
T = 1.0 / input_data[0]

yf = scipy.fftpack.fft(input_data[1])
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

plt.plot(xf, 2.0/N * np.abs(yf[:N/2]))
ydata = 2.0/N * np.abs(yf[:N/2])

print xf[np.where(ydata == max(ydata[100:]))[0][0]]

plt.show()