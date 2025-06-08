import numpy as np
import matplotlib.pyplot as plt

# Solicitar parámetros al usuario
try:
    A = float(input("Ingrese la amplitud (ej. 0.5, 1, 2): "))
    f = float(input("Ingrese la frecuencia en Hz (ej. 1, 2, 5): "))
    phi = float(input("Ingrese la fase en radianes (ej. 0, 0.785 (π/4), 1.57 (π/2)): "))
except ValueError:
    print("Error: Asegúrate de ingresar valores numéricos.")
    exit()

# Parámetros para la señal de referencia
t = np.linspace(0, 1, 1000)              # Tiempo continuo
Ts = 0.01                                # Periodo de muestreo
n = np.arange(0, 1, Ts)                  # Índices discretos
t_discreto = n * Ts

# Señal en tiempo continuo
x_cont = A * np.sin(2 * np.pi * f * t + phi)
x_ref_cont = 1 * np.sin(2 * np.pi * 1 * t + 0)  # Señal de referencia

# Señal en tiempo discreto
x_disc = A * np.sin(2 * np.pi * f * t_discreto + phi)
x_ref_disc = 1 * np.sin(2 * np.pi * 1 * t_discreto + 0)

# Gráfica tiempo continuo
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t, x_cont, label='Señal modificada', color='blue')
plt.plot(t, x_ref_cont, '--', label='Señal de referencia', color='red')
plt.title('Señal en Tiempo Continuo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

# Gráfica tiempo discreto
plt.subplot(1, 2, 2)
plt.stem(t_discreto, x_disc, basefmt=" ", linefmt='b-', markerfmt='bo', label='Señal modificada')
plt.plot(t_discreto, x_ref_disc, 'r--', label='Señal de referencia')
plt.title('Señal en Tiempo Discreto')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

