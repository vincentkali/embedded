import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display


#y, sr = librosa.load('ex.wav')
y, sr = librosa.load('Filename.mp3')
mfccs = librosa.feature.mfcc(y=y, sr=sr)

print (mfccs)

plt.figure(figsize=(10, 4))
librosa.display.specshow(mfccs, sr=sr, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()
plt.show()
