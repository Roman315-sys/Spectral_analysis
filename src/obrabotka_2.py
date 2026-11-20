import librosa
import numpy as np
import soundfile as sf
import os


# current_dir = os.path.dirname(os.path.abspath(__file__))
# project_root = os.path.dirname(current_dir)
# file_path = os.path.join(project_root, 'data', "NJENSI.mp3")


def remove_frequency(y, sr, target_freq):
    """Убирает конкретную частоту из сигнала."""

    D = librosa.stft(y)
    freqs = librosa.fft_frequencies(sr=sr)

    target_idx = np.argmin(np.abs(freqs - target_freq))

    mask = np.ones_like(D, dtype=bool)

    # можно убрать диапазон
    mask[target_idx, :] = False

    D_filtered = D * mask
    y_filtered = librosa.istft(D_filtered)

    return y_filtered


def save_audio(y, sr, output_path):
    """Сохраняет звуковой массив в файл."""
    sf.write(output_path, y, sr)
    print(f"Файл успешно сохранен: {output_path}")



# y, sr = librosa.load(file_path)
#
# freq = 440
# y_filtered = remove_frequency(y, sr, freq)
# save_path = os.path.join(project_root, 'data', 'song_440Hz.wav')
#
# save_audio(y_filtered, sr, save_path)