import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

input_data = wav.read('low_pitched_voice.wav')

# Number of samplepoints
N = len(input_data[1])#600
# sample spacing
T = 1.0 / input_data[0]

ps = np.abs(np.fft.fft(input_data[1]))**2
freqs = np.fft.fftfreq(N, T)
idx = np.argsort(freqs)

plt.plot(freqs[idx], ps[idx])

plt.show()