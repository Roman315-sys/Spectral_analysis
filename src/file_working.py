import os
import librosa
import matplotlib.pyplot as plt
import numpy as np


def file_working(filename):
    """Открываем файл для получения массива"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    file_path = os.path.join(project_root, 'data', filename)

    y, sr = librosa.load(file_path)
    return y, sr


def graf(filename):
    """Строит график по аудиофайлу"""
    y, sr = file_working(filename)

    plt.figure(figsize=(10, 3))
    plt.plot(y, color='blue', linewidth=3)
    plt.show()

    return y, sr


def matrix(filename):
    """Строит матрицу"""
    y, sr = file_working(filename)
    D = librosa.stft(y)

    # 3. Берем амплитуды и переводим в децибелы
    D_amplitude = np.abs(D)
    D_db = librosa.amplitude_to_db(D_amplitude, ref=np.max)

    plt.figure(figsize=(12, 6))
    librosa.display.specshow(D_db, sr=sr, x_axis='time', y_axis='log', cmap='magma')
    plt.colorbar(format='%+2.0f dB')
    plt.title(f'Спектрограмма: {filename}')

    plt.show()

    return plt.show()