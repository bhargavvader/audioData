# This file was taken to better understand Spectral Entropy


import numpy as np
import math
import scipy.io.wavfile as wav
from scipy import fft
from scipy import fftpack
from scipy.fftpack import dct
import matplotlib.pyplot as plt
from scipy.stats import entropy

def frame_sig(sig, framelen, framestep, winfunc=lambda x:np.ones((1,x))):
    """
    Frame a signal into overlapping frames.
    :param sig: the audio signal to frame.
    :param framelen: length of each frame measured in samples.
    :param framestep: number of samples after the start of the previous frame that the next frame should begin.
    :param winfunc: the analysis window to apply to each frame. By default no window is applied.    
    :returns: an array of frames. Size is NUMFRAMES by framelen.
    """
    slen = len(sig)
    framelen = int(round(framelen))
    framestep = int(round(framestep))

    if slen <= framelen:
        numframes = 1
    else:
        numframes = 1 + int(math.ceil((1.0 * slen - framelen) / framestep))
    
    padlen = int((numframes - 1) * framestep + framelen)
    padding = np.zeros(padlen - slen)
    padded_sig = np.concatenate((sig, padding))
    
    indices = np.tile(np.arange(0, framelen), (numframes, 1)) + np.tile(np.arange(0, numframes * framestep, framestep), (framelen, 1)).T
    indices = np.array(indices, dtype = np.int32)
    
    frames = padded_sig[indices]
    win = np.tile(winfunc(framelen), (numframes,1))
    
    return frames * win

def compPower(frames, NFFT):
    """
    Convert a value in Hertz to Mels
    :param frames: array of frames.
    :returns: Power of frequency bins in every frame.
    """
    fsig = fft(frames, NFFT)
    fsig = abs(fsig)
    x = np.linspace(0, 8000, 512)
    #print(fsig.shape)
    return fsig[:, :NFFT / 2 + 1]

def hz2mel(hz):
    """
    Convert a value in Hertz to Mels
    :param hz: a value in Hz. This can also be a numpy array, conversion proceeds element-wise.
    :returns: a value in Mels. If an array was passed in, an identical sized array is returned.
    """
    return 2595 * np.log10(1 + hz / 700.0)
    
def mel2hz(mel):
    """
    Convert a value in Mels to Hertz
    :param mel: a value in Mels. This can also be a numpy array, conversion proceeds element-wise.
    :returns: a value in Hertz. If an array was passed in, an identical sized array is returned.
    """
    return 700 * (10 ** (mel / 2595.0) - 1)

def get_filterbanks(nfilt=20,nfft=512,samplerate=16000,lowfreq=0,highfreq=None):
    """Compute a Mel-filterbank. The filters are stored in the rows, the columns correspond
    to fft bins. The filters are returned as an array of size nfilt * (nfft/2 + 1)
    :param nfilt: the number of filters in the filterbank, default 20.
    :param nfft: the FFT size. Default is 512.
    :param samplerate: the samplerate of the signal we are working with. Affects mel spacing.
    :param lowfreq: lowest band edge of mel filters, default 0 Hz
    :param highfreq: highest band edge of mel filters, default samplerate/2
    :returns: A numpy array of size nfilt * (nfft/2 + 1) containing filterbank. Each row holds 1 filter.
    """
    highfreq = highfreq or samplerate / 2
    assert highfreq <= samplerate / 2, "highfreq is greater than samplerate/2"
    
    # compute points evenly spaced in mels
    lowmel = hz2mel(lowfreq)
    highmel = hz2mel(highfreq)
    melpoints = np.linspace(lowmel,highmel,nfilt+2)
    # our points are in Hz, but we use fft bins, so we have to convert
    # from Hz to fft bin number
    bin = np.floor((nfft + 1) * mel2hz(melpoints) / samplerate)

    fbank = np.zeros([nfilt, nfft / 2 + 1])
    for j in range(0, nfilt):
        for i in range(int(bin[j]), int(bin[j + 1])):
            fbank[j,i] = (i - bin[j]) / (bin[j + 1] - bin[j])
        for i in range(int(bin[j + 1]), int(bin[j + 2])):
            fbank[j,i] = (bin[j + 2] - i) / (bin[j + 2] - bin[j + 1])
        
    return fbank

def deltas(mfcc, N):
    '''
    Finds the derivative of the mfcc passed to it
    '''
    S = mfcc.shape
    d = np.zeros((S[0], S[1]))
    for n in range(0, S[1]):
        d[:, n] = mfcc[:, (n + N / 2) % S[1]] - mfcc[:, n - N / 2] #negative indices wrap around
    d = d / N
    return d

def rms(energy):
    energy = np.mean(energy ** 2)
    return np.sqrt(energy)

def normalise(arr):
    for a in arr:
        a /= a.max()
    return arr

def main():
    """
    Read the wav file. 
    Change type to float64 for precision.
    Frame the signal.
    Compute the power.
    """

    #inputFile = ["sounds/Women/Pallavi/pallavi-angry.wav", "sounds/Women/Pallavi/pallavi-normal.wav"]
    #inputFile = ["sounds/Men/Bhargav/bhargav-normal.wav", "sounds/Men/Bhargav/bhargav-sad.wav", "sounds/Men/Bhargav/bhargav-angry.wav"]
    # inputFile = ["/Users/pallavi/BTechProject/sounds/Women/Pallavi/pallavi-normal.wav", "/Users/pallavi/BTechProject/sounds/Women/Pallavi/pallavi-angry.wav"]
    count = 1
    for tempInFile in inputFile:    
        (rate, sig) = wav.read(tempInFile)
        signal = np.float64(sig / 2 ** 15)
        frames = frame_sig(signal, 25 * rate / 1000, 10 * rate / 1000)
        signalPower = compPower(frames, 512)
        filterBanks = get_filterbanks(nfilt = 26)
        filterBankEnergies = np.dot(signalPower, filterBanks.T)
        filterBankEnergies = filterBankEnergies + 0.0000001
        filterBankEnergies = np.log10(filterBankEnergies)
        print(filterBankEnergies.max())
        mfccs = dct(filterBankEnergies)
        
        #ent = entropy(mfccs)

        x = [abs(k) for k in mfccs]
        x_ent = normalise(x)
        
        ent = entropy(x_ent)
        if(count == 1):
            l = 'Normal'
            count = 2
        else:
            l = 'Angry'
        print(ent.min(), ent.max(), tempInFile)
        
        plt.plot(ent, label = l)

        deltaOne = deltas(mfccs[:, 3:15], 2)
        deltaTwo = deltas(deltaOne, 2)

    plt.title("Spectral entropy")
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()

if __name__ == "__main__":
    main()