# Resultados principales

Los siguientes resultados corresponden a una evaluación sobre una submuestra de prueba de IMDb de 2000 ejemplos.

## Métricas en test

| Métrica | Resultado |
|---|---:|
| Accuracy | 90.10% |
| Precision | 89.08% |
| Recall | 91.40% |
| F1-score | 90.23% |

## Matriz de confusión

| | Predicho negativo | Predicho positivo |
|---|---:|---:|
| Real negativo | 888 | 112 |
| Real positivo | 86 | 914 |

## Interpretación breve

El modelo presenta un desempeño balanceado entre ambas clases. Se observa una ligera tendencia a clasificar algunas reseñas negativas como positivas, ya que se obtuvieron 112 falsos positivos frente a 86 falsos negativos.

## Comparación con baseline preliminar

| Métrica | Baseline preliminar | Modelo fine-tuneado |
|---|---:|---:|
| Accuracy | 85.20% | 90.10% |
| Precision | 84.40% | 89.08% |
| F1-score | 85.08% | 90.23% |

El fine-tuning permitió mejorar el desempeño respecto al entrenamiento preliminar reportado en el primer avance del proyecto.
