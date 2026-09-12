# 1. Introducción

En el presente laboratorio se realizó la adquisición y análisis de señales de electrocardiograma (ECG) utilizando el sistema de adquisición BITalino. El objetivo principal fue registrar la actividad eléctrica cardíaca mediante las tres derivaciones bipolares de las extremidades: DI, DII y DIII.

Para realizar la adquisición se colocaron electrodos sobre las extremidades del participante siguiendo la configuración del triángulo de Einthoven. Esta disposición permite obtener las diferencias de potencial correspondientes a las tres derivaciones bipolares del ECG.

El procedimiento experimental se desarrolló bajo diferentes condiciones fisiológicas. Primero se realizó una lectura basal en reposo, seguida de una prueba de hiperventilación, una prueba de hipoventilación y, finalmente, una actividad aeróbica.

Las señales obtenidas durante el laboratorio fueron visualizadas mediante OpenSignals y posteriormente procesadas utilizando Python, con el propósito de observar las características de la señal ECG y comparar los cambios producidos bajo las diferentes condiciones experimentales.


# 2. Objetivos

## 2.1. Objetivo general

Adquirir y analizar señales de electrocardiograma mediante el sistema BITalino utilizando las derivaciones DI, DII y DIII bajo diferentes condiciones fisiológicas.

## 2.2. Objetivos específicos

- Realizar correctamente la colocación de los electrodos para la adquisición de la señal ECG.

- Utilizar la configuración del triángulo de Einthoven para obtener las derivaciones DI, DII y DIII.

- Adquirir una señal ECG en condiciones de reposo.

- Observar los cambios de la señal ECG durante la hiperventilación.

- Observar los cambios de la señal ECG durante la hipoventilación.

- Evaluar la respuesta cardíaca después de realizar actividad aeróbica.

- Visualizar las señales adquiridas mediante OpenSignals.

- Procesar y graficar las señales mediante Python.

- Comparar las características de la señal ECG bajo las diferentes condiciones experimentales.


# 3. Materiales y equipos

Para la realización del laboratorio se utilizaron los siguientes materiales y equipos:

- Sistema de adquisición BITalino.

- Electrodos de superficie.

- Cables de conexión entre los electrodos y BITalino.

- Computadora.

- Software OpenSignals.

- Python.

- Participante para la adquisición de la señal ECG.


# 4. Colocación de los electrodos

Para realizar la adquisición de la señal ECG se utilizó la configuración correspondiente al **triángulo de Einthoven**.

Para esta práctica se utilizó una disposición equivalente al triángulo de Einthoven, colocando los electrodos cerca del corazón:

- **RA (Right Arm):** región de la clavícula derecha.

- **LA (Left Arm):** región de la clavícula izquierda.

- **LL/LF (Left Leg/Left Foot):** cresta ilíaca izquierda.

La denominación clásica de Einthoven utiliza RA, LA y LL. Sin embargo, la guía de BITalino también permite ubicar los electrodos sobre ambas clavículas y la cresta ilíaca izquierda. Esta disposición mantiene la orientación necesaria para obtener las derivaciones DI, DII y DIII.

## 4.1. Triángulo de Einthoven

La configuración utilizada puede representarse de la siguiente manera:

                    LA (+)

                      ●

                     / \\

                    /   \\

                   /     \\

                DI/       \DIII

                 /         \\

                /           \\

               /             \\

        RA (-) ●-------------● LL/LF (+)

                    DII

Las tres derivaciones se obtienen mediante las siguientes diferencias de potencial:

| Derivación | Electrodo negativo | Electrodo positivo |

|------------|--------------------|---------------------|

| **DI** | RA (-) | LA (+) |

| **DII** | RA (-) | LL/LF (+) |

| **DIII** | LA (-) | LL/LF (+) |

Por lo tanto:

- **DI = LA − RA**

- **DII = LL/LF − RA**

- **DIII = LL/LF − LA**

La correcta colocación de los electrodos es importante para obtener una señal ECG adecuada y reducir posibles errores durante la adquisición.

## 4.2. Evidencia de la colocación de los electrodos

**INSERTAR AQUÍ LA FOTO DE LOS ELECTRODOS COLOCADOS EN EL CUERPO.**

![Colocación de los electrodos](imagenes/colocacion_electrodos.jpg)

Figura 1. Colocación de los electrodos siguiendo la configuración del triángulo de Einthoven.

## 4.3. Conexión de los electrodos con BITalino

Los electrodos fueron conectados al sistema BITalino mediante los cables correspondientes. Se verificó que las conexiones fueran correctas y que existiera un contacto adecuado entre los electrodos y la piel.

**INSERTAR AQUÍ LA FOTO DE LAS CONEXIONES ENTRE BITALINO Y LOS ELECTRODOS.**

![Conexión de los electrodos con BITalino](imagenes/conexion_bitalino.jpg)

Figura 2. Conexión de los electrodos con el sistema BITalino.


# 5. Procedimiento experimental

El procedimiento experimental se realizó siguiendo una secuencia de cuatro etapas:

**Lectura basal → Hiperventilación → Hipoventilación → Actividad aeróbica**

En cada etapa se realizaron registros de las tres derivaciones del ECG:

**DI, DII y DIII.**

El objetivo fue observar cómo cambia la actividad eléctrica cardíaca ante diferentes condiciones fisiológicas.

## 5.1. Lectura basal

La primera etapa correspondió a la **lectura basal**, realizada con el participante en condiciones de reposo.

Esta medición permitió obtener una señal ECG de referencia antes de modificar el patrón respiratorio o realizar actividad física.

### Procedimiento

1. Se colocaron los electrodos en la clavícula derecha, clavícula izquierda y cresta ilíaca izquierda, siguiendo la disposición utilizada para las derivaciones de Einthoven.

2. Se conectaron los electrodos al sistema BITalino.

3. Se verificó la correcta conexión de los electrodos.

4. Se inició la adquisición mediante OpenSignals.

5. El participante permaneció en reposo durante el registro.

6. Se registraron las derivaciones DI, DII y DIII.

7. La lectura basal tuvo una duración aproximada de **30 segundos**.

La señal obtenida durante esta etapa se utilizó como referencia para comparar las modificaciones observadas durante las siguientes condiciones.

### Evidencia

**INSERTAR AQUÍ LA FOTO O EVIDENCIA DEL REGISTRO BASAL.**

### Señales de las tres derivaciones en OpenSignals

#### Derivación I — DI

![Basal DI en OpenSignals](imagenes_opensignal/Basal%20D1%2014-20%20segundos%20%281%29.png)

#### Derivación II — DII

![Basal DII en OpenSignals](imagenes_opensignal/Basal%20D2%2014-20%20segundos%20%281%29.png)

#### Derivación III — DIII

![Basal DIII en OpenSignals](imagenes_opensignal/Basal%20D3%2014-20%20segundos%20%281%29.png)


### Descripción

La lectura basal corresponde al estado de referencia del participante en reposo. En esta condición se observa la señal ECG antes de introducir cambios en la respiración o realizar actividad física.


## 5.2. Hiperventilación

La segunda etapa correspondió a la prueba de **hiperventilación**, en la cual se modificó voluntariamente el patrón respiratorio del participante.

El procedimiento indicado consistió en realizar repetidamente el siguiente ciclo:

**Inhalar → mantener → exhalar**

La prueba tuvo una duración aproximada de **30 segundos**.

### Procedimiento

1. Se mantuvieron los electrodos en la configuración utilizada durante la lectura basal.

2. El participante inició el patrón respiratorio indicado.

3. Se realizó la hiperventilación durante aproximadamente 30 segundos.

4. Se registró la señal ECG.

5. Se adquirieron las derivaciones DI, DII y DIII.

6. Entre cada registro se dejó un período de reposo de aproximadamente **1 minuto**.

### Objetivo

El objetivo de esta etapa fue observar las variaciones de la actividad cardíaca asociadas a la modificación del patrón respiratorio y compararlas con la condición basal.

### Evidencia

**INSERTAR AQUÍ LA FOTO DEL PARTICIPANTE O DE LA ADQUISICIÓN DURANTE LA HIPERVENTILACIÓN.**

### Señales de las tres derivaciones en OpenSignals

#### Derivación I — DI

![Hiperventilación DI en OpenSignals](imagenes_opensignal/Hiper%20D1%2010-15%20segundos%20%281%29.png)

#### Derivación II — DII

![Hiperventilación DII en OpenSignals](imagenes_opensignal/Hiper%20D2%2010-15%20segundos%20%281%29.png)

#### Derivación III — DIII

![Hiperventilación DIII en OpenSignals](imagenes_opensignal/Hiper%20D3%2010-15%20segundos%20%281%29.png)


### Descripción

Durante la hiperventilación se modificó voluntariamente el patrón respiratorio. El registro permite comparar el comportamiento de la señal ECG con respecto al estado basal y evaluar posibles cambios en la frecuencia cardíaca y en los intervalos entre latidos.


## 5.3. Hipoventilación

La tercera etapa consistió en realizar una prueba de **hipoventilación**, mediante una retención voluntaria de la respiración.

Durante esta etapa, el participante mantuvo la respiración durante el mayor tiempo posible, siguiendo las indicaciones dadas durante el laboratorio.

### Procedimiento

1. Se mantuvieron los electrodos en la configuración del triángulo de Einthoven.

2. El participante inició la retención voluntaria de la respiración.

3. Se mantuvo la respiración durante el mayor tiempo posible.

4. Se cuantificó el tiempo alcanzado.

5. Se realizó la exhalación.

6. Se adquirió la señal ECG.

7. Se registraron las derivaciones DI, DII y DIII.

8. Entre las mediciones se dejó un período de descanso de aproximadamente **1 minuto y 30 segundos**.

### Objetivo

El objetivo de esta etapa fue observar las modificaciones de la actividad cardíaca durante una disminución temporal de la ventilación y comparar los resultados con las condiciones basal e hiperventilación.

### Tiempo de retención

**Tiempo registrado: [COLOCAR AQUÍ EL TIEMPO OBTENIDO] segundos.**

### Señales de las tres derivaciones en OpenSignals

#### Derivación I — DI

![Hipoventilación DI en OpenSignals](imagenes_opensignal/Hipo%20D1%2014-20%20segundos%20%281%29.png)

#### Derivación II — DII

![Hipoventilación DII en OpenSignals](imagenes_opensignal/Hipo%20D2%2014-20%20segundos%20%281%29.png)

#### Derivación III — DIII

![Hipoventilación DIII en OpenSignals](imagenes_opensignal/Hipo%20D3%2014-20%20segundos%20%281%29.png)


### Descripción

Durante la hipoventilación se realizó una retención voluntaria de la respiración. El registro obtenido permite analizar el comportamiento de la señal ECG durante esta condición y compararlo con el registro basal y la hiperventilación.


## 5.4. Actividad aeróbica

La cuarta etapa consistió en realizar una **actividad aeróbica** con el propósito de evaluar la respuesta cardiovascular frente al ejercicio.

La actividad tuvo una duración aproximada de **2 minutos y 50 segundos**.

### Procedimiento

1. Se verificó que los electrodos permanecieran correctamente colocados.

2. El participante realizó la actividad aeróbica durante aproximadamente 2 minutos y 50 segundos.

3. Al finalizar el ejercicio se inició rápidamente la adquisición del ECG.

4. Se registraron las tres derivaciones:

   - DI

   - DII

   - DIII.

5. Se dejó un intervalo aproximado de **30 segundos entre cada derivación**.

La adquisición se realizó rápidamente después de finalizar la actividad para registrar la respuesta cardíaca durante el período inicial de recuperación.

### Objetivo

El objetivo de esta etapa fue observar la respuesta de la actividad eléctrica cardíaca ante el aumento de la demanda cardiovascular producido por la actividad física.

### Señales de las tres derivaciones en OpenSignals

#### Derivación I — DI

![Actividad aeróbica DI en OpenSignals](imagenes_opensignal/Aerobico%20D1%2010-15%20segundos%20%281%29.png)

#### Derivación II — DII

![Actividad aeróbica DII en OpenSignals](imagenes_opensignal/Aerobica%20D2%2010-15%20segundos%20%281%29.png)

#### Derivación III — DIII

![Actividad aeróbica DIII en OpenSignals](imagenes_opensignal/Aerobico%20D3%2010-15%20segundos%20%281%29.png)


### Descripción

Después de finalizar la actividad aeróbica se registró rápidamente el ECG para observar la respuesta cardiovascular producida por el ejercicio. Esta condición permite comparar la señal con el estado basal y con las pruebas respiratorias.


# 6. Resumen del protocolo experimental

El procedimiento completo realizado durante el laboratorio se resume en la siguiente tabla:

| Etapa | Condición | Procedimiento | Duración aproximada | Derivaciones |

|------|-----------|---------------|---------------------|--------------|

| **1** | Basal | Registro en reposo | 30 s | DI, DII, DIII |

| **2** | Hiperventilación | Inhalar, mantener y exhalar | 30 s | DI, DII, DIII |

| **3** | Hipoventilación | Retención voluntaria de la respiración | Según el tiempo alcanzado | DI, DII, DIII |

| **4** | Actividad aeróbica | Ejercicio y medición inmediata | 2 min 50 s | DI, DII, DIII |

Entre las mediciones se realizaron períodos de descanso de acuerdo con el protocolo utilizado durante la práctica.


# 7. Video de la señal en reposo

Como parte de los entregables se realizó un video correspondiente a la adquisición de la señal ECG durante la condición de reposo.

En el video se puede observar:

- La colocación de los electrodos sobre el cuerpo.

- La conexión de los electrodos con BITalino.

- La adquisición de la señal ECG.

- La señal ECG visualizada durante el registro.

### Videos del laboratorio

Los videos grabados durante el laboratorio se encuentran almacenados en una carpeta independiente dentro del mismo repositorio.

**📁 Acceder a los videos del laboratorio:**

[▶️ Ver carpeta de videos del laboratorio](videos/)

> En la carpeta videos/ se pueden almacenar todos los videos registrados durante la práctica. De esta manera, el README mantiene una estructura ordenada y los archivos multimedia pueden consultarse mediante el enlace anterior.


# 8. Ploteo de la señal en OpenSignals

La señal ECG adquirida mediante BITalino fue visualizada utilizando el software **OpenSignals**.

Durante la adquisición se observaron las señales correspondientes a las tres derivaciones:

- **DI**

- **DII**

- **DIII**

La visualización permitió comprobar la adquisición de la señal y verificar que la conexión de los electrodos fuera adecuada.

## 8.1. Condición basal

![Basal DI](imagenes_opensignal/Basal%20D1%2014-20%20segundos%20%281%29.png)

![Basal DII](imagenes_opensignal/Basal%20D2%2014-20%20segundos%20%281%29.png)

![Basal DIII](imagenes_opensignal/Basal%20D3%2014-20%20segundos%20%281%29.png)

## 8.2. Hiperventilación

![Hiperventilación DI](imagenes_opensignal/Hiper%20D1%2010-15%20segundos%20%281%29.png)

![Hiperventilación DII](imagenes_opensignal/Hiper%20D2%2010-15%20segundos%20%281%29.png)

![Hiperventilación DIII](imagenes_opensignal/Hiper%20D3%2010-15%20segundos%20%281%29.png)

## 8.3. Hipoventilación

![Hipoventilación DI](imagenes_opensignal/Hipo%20D1%2014-20%20segundos%20%281%29.png)

![Hipoventilación DII](imagenes_opensignal/Hipo%20D2%2014-20%20segundos%20%281%29.png)

![Hipoventilación DIII](imagenes_opensignal/Hipo%20D3%2014-20%20segundos%20%281%29.png)

## 8.4. Actividad aeróbica

![Actividad aeróbica DI](imagenes_opensignal/Aerobico%20D1%2010-15%20segundos%20%281%29.png)

![Actividad aeróbica DII](imagenes_opensignal/Aerobica%20D2%2010-15%20segundos%20%281%29.png)

![Actividad aeróbica DIII](imagenes_opensignal/Aerobico%20D3%2010-15%20segundos%20%281%29.png)

> Las imágenes anteriores corresponden a los registros realizados en OpenSignals para las tres derivaciones y las diferentes condiciones experimentales.


# 9. Resumen y explicación de la señal ECG

El **electrocardiograma (ECG)** es una representación gráfica de la actividad eléctrica generada por el corazón durante cada ciclo cardíaco.

La actividad eléctrica cardíaca produce variaciones de potencial que pueden ser detectadas mediante electrodos colocados sobre la superficie corporal.

En una señal ECG se pueden identificar principalmente los siguientes componentes:

### Onda P

La onda P está relacionada principalmente con la despolarización de las aurículas y aparece antes del complejo QRS.

### Complejo QRS

El complejo QRS representa principalmente la despolarización de los ventrículos.

Dentro del complejo QRS se encuentra el pico R, que generalmente presenta una amplitud destacada y puede utilizarse para identificar los diferentes latidos cardíacos.

### Onda T

La onda T está relacionada principalmente con la repolarización ventricular y aparece después del complejo QRS.

### Representación simplificada de un ECG

                 R

                /\\

               /  \\

      P       /    \              T

     /\      /      \            /\\

    /  \\_/        \\___/  \\__

_/*__*____________

La identificación de estos componentes permite analizar características como la frecuencia cardíaca, los intervalos entre latidos y la morfología de la señal.


# 10. Frecuencia cardíaca e intervalo R-R

Una de las variables que puede obtenerse a partir de la señal ECG es la **frecuencia cardíaca**.

Para determinarla se identifican los picos R correspondientes a cada latido y se mide el tiempo entre dos picos R consecutivos. Este intervalo se denomina **intervalo R-R**.

La frecuencia cardíaca puede estimarse mediante:

**Frecuencia cardíaca (BPM) = 60 / intervalo R-R (s)**

Cuando el intervalo R-R disminuye, la frecuencia cardíaca aumenta.

Por el contrario, cuando el intervalo R-R aumenta, la frecuencia cardíaca disminuye.

El análisis de estos intervalos permite comparar la respuesta cardíaca entre la condición basal, la hiperventilación, la hipoventilación y la actividad aeróbica.


# 11. Procesamiento de la señal en Python

Los datos obtenidos durante el laboratorio fueron procesados utilizando **Python**.

El procesamiento permitió visualizar las señales ECG en función del tiempo y analizar sus principales características.

Las etapas principales del procesamiento fueron:

1. Importación de los datos obtenidos mediante BITalino.

2. Identificación de los canales correspondientes a la señal ECG.

3. Conversión de las muestras a una escala temporal.

4. Visualización de la señal original.

5. Aplicación de filtrado cuando fue necesario.

6. Identificación de los complejos QRS.

7. Detección de los picos R.

8. Cálculo de los intervalos R-R.

9. Estimación de la frecuencia cardíaca.

10. Comparación de las señales correspondientes a las diferentes condiciones experimentales.

El procesamiento permitió obtener una representación más clara de la señal y facilitar el análisis de sus características.


# 12. Ploteo de la señal en Python

Después de importar y procesar los datos obtenidos mediante BITalino, se realizó el ploteo de las señales ECG utilizando Python.

## 12.1. Condición basal

### Derivación I — DI

![Basal DI en Python](imagenes_python/Basal%201%20%281%29.png)

### Derivación II — DII

![Basal DII en Python](imagenes_python/Basal%20D2%20%281%29.png)

### Derivación III — DIII

![Basal DIII en Python](imagenes_python/Basal%20D3%20%281%29.png)

## 12.2. Hiperventilación

### Derivación I — DI

![Hiperventilación DI en Python](imagenes_python/Hiper%20D1%20%281%29.png)

### Derivación II — DII

![Hiperventilación DII en Python](imagenes_python/Hiper%20D2%20%281%29.png)

### Derivación III — DIII

![Hiperventilación DIII en Python](imagenes_python/Hiper%20D3%20%281%29.png)

## 12.3. Hipoventilación

### Derivación I — DI

![Hipoventilación DI en Python](imagenes_python/Hipo%20D1%20%281%29.png)

### Derivación II — DII

![Hipoventilación DII en Python](imagenes_python/Hipo%20D2%20%281%29.png)

### Derivación III — DIII

![Hipoventilación DIII en Python](imagenes_python/Hipo%20D3%20%281%29.png)

## 12.4. Actividad aeróbica

### Derivación I — DI

![Actividad aeróbica DI en Python](imagenes_python/Aerobico%20D1%20%281%29.png)

### Derivación II — DII

![Actividad aeróbica DII en Python](imagenes_python/Aerobico%20D2%20%281%29.png)

### Derivación III — DIII

![Actividad aeróbica DIII en Python](imagenes_python/Aerobico%20D3%20%281%29.png)


# 13. Comparación de las condiciones experimentales

Las señales obtenidas durante el laboratorio permiten comparar la actividad cardíaca bajo diferentes condiciones fisiológicas.

## 13.1. Condición basal

La condición basal corresponde al registro realizado durante el reposo y representa la referencia para las demás mediciones.

En esta condición se espera observar el comportamiento de la señal ECG correspondiente al estado de reposo del participante.

## 13.2. Hiperventilación

Durante la hiperventilación se modificó voluntariamente el patrón respiratorio del participante.

Esta condición permitió observar posibles variaciones en la frecuencia cardíaca y en los intervalos R-R respecto a la condición basal.

## 13.3. Hipoventilación

Durante la hipoventilación se realizó una retención voluntaria de la respiración.

Esta condición permitió observar el comportamiento de la señal ECG durante una disminución temporal de la ventilación.

## 13.4. Actividad aeróbica

Después de realizar la actividad aeróbica se registró rápidamente la señal ECG.

Esta condición permitió observar la respuesta cardiovascular producida por el ejercicio y compararla con la condición de reposo.


# 14. Comparación de resultados

A partir de las señales obtenidas se puede realizar una comparación de los principales parámetros del ECG entre las diferentes condiciones experimentales.

| Condición | Frecuencia cardíaca | Intervalo R-R | Observación |

|-----------|---------------------|----------------|-------------|

| Basal | [COLOCAR VALOR] BPM | [COLOCAR VALOR] s | [COLOCAR OBSERVACIÓN] |

| Hiperventilación | [COLOCAR VALOR] BPM | [COLOCAR VALOR] s | [COLOCAR OBSERVACIÓN] |

| Hipoventilación | [COLOCAR VALOR] BPM | [COLOCAR VALOR] s | [COLOCAR OBSERVACIÓN] |

| Actividad aeróbica | [COLOCAR VALOR] BPM | [COLOCAR VALOR] s | [COLOCAR OBSERVACIÓN] |

Esta comparación permitirá identificar las variaciones de la frecuencia cardíaca y de los intervalos R-R producidas por los cambios en la respiración y por la actividad física.

### Gráfica comparativa

**INSERTAR AQUÍ UNA GRÁFICA COMPARATIVA DE LA FRECUENCIA CARDÍACA ENTRE LAS CUATRO CONDICIONES, SI SE REALIZÓ.**

![Comparación de frecuencia cardíaca](imagenes/comparacion_frecuencia.png)