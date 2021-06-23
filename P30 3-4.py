import matplotlib.pyplot as plt
from thinkdsp import decorate, read_wave

wave=read_wave(r'C:\Users\Mia\Desktop\study\code_72475__rockwehrmann__glissup02.wav')
wave.make_spectrogram(512).plot(high=5000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
plt.show()