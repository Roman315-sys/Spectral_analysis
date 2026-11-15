import librosa
import numpy as np


def extract_frequency_range(y, sr, min_freq, max_freq):
    """Оставляет только частоты в заданном диапазоне."""
    D = librosa.stft(y)
    freqs = librosa.fft_frequencies(sr=sr)

    mask = np.zeros_like(D, dtype=bool)
    mask[(freqs >= min_freq) & (freqs <= max_freq), :] = True

    D_filtered = D * mask

    y_filtered = librosa.istft(D_filtered)
    return y_filtered


def remove_frequency_range(y, sr, min_freq, max_freq):
    """Убирает частоты в заданном диапазоне."""
    D = librosa.stft(y)
    freqs = librosa.fft_frequencies(sr=sr)

    # Создаем маску, где всё True
    mask = np.ones_like(D, dtype=bool)

    mask[(freqs >= min_freq) & (freqs <= max_freq), :] = False

    D_filtered = D * mask
    y_filtered = librosa.istft(D_filtered)
    return y_filtered