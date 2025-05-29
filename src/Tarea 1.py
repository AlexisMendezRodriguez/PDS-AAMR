import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square, sawtooth

# Parámetros generales
f = 2  # Frecuencia recomendada
T_s = 0.01  # Periodo de muestreo
t_cont = np.linspace(-1, 5, 1000)  # Tiempo continuo
n = np.arange(0, int((5 + 1)/T_s))  # Índices de muestreo
t_disc = n * T_s  # Tiempo discreto

# Señal 1: x₁(t) = sin(2π·f·t)
x1_cont = np.sin(2 * np.pi * f * t_cont)
x1_disc = np.sin(2 * np.pi * f * t_disc)

# Señal 2: x₂(t) = e^(–2t) · u(t)
u_cont = np.heaviside(t_cont, 1)
x2_cont = np.exp(-2 * t_cont) * u_cont
u_disc = np.heaviside(t_disc, 1)
x2_disc = np.exp(-2 * t_disc) * u_disc

# Señal 3: x₃(t) = tri(t, f) (triangular periódica)
x3_cont = sawtooth(2 * np.pi * f * t_cont, width=0.5)
x3_disc = sawtooth(2 * np.pi * f * t_disc, width=0.5)

# Señal 4: x₄(t) = sq(t, f) (cuadrada)
x4_cont = square(2 * np.pi * f * t_cont)
x4_disc = square(2 * np.pi * f * t_disc)

# Función para graficar
def plot_signal(t_cont, x_cont, t_disc, x_disc, title):
    plt.figure(figsize=(10, 4))
    plt.plot(t_cont, x_cont, label='Señal continua', color='blue')
    plt.stem(t_disc, x_disc, linefmt='r-', markerfmt='ro', basefmt='k-', label='Señal discreta')
    plt.title(title)
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Graficar todas las señales
plot_signal(t_cont, x1_cont, t_disc, x1_disc, "Señal x₁(t) = sin(2π·f·t)")
plot_signal(t_cont, x2_cont, t_disc, x2_disc, "Señal x₂(t) = e^(–2t) · u(t)")
plot_signal(t_cont, x3_cont, t_disc, x3_disc, "Señal x₃(t) = tri(t, f)")
plot_signal(t_cont, x4_cont, t_disc, x4_disc, "Señal x₄(t) = sq(t, f)")
