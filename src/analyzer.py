import os
import librosa
import numpy as np
import matplotlib.pyplot as plt


current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
file_path = os.path.join(project_root, 'data', 'NJENSI.mp3')

y, sr = librosa.load(file_path)

D = librosa.stft(y)
D_amplitude = np.abs(D)
D_db = librosa.amplitude_to_db(D_amplitude, ref=np.max)


plt.figure(figsize=(12, 6))
librosa.display.specshow(D_db, sr=sr, x_axis='time', y_axis='log', cmap='magma')
plt.colorbar(format='%+2.0f dB')
plt.title('Спектрограмма')
plt.show()
#plt.imshow(D_db)
plt.plot(D_db)
