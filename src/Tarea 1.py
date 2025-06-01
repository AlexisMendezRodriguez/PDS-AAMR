import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square, sawtooth

# Parámetros comunes
f = 2  # Frecuencia en Hz
t_cont = np.linspace(-1, 5, 1000)  # Tiempo continuo
T_s = 0.01  # Periodo de muestreo
t_disc = np.arange(-1, 5, T_s)  # Tiempo discreto

#Las 4 diferentes señales

# 1. Señal sinusoidal
x1_cont = np.sin(2 * np.pi * f * t_cont)
x1_disc = np.sin(2 * np.pi * f * t_disc)

# 2. Señal exponencial con escalón
u_cont = np.heaviside(t_cont, 1)
u_disc = np.heaviside(t_disc, 1)
x2_cont = np.exp(-2 * t_cont) * u_cont
x2_disc = np.exp(-2 * t_disc) * u_disc

# 3. Señal triangular
x3_cont = sawtooth(2 * np.pi * f * t_cont, width=0.5)
x3_disc = sawtooth(2 * np.pi * f * t_disc, width=0.5)

# 4. Señal cuadrada
x4_cont = square(2 * np.pi * f * t_cont)
x4_disc = square(2 * np.pi * f * t_disc)

# Función para graficar las tres versiones de cada señal

def plot_signal_versions(t_cont, x_cont, t_disc, x_disc, title_base):
    # Gráfica continua
    plt.figure(figsize=(10, 3))
    plt.plot(t_cont, x_cont, 'b', label='Señal continua')
    plt.title(f'{title_base} - Continua')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Gráfica discreta
    plt.figure(figsize=(10, 3))
    plt.stem(t_disc, x_disc, linefmt='g-', markerfmt='go', basefmt=" ", label='Señal discreta')
    plt.title(f'{title_base} - Discreta')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Gráfica combinada
    plt.figure(figsize=(10, 3))
    plt.plot(t_cont, x_cont, 'b', label='Señal continua')
    plt.stem(t_disc, x_disc, linefmt='r-', markerfmt='ro', basefmt=" ", label='Señal discreta')
    plt.title(f'{title_base} - Continua y Discreta')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Llamar a la función para cada señal
plot_signal_versions(t_cont, x1_cont, t_disc, x1_disc, 'Sinusoidal: x₁(t) = sin(2π·f·t)')
plot_signal_versions(t_cont, x2_cont, t_disc, x2_disc, 'Exponencial: x₂(t) = e^(–2t) · u(t)')
plot_signal_versions(t_cont, x3_cont, t_disc, x3_disc, 'Triangular: x₃(t) = tri(t, f)')
plot_signal_versions(t_cont, x4_cont, t_disc, x4_disc, 'Cuadrada: x₄(t) = sq(t, f)')
