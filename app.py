import gradio as gr
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch.nn.functional as F

# Cargar el tokenizer y el modelo guardados
MODEL_PATH = "./modelo_distilbert_imdb" 

tokenizer_demo = AutoTokenizer.from_pretrained(MODEL_PATH)
model_demo = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

device_demo = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_demo.to(device_demo)
model_demo.eval()

def predict_sentiment(text):
    """
    Función de predicción que toma un texto y devuelve el sentimiento (positivo/negativo)
    y la confianza asociada.
    """
    inputs = tokenizer_demo(
        text,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=256
    )
    
    inputs = {k: v.to(device_demo) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model_demo(**inputs)
        logits = outputs.logits
        probabilities = F.softmax(logits, dim=-1)[0] 

    predicted_class_id = torch.argmax(probabilities).item()

    sentiment_labels = {0: "NEGATIVO", 1: "POSITIVO"}
    predicted_sentiment = sentiment_labels[predicted_class_id]
    confidence = probabilities[predicted_class_id].item() * 100

    return f"Sentimiento: {predicted_sentiment} (Confianza: {confidence:.2f}%)"

# Crear la interfaz de Gradio
iface = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(lines=5, placeholder="Escribe tu reseña aquí..."),
    outputs="text",
    title="Análisis de Sentimientos de Reseñas de Películas",
    description="Un modelo para clasificar reseñas de películas como Positivas o Negativas.",
    examples=[
        ["This movie was a masterpiece, I highly recommend it to everyone."],
        ["What a terrible film, I fell asleep halfway through."],
        ["It had its moments, but overall it was just average."]
    ]
)

# Lanzar la interfaz sin "share=True"
iface.launch()