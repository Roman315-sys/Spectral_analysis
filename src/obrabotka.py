import librosa
import numpy as np
import soundfile as sf


def extract_frequency(y, sr, target_freq):
    """Вырезает конкретную частоту из сигнала."""

    D = librosa.stft(y)

    freqs = librosa.fft_frequencies(sr=sr) #массив с частотами
    target_idx = np.argmin(np.abs(freqs - target_freq))

    mask = np.zeros_like(D, dtype=bool) #пустая матрица которую мы будем заполнять

    mask[target_idx, :] = True
    D_filtered = D * mask

    y_filtered = librosa.istft(D_filtered) #обратное преобразование

    return y_filtered


def save_audio(y, sr, output_path):
    """Сохраняет звуковой массив в файл."""
    sf.write(output_path, y, sr)
    print(f"Файл успешно сохранен: {output_path}")