### **Q1. What are the most typical types of noise sources affecting ECG?**
Las fuentes de ruido más comunes que afectan la señal de ECG son:
* **Artefactos por movimiento (Movement Artifacts):** Desplazamientos de los electrodos sobre la piel o movimientos del sujeto.
* **Interferencia de la red eléctrica (Powerline Noise):** Ruido de 50 Hz o 60 Hz inducido por la red eléctrica de los dispositivos cercanos.
* **Electromiografía / Ruido Muscular (EMG Noise):** Actividad eléctrica producida por la contracción involuntaria o voluntaria de los músculos subyacentes.
* **Ruido de contacto del electrodo:** Variaciones en la impedancia entre la piel y el electrodo por mala adhesión o gel seco.
* **Deriva de la línea base (Baseline Wander):** Variaciones de baja frecuencia causadas por la respiración o la transpiración.

---

### **Q2. Why does the change of the positioning of the sensors (lead I-III) change the ECG signal components? How do the components change?**
* **Causa del cambio:** Las derivaciones de Einthoven (I, II y III) miden la diferencia de potencial eléctrico del corazón desde diferentes ángulos espaciales en el plano frontal.
* **Cambios en los componentes:** El vector eléctrico principal de despolarización ventricular se orienta generalmente hacia abajo y hacia la izquierda. Por ello, las amplitudes de las ondas (especialmente la onda R del complejo QRS) cambian según la alineación del vector cardíaco con el eje de la derivación. Por ejemplo, en la derivación II la onda R suele tener mayor amplitud debido a que la dirección del vector se alinea estrechamente con el eje de dicha derivación.

---

### **Q3. Describe if there are major differences in the signal when acquiring the signal from different body locations (e.g., wrist / collarbone / chest). What could be the cause? Did you expect such changes in the signal? Store a signal segment of each to visualize the differences.**
* **Diferencias en la señal:** La amplitud de la señal de ECG es significativamente más alta y clara cuando los electrodos se colocan directamente en el tórax/pecho en comparación con las muñecas.
* **Causa:** Colocar los electrodos más cerca del corazón incrementa la amplitud de la señal recibida y reduce la interferencia muscular (EMG) de las extremidades. A medida que los electrodos se alejan, la señal viaja más distancia a través del tejido corporal, reduciendo la relación señal-ruido.
* *(Nota: El almacenamiento de segmentos de señal visuales debe ser realizado directamente por el usuario al ejecutar la práctica).*

---

### **Q4. The cardiac and the respiratory systems are well interconnected as is well known. Do you expect that different types of breathing (e.g. faster, deeper) to influence the ECG signals? Show screenshots of ECG signals in different respiratory circumstances and described the variations if there are any.**
* **Efecto de la respiración:** Sí. La respiración altera la señal de ECG principalmente de dos formas:
  1. **Arritmia Sinusal Respiratoria (RSA):** La frecuencia cardíaca aumenta de forma natural durante la inhalación y disminuye durante la exhalación.
  2. **Modulación de la amplitud por movimiento del tórax:** La inhalación profunda altera la posición anatómica relativa del corazón con respecto a los electrodos y modifica la distancia entre la superficie cutánea y el corazón, haciendo fluctuar la amplitud de los picos R[cite: 1].
* *(Nota: Las capturas de pantalla deben ser tomadas por el usuario durante el desarrollo de la prueba experimental).*

---

### **Q5. In Home-Guide #1 you have seen that different amounts of force produced in the muscle generated signals with different amplitudes. How does movement influence your ECG signal?**
* El movimiento genera contracciones de los músculos esqueléticos cercanos, produciendo señales electromiográficas (EMG) no deseadas que se superponen a la señal de ECG. Esto causa picos de alta frecuencia (ruido EMG) o variaciones bruscas en la línea base de la señal. Por esta razón, se recomienda colocar los electrodos sobre zonas con menor densidad o actividad muscular (como superficies óseas) durante las mediciones.

---

### **Q6. To the best of your knowledge, how can you detect bradycardia and tachycardia in the ECG signal?**
* Se detectan midiendo el intervalo entre picos R consecutivos (intervalo R-R) para calcular la frecuencia cardíaca en latidos por minuto (bpm):
  * **Taquicardia:** Se detecta cuando la frecuencia cardíaca supera los 100 bpm en reposo, lo que se traduce visualmente en un intervalo R-R más corto.
  * **Bradicardia:** Se detecta cuando la frecuencia cardíaca cae por debajo de los 60 bpm en reposo, manifestándose con un intervalo R-R significativamente más largo.