import numpy as np
from scipy import signal
from scipy import io
import matplotlib.pyplot as plt
rng = np.random.default_rng()

### LOOK AT TESTING.IPYNB INSTEAD OF THIS ###
# This is initial experimentation with simple thresholding of the power spectra, which seems ineffective at least without further pre-processing/experimentation #

# We first calibrate our thresholds to an expert judgment.
# This should be done with multiple examples, but we'll do it with one
sr, test = io.wavfile.read("Peak Frequencies/After/6179876__S4A03508_20170502_124702.wav")
m = np.mean(test)
s = np.std(test)
test2 = (test - m)/s
f, Pxx_den = signal.welch(test2, sr)
# f[88] is 7579.6 to 7665.8, corresponding to the expert judgment
# Pxx_den[88] is 6.99802113884239e-06
# Threshold is 6.99e-06
print(np.max(f[Pxx_den > 6.99e-6]))
print(np.min(f[Pxx_den > 6.99e-6]))

# Now test against a couple of examples
sr, test = io.wavfile.read("Peak Frequencies/After/b2y16kbs1_20160413_100000_2973.wav")
m = np.mean(test)
s = np.std(test)
test2 = (test - m)/s
f, Pxx_den = signal.welch(test2, sr)
# f[88] is 7579.6 to 7665.8, corresponding to the expert judgment
# Pxx_den[88] is 6.99802113884239e-06
# Threshold is 6.99e-06
print(np.max(f[Pxx_den > 6.99e-6]))
print(np.min(f[Pxx_den > 6.99e-6]))
plt.semilogy(f, Pxx_den)
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()


sr, test = io.wavfile.read("Single Birdcall Samples/iso1.wav")
f, Pxx_den = signal.welch(test, sr)
plt.semilogy(f, Pxx_den)
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

print(np.max(f[Pxx_den > 0.00001]))
print(np.min(f[Pxx_den > 0.00001]))

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