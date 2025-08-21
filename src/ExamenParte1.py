import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
fm = 0.5   #frecuencia de modulación (Hz)
fc = 8.0   #frecuencia portadora (Hz)
m = 0.5    #índice de modulación
fs = 100   #frecuencia de muestreo (Hz)
T = 10     #duración (segundos)
N = int(fs * T)  #número de muestras

# Vector de tiempo
t = np.arange(N) / fs

# Señal onda sinusoidal
x = (1 + m * np.cos(2 * np.pi * fm * t)) * np.sin(2 * np.pi * fc * t)

# Calcular la DFT usando FFT
X = np.fft.fft(x)
X_magnitude = np.abs(X) / N
freqs = np.fft.fftfreq(N, d=1/fs)

# Solo parte positiva del espectro
mask = freqs >= 0
freqs_pos = freqs[mask]
X_pos = X_magnitude[mask]

# Resolución en frecuencia
delta_f = fs / N
print(f"Resolución en frecuencia Δf = {delta_f:.3f} Hz")

# Graficar señal en el tiempo
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(t, x)
plt.title("Señal muestreada en el tiempo")
plt.xlabel("Tiempo [s]")
plt.ylabel("x(t)")
plt.xlim(0, 2)

# Graficar espectro
plt.subplot(1,2,2)
plt.stem(freqs_pos, X_pos, basefmt=" ")
plt.title("Espectro de magnitud (DFT)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("|X(f)|")
plt.xlim(0, 20)
plt.grid()
plt.tight_layout()

plt.show()

