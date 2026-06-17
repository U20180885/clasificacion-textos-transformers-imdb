# clasificacion-textos-transformers-imdb

Proyecto de Deep Learning para clasificación binaria de sentimientos en reseñas IMDb usando DistilBERT y Hugging Face.





Proyecto final del curso Deep Learning \[1INF52].  

El objetivo es desarrollar un clasificador binario de sentimientos capaz de identificar si una reseña de película en inglés expresa una polaridad positiva o negativa.



\## Integrantes



\- Frank Kevin Jiménez Valencia

\- Gustavo Alberto Torres Flores

\- Guillermo Francisco Lozano Rodriguez

\- Alvaro Javier Escudero Lay



\## Dataset



El dataset principal utilizado es IMDb, un corpus de reseñas de películas en inglés para clasificación binaria de sentimientos. Cada reseña está etiquetada como negativa o positiva.



También se considera Amazon Polarity como dataset complementario para evaluar generalización en otro dominio textual.



\## Modelo



El modelo base utilizado es `distilbert-base-uncased`, una versión optimizada de BERT que reduce el costo computacional manteniendo un buen desempeño en tareas de comprensión de lenguaje.



\## Pipeline implementado



El notebook principal incluye:



1\. Carga del dataset desde Hugging Face.

2\. Exploración inicial de datos.

3\. Separación en train, validation y test.

4\. Tokenización con DistilBERT.

5\. Fine-tuning del modelo.

6\. Evaluación con métricas.

7\. Matriz de confusión.

8\. Comparación contra el baseline inicial.



\## Resultados principales



Sobre una submuestra de prueba de IMDb, el modelo obtuvo:



| Métrica | Resultado |

|---|---:|

| Accuracy | 90.10% |

| Precision | 89.08% |

| Recall | 91.40% |

| F1-score | 90.23% |



\## Demo



La demo interactiva fue implementada con Gradio y publicada en Hugging Face Spaces:



\[Demo en Hugging Face Spaces](PEGAR\_AQUI\_EL\_LINK\_DEL\_SPACE)



\## Estructura del repositorio



```text

notebooks/

&#x20; 02\_finetuning\_distilbert\_imdb.ipynb



demo/

&#x20; app.py

&#x20; requirements.txt



results/

&#x20; matriz\_confusion\_imdb.png

&#x20; metricas\_resultados.md



docs/

&#x20; capturas\_demo/

