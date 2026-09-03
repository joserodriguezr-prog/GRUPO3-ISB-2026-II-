![Informe de Laboratorio 3](./Laboratorios./Lab_02./Lab003./infografia_ecg_solo_inicio.jpeg)
# Informe resumen — Laboratorio 3

## Filtros FIR, IIR y Transformada Z aplicados a señales ECG

### 1. Introducción

En este laboratorio se trabajó con una señal ECG sintética con el objetivo de aprender a inspeccionar, caracterizar, analizar, filtrar y validar una señal biomédica. El análisis se realizó tanto en el dominio temporal como en el dominio frecuencial, utilizando herramientas de Python.

El flujo general del laboratorio fue:

**Señal → análisis temporal → análisis frecuencial → identificación del ruido → selección del filtro → diseño → aplicación → validación.**

### 2. Señal ECG

Se generó una señal ECG sintética utilizando NeuroKit2. La señal tuvo una duración de **10 segundos**, una frecuencia de muestreo de **250 Hz** y una frecuencia cardíaca de **70 bpm**.

En la señal se pueden reconocer las principales características de la morfología ECG: **onda P, complejo QRS y onda T**.

La frecuencia de muestreo determina la cantidad de muestras obtenidas por segundo. La relación utilizada fue:

`N = fs · T`

Por lo tanto:

- `fs = 250 Hz`
- `T = 10 s`
- `N = 2500 muestras`

La frecuencia máxima observable está relacionada con la frecuencia de Nyquist:

`f_max = fs / 2`

En este caso:

`f_max = 250 / 2 = 125 Hz`

### 3. Análisis frecuencial mediante FFT

La Transformada Rápida de Fourier (FFT) permitió analizar la señal en el dominio frecuencial e identificar las componentes presentes.

La señal ECG presentó principalmente componentes de baja frecuencia. La frecuencia fundamental relacionada con la frecuencia cardíaca fue aproximadamente:

`70 / 60 ≈ 1.17 Hz`

También se observaron armónicos debido a la forma de la señal ECG.

La FFT fue importante para determinar qué frecuencias pertenecían al contenido fisiológico y cuáles podían corresponder a ruido o interferencias.

### 4. Filtros FIR e IIR

Se estudiaron dos tipos principales de filtros digitales: **FIR (Finite Impulse Response)** e **IIR (Infinite Impulse Response)**.

Los filtros FIR no utilizan realimentación y permiten obtener fácilmente una respuesta de fase lineal. Por otro lado, los filtros IIR utilizan realimentación, pueden conseguir respuestas más pronunciadas con órdenes menores, pero requieren analizar su estabilidad.

| Característica | FIR | IIR |
|---|---|---|
| Realimentación | No | Sí |
| Estabilidad | Sencilla de garantizar | Debe analizarse |
| Fase lineal | Fácil de obtener | Más compleja |
| Orden requerido | Generalmente mayor | Generalmente menor |

### 5. Diseño del filtro FIR

Se diseñó un filtro **FIR pasa-bajos** utilizando `scipy.signal.firwin`.

La finalidad del filtro fue conservar las componentes principales del ECG y atenuar las componentes de mayor frecuencia.

El filtro se aplicó mediante `filtfilt`, realizando el filtrado en ambas direcciones para evitar un desplazamiento de fase apreciable.

### 6. Diseño del filtro IIR

Se diseñó un filtro **IIR Butterworth pasa-bajos de orden 4**, con una frecuencia de corte de **40 Hz**.

Se utilizó la representación **SOS (Second-Order Sections)** para mejorar la estabilidad numérica del filtro. Posteriormente se utilizó `sosfiltfilt`, que permite realizar un filtrado de fase cero.

### 7. Comparación de los filtros

La comparación se realizó observando la señal original y las señales filtradas, además de analizar las respuestas en frecuencia.

Los filtros FIR e IIR presentan diferentes ventajas. El FIR facilita el control de la fase, mientras que el IIR puede conseguir una respuesta similar con un orden menor.

Para evaluar cuantitativamente las señales se utilizó el error cuadrático medio (MSE).

### 8. Construcción de una señal ECG contaminada

Para comprobar el funcionamiento del filtrado se agregó una interferencia sinusoidal de alta frecuencia a la señal ECG.

Se utilizaron:

- **Amplitud de la interferencia:** `0.20`
- **Frecuencia de la interferencia:** `35 Hz`

La señal contaminada se construyó como:

`ECG_contaminado = ECG_limpio + ruido`

Al analizar la FFT se identificó un pico alrededor de **35 Hz**, correspondiente a la interferencia introducida.

### 9. Recuperación de la señal

Para eliminar la interferencia se diseñó un filtro **IIR Butterworth pasa-bajos de orden 4** con una frecuencia de corte de **25 Hz**.

La frecuencia de corte se seleccionó por debajo de los **35 Hz** de la interferencia, buscando atenuarla sin eliminar las principales características fisiológicas del ECG.

La señal recuperada se obtuvo utilizando:

`signal.sosfiltfilt()`

El uso de `sosfiltfilt` permitió reducir la interferencia evitando un desplazamiento temporal importante de las ondas.

### 10. Validación cuantitativa

La señal recuperada se comparó con la señal ECG limpia utilizando MSE y RMSE.

El MSE se calculó mediante:

`MSE = (1/N) Σ(x[n] - x̂[n])²`

El RMSE corresponde a:

`RMSE = √MSE`

Los resultados obtenidos fueron:

- **MSE:** `9.3098 × 10⁻⁵`
- **RMSE:** `0.00965`

Estos valores indican que la señal recuperada presenta un error relativamente pequeño respecto a la señal limpia de referencia.

También se evaluó la relación señal-ruido:

- **SNR antes del filtrado:** `5.14 dB`
- **SNR después del filtrado:** `28.46 dB`

El aumento del SNR indica una mejora importante después del filtrado.

### 11. Transformada Z

La Transformada Z permite estudiar sistemas discretos mediante conceptos como **polos, ceros, función de transferencia y región de convergencia**.

Para un sistema discreto:

`H(z) = Y(z) / X(z) = B(z) / A(z)`

La Transformada Z es especialmente útil para analizar filtros IIR debido a la presencia de realimentación y polos.

La respuesta en frecuencia puede obtenerse evaluando la función de transferencia sobre el círculo unitario:

`z = e^(jω)`

De esta manera, la Transformada Z proporciona un marco general para estudiar sistemas discretos, mientras que la Transformada de Fourier permite analizar específicamente su comportamiento frecuencial.

### 12. Conclusiones

El laboratorio permitió comprender el proceso completo de análisis y filtrado de una señal biomédica. Primero se analizó la señal ECG en el dominio temporal y posteriormente mediante FFT para conocer su contenido frecuencial.

La identificación de una interferencia de **35 Hz** permitió seleccionar una frecuencia de corte adecuada para recuperar la señal. El filtro IIR Butterworth de orden 4 con corte en **25 Hz** logró reducir considerablemente la interferencia.

Los resultados cuantitativos mostraron una mejora del SNR de **5.14 dB a 28.46 dB**, junto con un MSE de `9.3098 × 10⁻⁵` y un RMSE de `0.00965`.

Finalmente, se comprobó que el filtrado debe evaluarse no solo por la apariencia de la señal, sino también mediante el análisis frecuencial, las métricas de error y la conservación de la información fisiológica relevante.

### 13. Herramientas utilizadas

- Python 3.x
- NumPy
- SciPy
- Matplotlib
- Pandas
- NeuroKit2
- Jupyter Notebook / Google Colab

### 14. Flujo de trabajo

**ECG → FFT → identificación de frecuencias → identificación del ruido → diseño FIR/IIR → filtrado → FFT de validación → MSE/RMSE/SNR → interpretación fisiológica**