# Fundamentos de Filtrado y Transformada Wavelet en Señales de ECG Reales

## I. Adquisición y Naturaleza de la Señal ECG

El análisis de señales requiere comprender el origen y las características de los datos. El Electrocardiograma (ECG) refleja la actividad eléctrica del corazón, caracterizada por una morfología específica (ondas P, complejo QRS y onda T)

**Características del Registro:**
Un punto crucial en el procesamiento es que la mayor parte de la energía útil del ECG se concentra en bajas frecuencias (menores a 40 Hz).
En una adquisición real (como la obtenida mediante una placa BITalino y software OpenSignals en Derivación II tras 5 minutos de ejercicio):
*   Se utiliza un canal específico (ej. Canal A2).
*   La **frecuencia de muestreo** es típicamente alta (ej. 1000 Hz) para no perder detalles finos.
*   La señal cruda (en bits) debe convertirse a unidades físicas reales (mV) y centrarse en cero eliminando su media para facilitar el análisis matemático.

> **[Espacio para Imagen 1]**
> *Sugerencia:* Insertar aquí la gráfica del **"ECG real (canal A2)"**. Esta imagen muestra la forma de onda limpia y centrada en cero, permitiendo visualizar la morfología base antes de cualquier procesamiento.

## II. El Problema del Ruido y la Contaminación

En entornos reales, la señal de interés rara vez está limpia. Se ve afectada por dos componentes no deseados principales:
1.  **Ruido:** Es aleatorio y afecta a todo el espectro, como el ruido gaussiano (que eleva el piso espectral en frecuencia) o el ruido muscular electromiográfico.
2.  **Interferencia:** Es una señal no deseada pero con una estructura y frecuencia muy identificables, siendo la más común la interferencia de la red eléctrica.

Para evaluar objetivamente los algoritmos de filtrado en un entorno controlado, es una práctica común realizar una **Contaminación Artificial**. Esto implica tomar un ECG original limpio y sumarle matemáticamente:
*   Interferencia primaria (ej. 60 Hz).
*   Armónicos de la interferencia (ej. 120 Hz).
*   Ruido gaussiano de alta frecuencia.

El espectro de frecuencias (FFT) de esta señal contaminada revelará picos nítidos en las frecuencias de interferencia, ilustrando por qué la FFT nos dice *qué* frecuencias están presentes, mientras que las técnicas avanzadas nos dirán *cuándo* aparecen.

> **[Espacio para Imagen 2]**
> *Sugerencia:* Insertar aquí la gráfica del **"ECG contaminado (+ 60 Hz + 120 Hz + ruido gaussiano)"**. Esta visualización demostrará cómo las interferencias y el ruido enmascaran casi por completo los complejos QRS.

## III. Métodos de Filtrado Convencional y Adaptativo

Para recuperar la señal, existen diferentes aproximaciones matemáticas, cada una con un propósito específico:

### 1. Filtrado Pasa-Banda (Butterworth)
Es la primera línea de defensa. Se configura para permitir el paso solo de las frecuencias donde reside la energía útil del ECG.
*   **Parámetros Típicos:** Frecuencia de corte de 0.5 Hz a 40 Hz, con un orden matemático (ej. orden 4) que define cuán abrupto es el corte.
*   **Función:** Atenúa simultáneamente las variaciones muy lentas (deriva de línea base, $< 0.5$ Hz) y el ruido de alta frecuencia ($> 40$ Hz).

### 2. Filtrado Notch
Es un filtro de rechazo de banda extremadamente estrecho.
*   **Aplicación:** Se diseña específicamente para "morder" y eliminar frecuencias puntuales de interferencia (ej. 60 Hz y su armónico de 120 Hz).
*   **Factor de Calidad (Q):** Un Q alto (ej. Q = 30) asegura que el filtro sea muy selectivo, eliminando la interferencia con la mínima distorsión posible en las frecuencias adyacentes de la señal ECG.

### 3. Filtros Adaptativos (Algoritmo LMS)
A diferencia de los filtros anteriores, cuyos coeficientes son fijos, el filtro adaptativo LMS ajusta sus propios pesos ($w$) muestra a muestra para cancelar el ruido.
*   **Mecanismo:** Utiliza señales de referencia (como ondas seno/coseno sintéticas a 60 y 120 Hz) y evalúa el error en cada paso ($e[n]$) para actualizar la ecuación: $w[n+1] = w[n] + 2\mu e[n]x[n]$.
*   **Parámetro $\mu$:** El tamaño del paso (ej. $\mu = 0.005$) controla la velocidad de aprendizaje y la estabilidad. Es especialmente útil cuando las interferencias cambian en el tiempo.

> **[Espacio para Imagen 3]**
> *Sugerencia:* Insertar la gráfica de **"Descopación de los coeficientes"** del filtro LMS adaptativo. Esto ilustrará la teoría de cómo los coeficientes del filtro parten de cero y "aprenden" hasta estabilizarse para cancelar las frecuencias de 60 Hz y 120 Hz.

## IV. La Transformada Wavelet Discreta (DWT)

Mientras los filtros convencionales actúan sobre la frecuencia global, la Transformada Wavelet localiza en el tiempo los componentes rápidos del ECG (como el QRS), separándolos del ruido y las interferencias.

El proceso de DWT descompone la señal en múltiples niveles de detalle (D) y una aproximación final (A).
Por ejemplo, si utilizamos una familia **Wavelet db4** (cuyas ondas se asemejan al complejo QRS) con **8 niveles de descomposición**, obtenemos bandas de frecuencia específicas:
*   **D1 a D3:** Contienen frecuencias muy altas (250-500 Hz, 125-250 Hz, 62.5-125 Hz). Aquí reside predominantemente el **ruido gaussiano** y la **interferencia de 120 Hz** (en D3).
*   **D4:** Contiene la banda de 31.2 a 62.5 Hz, atrapando principalmente la **interferencia de 60 Hz**.
*   **D5 (15.6 - 31.2 Hz) y D6:** Contienen la mayor parte de la energía de los eventos rápidos fisiológicos, especialmente el **complejo QRS**.
*   **A8 (Aproximación de nivel 8):** Retiene las frecuencias ultrabajas ($0 - 2.0$ Hz), representando la **deriva de la línea base**.

Para realizar el *denoising* (reducción de ruido), se aplica un **umbral universal** (método 'soft' o suave) sobre los coeficientes de detalle. Esto reduce el ruido gaussiano preservando la morfología de eventos rápidos útiles como el QRS. Sin embargo, la Wavelet por sí sola no es óptima para eliminar interferencias sinusoidales intensas y estrechas (como las de 60Hz), ya que su fuerte es el análisis transitorio.

> **[Espacio para Imagen 4]**
> *Sugerencia:* Insertar la gráfica de la **"Descomposición Wavelet (ejemplos de niveles)"**. Esto permitirá visualizar claramente cómo la señal se separa en diferentes sub-bandas (A8, D5, D4, D3), demostrando empíricamente en qué nivel se aloja la deriva de línea base, el QRS y el ruido.

## V. Evaluación y Conclusiones del Filtrado

Para determinar qué método es superior, se debe evaluar no solo visualmente, sino métricamente. Se utiliza la relación Señal-a-Ruido (**SNR**) y el coeficiente de correlación ($r$) con la señal original.

En un escenario práctico comparativo:
*   El filtro **Pasa-Banda** suele ser robusto y puede obtener el SNR más alto (ej. 12.30 dB) al barrer con interferencias fuera de su banda.
*   Sin embargo, un **enfoque híbrido (ej. Notch + Wavelet)** ofrece el mejor equilibrio: mantiene una altísima correlación con la señal original (ej. $r=0.9756$), logrando una excelente limpieza mientras preserva estrictamente la morfología fisiológica, lo cual es vital para el diagnóstico clínico.

> **[Espacio para Imagen 5]**
> *Sugerencia:* Insertar las gráficas comparativas finales del panel 6: **"Señales en el dominio del tiempo (segmento)"** mostrando la señal filtrada, junto al gráfico de barras de **"SNR por método (dB)"**. Esto brindará un resumen visual contundente del rendimiento de cada técnica discutida en la teoría.
