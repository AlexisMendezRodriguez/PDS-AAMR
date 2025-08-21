import numpy as np
import matplotlib.pyplot as plt

# Parámetros
fs = 256            #frecuencia de muestreo [Hz]
Ts = 1/fs           #periodo de muestreo
T = 6               #duración [segundos]
N = fs * T          #número total de muestras
t = np.arange(N) * Ts  #vector de tiempo discreto

# Frecuencias de la señal original
f1 = 8   #Hz
f2 = 20  #Hz

# Señal discreta base (limpia)
x_clean = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)

# DFT señal limpia
X_clean = np.fft.fft(x_clean)
freqs = np.fft.fftfreq(N, Ts)

# Añadir ruido: por ejemplo una sinusoide de 50 Hz
f_noise = 50
noise = 0.7*np.sin(2*np.pi*f_noise*t)

x_noisy = x_clean + noise
X_noisy = np.fft.fft(x_noisy)

# Resolución en frecuencia
delta_f = fs / N
print(f"Resolución en frecuencia Δf = {delta_f:.4f} Hz")

#Graficar

# Señal limpia y su espectro
plt.figure(figsize=(12,6))

plt.subplot(2,2,1)
plt.plot(t, x_clean)
plt.title("Señal discreta base (limpia)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")

plt.subplot(2,2,2)
plt.stem(freqs[:N//2], np.abs(X_clean[:N//2])/N)
plt.title("DFT - Señal limpia")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")

# Señal con ruido y su espectro
plt.subplot(2,2,3)
plt.plot(t, x_noisy)
plt.title("Señal con ruido")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")

plt.subplot(2,2,4)
plt.stem(freqs[:N//2], np.abs(X_noisy[:N//2])/N)
plt.title("DFT - Señal con ruido")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")

plt.tight_layout()
plt.show()
