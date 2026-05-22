# Predicción y Codificación de Curvas S11 usando Inteligencia Artificial

Este repositorio contiene el desarrollo del **Trabajo Encargado 02**, enfocado en el diseño de un sistema inteligente capaz de modelar e invertir el comportamiento electromagnético de una antena a partir de su coeficiente de reflexión ($S_{11}$). El objetivo principal es evaluar cómo influye la reducción de dimensionalidad en el entrenamiento de Redes Neuronales Artificiales (MLP).

## Estructura del Repositorio

El proyecto está organizado de la siguiente manera:
* `exploracion_datos.ipynb`: Jupyter Notebook principal que contiene todo el pipeline de código ejecutable, la carga de datos, cálculo de correlación, entrenamiento de modelos de TensorFlow y las visualizaciones gráficas.
* `archivo2.py`: Script base de referencia provisto para la asignación.
* `requirements.txt`: Archivo de configuración que detalla las dependencias y librerías de Python necesarias para replicar el entorno.
* `README.md`: Documentación técnica e informe del proyecto (este archivo).

*Nota: Los archivos masivos de datos `.h5` (`train_test_split_S11.h5` y `train_test_split_S11encode_17d_sortf.h5`) han sido omitidos del repositorio local mediante políticas de Git debido a restricciones de almacenamiento de GitHub y para proteger la integridad de los datos de origen de la IEEE.*

## Especificaciones del Dataset (Hoja Técnica)

Se implementó una estrategia estricta de división de datos utilizando conjuntos independientes de entrenamiento (*train*) y prueba (*test*), garantizando la prohibición absoluta de mezclar datos de validación con entrenamiento (*data leakage*):

* **Datos Originales del Espectro ($S_{11}$):**
  * `S11_combine_train`: 138,249 muestras con 101 puntos de frecuencia.
  * `S11_combine_test`: 59,250 muestras con 101 puntos de frecuencia.
* **Datos Comprimidos (Features Codificadas):**
  * `S11_encode_train`: 138,249 muestras mapeadas a un espacio latente de 17 dimensiones.
  * `S11_encode_test`: 59,250 muestras mapeadas a un espacio latente de 17 dimensiones.
* **Variables de Salida (Etiquetas de Regresión):**
  * `final_params_combine_train` / `test`: 8 parámetros geométricos y físicos de la estructura de la antena.

## Arquitectura del Pipeline de Inteligencia Artificial

El enfoque seleccionado corresponde al **Modelado Inverso de Diseño de Antenas**. Se diseñaron dos arquitecturas de Redes Neuronales Artificiales Multicapa (MLP) en Python usando **TensorFlow/Keras**:
1. **Modelo Original (101d):** Aprende la relación directa $S_{11_{101}} \rightarrow \text{Parámetros}_8$.
2. **Modelo Codificado (17d):** Evalúa el rendimiento utilizando la representación reducida de variables como entrada.

**Parámetros de Configuración Comunes:**
* **Capas Ocultas:** Capas densas totalmente conectadas de 128, 64 y 32 neuronas.
* **Funciones de Activación:** No lineales de tipo `ReLU` en las capas intermedias para capturar las resonancias complejas, y activación `Linear` en la capa de salida.
* **Optimización:** Optimizador Adam minimizando la pérdida por Error Cuadrático Medio (MSE). Un 20% del set