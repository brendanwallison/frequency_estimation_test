import numpy as np
from scipy import signal
from scipy import io
import matplotlib.pyplot as plt
rng = np.random.default_rng()

sr, test = io.wavfile.read("after0.wav")
f, Pxx_den = signal.welch(test, sr)

m = np.mean(test)
s = np.std(test)
test2 = (test - m)/s
f, Pxx_den = signal.welch(test2, sr)

plt.semilogy(f, Pxx_den)
#plt.ylim([1e-7, 1e2])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()


print(np.max(f[Pxx_den > 0.05]))
print(np.min(f[Pxx_den > 0.05]))

sr, test = io.wavfile.read("before0.wav")
test = test[:,1] # just first channel
f, Pxx_den = signal.welch(test, sr)
plt.semilogy(f, Pxx_den)
#plt.ylim([1e-7, 1e2])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()


m = np.mean(test)
s = np.std(test)
test2 = (test - m)/s
f, Pxx_den = signal.welch(test2, sr)

plt.semilogy(f, Pxx_den)
#plt.ylim([1e-7, 1e2])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()


np.max(f[Pxx_den > 0.05])
np.min(f[Pxx_den > 0.05])





print("DONE")