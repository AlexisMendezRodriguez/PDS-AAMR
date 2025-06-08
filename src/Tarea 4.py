import numpy as np
import matplotlib.pyplot as plt

def dac_analysis(bits, vfs=5.0):
    # Cálculos
    levels = 2 ** bits
    step_size = vfs / (levels - 1)
    resolution_percent = (step_size / vfs) * 100

    # Imprimir resultados
    print(f"\nNúmero de bits: {bits}")
    print(f"Número total de niveles: {levels}")
    print(f"Tamaño del paso: {step_size:.6f} V")
    print(f"Resolución porcentual: {resolution_percent:.4f} %")

    # Generar datos para gráfica
    digital_inputs = np.arange(levels)
    analog_outputs = digital_inputs * step_size

    # Gráfica
    plt.figure(figsize=(10, 5))
    plt.plot(digital_inputs, analog_outputs, marker='o', linestyle='-')
    plt.title(f"Salida del DAC de {bits} bits")
    plt.xlabel("Nivel Digital de Entrada")
    plt.ylabel("Voltaje Analógico (V)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    try:
        n_bits = int(input("Ingresa el número de bits del DAC: "))
        if n_bits < 1:
            raise ValueError
        dac_analysis(n_bits)
    except ValueError:
        print("Por favor ingresa un número entero positivo para los bits.")

