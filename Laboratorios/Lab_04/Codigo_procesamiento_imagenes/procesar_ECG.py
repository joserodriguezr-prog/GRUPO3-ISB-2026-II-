#Librerias utilizadas
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, iirnotch

# 1. CONFIGURACIÓN
archivo="Lectura_basal_D3.txt"  #Nombre del archivo de OpenSignals que contiene el registro de ECG
Fs=1000  #Frecuencia de muestreo de tu registro
# 2. LEER EL ARCHIVO DE OPENSIGNALS
datos=np.loadtxt(
    archivo,
    comments="#"
)
# 3. EXTRAER EL CANAL ECG

# Columnas del archivo:
# 0 = nSeq
# 1 = I1
# 2 = I2
# 3 = O1
# 4 = O2
# 5 = A2
ecg=datos[:, 5]
# 4. CREAR EJE DE TIEMPO
tiempo=np.arange(len(ecg)) / Fs
# 5. FILTRO PASA BANDA
# 0.5 - 40 Hz
frecuencia_baja = 0.5    #Filltrar señales de baja frecuencia
frecuencia_alta = 40     #Filtrar señales de alta frecuencia
b, a = butter(
    4,
    [frecuencia_baja, frecuencia_alta],
    btype="bandpass",
    fs=Fs
)

ecg_filtrado=filtfilt(
    b,
    a,
    ecg
)

# 6. FILTRO NOTCH
#    ELIMINA INTERFERENCIA DE 60 Hz
frecuencia_red=60
factor_calidad=30

b_notch, a_notch = iirnotch(
    frecuencia_red,
    factor_calidad,
    Fs
)

ecg_filtrado = filtfilt(
    b_notch,
    a_notch,
    ecg_filtrado
)

# 7. INFORMACIÓN DEL REGISTRO
print("--------------------------------------")
print("       PROCESAMIENTO DE ECG")
print("--------------------------------------")

print("Archivo:", archivo)
print("Frecuencia de muestreo:", Fs, "Hz")
print("Número de muestras:", len(ecg))
print("Duración:", tiempo[-1], "segundos")

print("\nECG ORIGINAL")
print("Valor mínimo:", np.min(ecg))
print("Valor máximo:", np.max(ecg))
print("Valor promedio:", np.mean(ecg))

print("\nFILTRO PASA BANDA")
print("Frecuencia inferior:", frecuencia_baja, "Hz")
print("Frecuencia superior:", frecuencia_alta, "Hz")

print("\nFILTRO NOTCH")
print("Frecuencia eliminada:", frecuencia_red, "Hz")

# 8. SELECCIONAR INTERVALO PARA VISUALIZACIÓN
inicio=14
fin=20
indices = (
    (tiempo >= inicio) &
    (tiempo <= fin)
)

# 9. GRAFICAR ECG ORIGINAL Y ECG FILTRADO
#    SOLO ENTRE 10 Y 15 SEGUNDOS
plt.figure(figsize=(12, 8))
# ECG ORIGINAL
plt.subplot(2, 1, 1)
plt.plot(
    tiempo[indices],
    ecg[indices]
)

plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("ECG original (14–20 s)")

plt.grid(True)

# ECG FILTRADO
plt.subplot(2, 1, 2)

plt.plot(
    tiempo[indices],
    ecg_filtrado[indices]
)

plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("ECG filtrado (14–20 s)")
plt.grid(True)
plt.tight_layout()
plt.show()