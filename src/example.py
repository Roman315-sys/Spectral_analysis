import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def calculation(f ,n, x):
    """Вычисление ряда для 2pi переодичных функций"""

    a_0, error = quad(lambda t: f(t), -np.pi, np.pi)
    a_0 = a_0 / np.pi

    y_result = np.full_like(x, a_0 / 2.0)

    for n in range(1, n + 1):
        a_n, error = quad(lambda t: f(t) * np.cos(n * t), -np.pi, np.pi)
        a_n = a_n / np.pi

        b_n, error = quad(lambda t: f(t) * np.sin(n * t), -np.pi, np.pi)
        b_n = b_n / np.pi

        s_n = a_n * np.cos(n * x) + b_n * np.sin(n * x)
        y_result += s_n

    return y_result