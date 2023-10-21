import warnings
warnings.filterwarnings("ignore")
import os,json 

# Obtiene la ruta del directorio del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construye la ruta relativa desde el directorio del script
relative_path = os.path.join(script_dir, ".cache/huggingface")

# Establece la variable de entorno
os.environ["HF_HOME"] = relative_path

from transformers import AutoTokenizer, BertForSequenceClassification, AdamW
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import torch

model_base_fine_tunned = os.path.join(script_dir, ".cache/app-models-fine-tunned/model_base_fine_tunned")

# Preparación de datos y tokenización
tokenizer = AutoTokenizer.from_pretrained(model_base_fine_tunned)
model = BertForSequenceClassification.from_pretrained(model_base_fine_tunned)

# Predicciones en nuevos textos
new_texts =  ["fue lo espectacular, remendada!", "horrible espectáculo, no se la recomiendo a nadie"]
new_inputs = tokenizer(new_texts, return_tensors="pt", padding=True, truncation=True)
new_outputs = model(**new_inputs)
predicted_labels = torch.argmax(new_outputs.logits, dim=1)

for text, label in zip(new_texts, predicted_labels):
    print(f"Texto: {text} - Sentimiento: {label}")
