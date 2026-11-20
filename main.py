from src.file_working import file_working, graf, matrix
from src.obrabotka import extract_frequency, save_audio
from src.obrabotka_2 import save_audio, remove_frequency
from src.cross_section import extract_frequency_range, remove_frequency_range


def main():
    while True:
        print("1. Построить график волны")
        print("2. Построить спектрограмму")
        print("3. Вырезать конкретную частоту и сохранить")
        print("4. Удалить конкретную частоту и сохранить")
        print("5. ОСТАВИТЬ ДИАПАЗОН")
        print("6. УДАЛИТЬ ДИАПАЗОН")
        print("7. Выход")
        choice = input("Выбери действие (1-7): ")

        if choice == '7':
            print("Пока!")
            break

        filename = input("Введи имя файла (например, NJENSI.mp3): ")

        if choice == '1':
            graf(filename)

        elif choice == '2':
            matrix(filename)

        elif choice == '3':
            freq = float(input("Какую частоту вырезать (Гц)? "))
            y, sr = file_working(filename)
            y_filt = extract_frequency(y, sr, freq)
            save_audio(y_filt, sr, f'data/only_{freq}Hz.wav')
        elif choice == '4':
            freq = float(input("Какую частоту удалить (Гц)? "))
            y, sr = file_working(filename)
            y_filt = remove_frequency(y, sr, freq)
            save_audio(y_filt, sr, f'data/un_only_{freq}Hz.wav')
        elif choice == '5':
            print("ОСТАВИТЬ ДИАПАЗОН")
            min_f = float(input("От какой частоты (Гц)? "))
            max_f = float(input("До какой частоты (Гц)? "))
            y, sr = file_working(filename)
            y_filt = extract_frequency_range(y, sr, min_f, max_f)
            save_audio(y_filt, sr, f'data/range_{min_f}-{max_f}Hz.wav')
        elif choice == '6':
            print("УДАЛИТЬ ДИАПАЗОН")
            min_f = float(input("От какой частоты (Гц)? "))
            max_f = float(input("До какой частоты (Гц)? "))
            y, sr = file_working(filename)
            y_filt = remove_frequency_range(y, sr, min_f, max_f)
            save_audio(y_filt, sr, f'data/removed_{min_f}-{max_f}Hz.wav')
        else:
            print("Нет такого пункта!")


if __name__ == "__main__":
    main()