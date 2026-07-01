# Clasificación de Textos empleando Transformers usando IMDb

Proyecto final del curso **Deep Learning [1INF52]**.

El objetivo del proyecto es desarrollar un clasificador binario de sentimientos capaz de identificar si una reseña de película en inglés expresa una polaridad **positiva** o **negativa**, utilizando modelos basados en Transformers y herramientas de Hugging Face.

## Integrantes

- Frank Kevin Jiménez Valencia
- Gustavo Alberto Torres Flores
- Guillermo Francisco Lozano Rodriguez
- Alvaro Javier Escudero Lay

## Dataset

El dataset principal utilizado es **IMDb**, un corpus de reseñas de películas en inglés empleado para clasificación binaria de sentimientos. Cada reseña está etiquetada como negativa o positiva.

Además, se considera **Amazon Polarity** como dataset complementario para evaluar el comportamiento del modelo en un dominio textual distinto, compuesto por reseñas de productos.

## Modelo

El modelo base utilizado es `distilbert-base-uncased`, una versión optimizada de BERT que reduce el costo computacional manteniendo un buen desempeño en tareas de comprensión de lenguaje natural.

DistilBERT fue fine-tuneado sobre una submuestra del dataset IMDb para adaptar sus representaciones contextuales a la tarea de clasificación binaria de sentimientos.

El repositorio incluye la carpeta `modelo_distilbert_imdb/`, que contiene el modelo fine-tuneado utilizado por la demo local.

## Pipeline implementado

El notebook principal incluye las siguientes etapas:

1. Carga del dataset IMDb desde Hugging Face.
2. Exploración inicial de datos.
3. Separación en conjuntos de entrenamiento, validación y prueba.
4. Tokenización con el tokenizador de DistilBERT.
5. Fine-tuning del modelo `distilbert-base-uncased`.
6. Evaluación con métricas de clasificación.
7. Generación de matriz de confusión.
8. Comparación contra el baseline preliminar.
9. Análisis de errores.
10. Evaluación complementaria con Amazon Polarity.

## Resultados principales

Los siguientes resultados corresponden a una evaluación sobre una submuestra de prueba de IMDb de 2000 ejemplos.

| Métrica | Resultado |
|---|---:|
| Accuracy | 90.10% |
| Precision | 89.08% |
| Recall | 91.40% |
| F1-score | 90.23% |

La matriz de confusión obtenida sobre la muestra de prueba fue la siguiente:

| | Predicho negativo | Predicho positivo |
|---|---:|---:|
| Real negativo | 888 | 112 |
| Real positivo | 86 | 914 |

Estos resultados muestran un desempeño balanceado entre ambas clases, con una ligera tendencia a clasificar algunas reseñas negativas como positivas.

## Demo

La demo interactiva fue implementada con **Gradio** y publicada en **Hugging Face Spaces**:

[Demo en Hugging Face Spaces](https://huggingface.co/spaces/GuillermoLozano/CLASIFICACION_DE_TEXTOS_TRANSFORMERS_IMDB)

La aplicación permite ingresar una reseña de película en inglés y devuelve la polaridad estimada junto con un nivel de confianza.

## Estructura del repositorio

```text
clasificacion-textos-transformers-imdb/
├── README.md
├── requirements.txt
├── .gitattributes
├── .gitignore
├── modelo_distilbert_imdb/
├── notebooks/
│   └── 02_finetuning_distilbert_imdb_v3.ipynb
├── demo/
│   ├── app.py
│   └── requirements.txt
├── results/
│   └── metricas_resultados.md
└── docs/
    └── capturas_demo/
```

## Ejecución del notebook

Para ejecutar el notebook de fine-tuning, se recomienda usar Google Colab con GPU habilitada.

1. Instalar las dependencias principales:

```bash
pip install -r requirements.txt
```

2. Abrir el notebook:

```text
notebooks/02_finetuning_distilbert_imdb_v3.ipynb
```

3. Ejecutar las celdas en orden.

El notebook descarga el dataset desde Hugging Face, tokeniza los textos, realiza el fine-tuning de DistilBERT y evalúa el modelo con métricas de clasificación.

## Ejecución local de la demo

La demo puede ejecutarse localmente con Gradio usando la carpeta `modelo_distilbert_imdb/` incluida en el repositorio.

Desde la raíz del repositorio, ejecutar:

```bash
pip install -r demo/requirements.txt
python demo/app.py
```

Es importante ejecutar `python demo/app.py` desde la raíz del repositorio, porque el archivo `demo/app.py` carga el modelo desde la ruta:

```text
./modelo_distilbert_imdb
```

También puede usarse directamente la demo publicada en Hugging Face Spaces.

## Limitaciones

El modelo fue entrenado principalmente sobre reseñas de películas en inglés. Por ello, puede presentar limitaciones en los siguientes casos:

- textos en otros idiomas;
- dominios distintos al de reseñas de películas;
- sarcasmo o ironía;
- reseñas con sentimiento mixto;
- entradas demasiado largas que requieran truncamiento;
- textos con ruido o estructuras poco comunes.

## Trabajos futuros

Como mejoras futuras se propone:

- entrenar con una mayor proporción del dataset IMDb;
- evaluar configuraciones con `max_length=512`;
- realizar limpieza más exhaustiva de etiquetas HTML;
- comparar con otros modelos Transformer, como BERT o RoBERTa;
- realizar fine-tuning adicional o evaluación más amplia con Amazon Polarity;
- mejorar la interpretabilidad del modelo mediante LIME u otras técnicas.

## Referencias principales

- Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding**.
- Sanh, V., Debut, L., Chaumond, J., & Wolf, T. **DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter**.
- Maas, A. L., Daly, R. E., Pham, P. T., Huang, D., Ng, A. Y., & Potts, C. **Learning Word Vectors for Sentiment Analysis**.
- Ribeiro, M. T., Singh, S., & Guestrin, C. **“Why Should I Trust You?” Explaining the Predictions of Any Classifier**.
- Hugging Face. **Transformers Documentation**.
- Hugging Face. **Datasets Documentation**.
- Gradio. **Gradio Documentation**.
