from thinkdsp import CosSignal, SinSignal, decorate, read_wave
import matplotlib.pyplot as plt
wave = read_wave(r'C:\Users\Mia\Desktop\study\code_170255_dublie_trumpet.wav')
#wave.normalize()
#wave.make_audio()
#plt.subplot(121)
#wave.plot()
#segment = wave.segment(start=1.1, duration=0.3)
#segment.make_audio()
#plt.subplot(122)
#segment.plot()
#segment.segment(start=1.1, duration=0.005).plot()
#spectrum = segment.make_spectrum()
#plt.subplot(121)
#spectrum.plot(high=7000)
#spectrum.low_pass(4000)
#plt.subplot(122)
#spectrum.plot(high=7000)
#spectrum.high_pass(1000)
#plt.subplot(121)
#spectrum.plot(high=7000)
#spectrum.band_stop(2500,1000)
#plt.subplot(122)
#spectrum.plot(high=7000)
#plt.show()
'''
cos_sig = CosSignal(freq=440,amp=1.0,offset=0)
sin_sig = SinSignal(freq=880,amp=2.0,offset=0)

plt.subplot(231)
cos_sig.plot()
decorate(xlabel='Time (s)')

wave1 = cos_sig.make_wave(duration=1)
wave1.apodize()
wave1.make_audio()
spectrum1 = wave1.make_spectrum()
plt.subplot(232)
spectrum1.plot(high=2000)

plt.subplot(233)
sin_sig.plot()
decorate(xlabel='Time (s)')

wave2 = cos_sig.make_wave(duration=1)
wave2.apodize()
wave2.make_audio()
spectrum2 = wave2.make_spectrum()
plt.subplot(234)
spectrum2.plot(high=2000)

mix = sin_sig + cos_sig
plt.subplot(235)
decorate(xlabel='Time (s)')
mix.plot()

wave3 = mix.make_wave(duration=1)
wave3.apodize()
wave3.make_audio()
spectrum3 = wave3.make_spectrum()
plt.subplot(236)
spectrum3.plot(high=2000)
plt.show()'''

wave.normalize()
wave.make_audio()

def stretch(wave,factor):
    wave.ts *= factor
    wave.framerate /= factor
stretch(wave, 0.5)

wave.plot()
plt.show()

