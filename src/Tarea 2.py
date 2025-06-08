import numpy as np
import matplotlib.pyplot as plt

# Parámetros fijos
A = 1  # Amplitud
t = np.linspace(0, 1, 1000)  # Tiempo de 0 a 1 segundo, con 1000 puntos

# Solicitar frecuencia al usuario
f = float(input("Introduce la frecuencia (Hz): "))

# Ecuación de la señal
x = A * np.sin(2 * np.pi * f * t)

# Graficar la señal
plt.figure(figsize=(10, 4))
plt.plot(t, x)
plt.title(f'Señal Senoidal - Frecuencia: {f} Hz')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.tight_layout()
plt.show()
