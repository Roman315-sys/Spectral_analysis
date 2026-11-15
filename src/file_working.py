import os
import librosa
import matplotlib.pyplot as plt


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



graf('NJENSI.mp3')
# print(graf('NJENSI.mp3'))