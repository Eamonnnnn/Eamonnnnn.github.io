from thinkdsp import Chirp
from thinkdsp import decorate
import numpy as np
import matplotlib.pyplot as plt

PI2 = 2 * np.pi

class TromboneGliss(Chirp):
    
    def evaluate(self, ts):

        l1, l2 = 1.0 / self.start, 1.0 / self.end
        lengths = np.linspace(l1, l2, len(ts))
        freqs = 1 / lengths
        
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        ys = self.amp * np.cos(phases)
        return ys

low = 262
high = 349
signal = TromboneGliss(high, low)
wave1 = signal.make_wave(duration=1)
signal = TromboneGliss(low, high)
wave2 = signal.make_wave(duration=1)
wave = wave1 | wave2
sp = wave.make_spectrogram(1024)
sp.plot(high=1000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
plt.show()