import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np
from numpy.random import normal
import wave

data = np.array(wav.read('test_music.wav')[1])
# data = data[len(data)*0.3:len(data)*0.7]
# data = normal(0, 1, 1000)

# return values are lags, correlation vector and the drawn line
lags, corr, line, rest = plt.acorr(data, marker=None, linestyle='-', color='red', usevlines=False)
plt.title('Autocorrelation plot')
plt.show()
