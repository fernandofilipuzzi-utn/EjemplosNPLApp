import warnings
warnings.filterwarnings("ignore")
import os,json 

# Obtiene la ruta del directorio del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construye la ruta relativa desde el directorio del script
relative_path = os.path.join(script_dir, ".cache/huggingface")

# Establece la variable de entorno
os.environ["HF_HOME"] = relative_path

# la configuración de HF_CACHE debe ser antes de hacer los imports.
# sino toma el por default
from transformers import AutoTokenizer, BertForSequenceClassification, AdamW
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import torch

model_base = "bert-base-uncased"
model_base = "mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"
#model_base = "Toshifumi/bert-base-multilingual-cased-finetuned-emotion"
#modelo="edumunozsala/beto_sentiment_analysis_es"
#modelo="nlptown/bert-base-multilingual-uncased-sentiment"

# Preparación de datos y tokenización
tokenizer = AutoTokenizer.from_pretrained(model_base)
model = BertForSequenceClassification.from_pretrained(model_base, num_labels=11,ignore_mismatched_sizes=True)  # 3 etiquetas: positivo, negativo, neutro

# Datos de entrenamiento (reemplaza esto con tus propios datos)
script_dir = os.path.dirname(os.path.abspath(__file__)) 
dataset_path = os.path.join(script_dir,'input.json')
    
with open(dataset_path, 'r', encoding='utf-8') as file:        
    data = json.load(file)

train_texts = []
train_labels = []

for item in data:
    train_texts.append(item['comentario'])
    train_labels.append(item['valoracion'])


# División de datos en conjunto de entrenamiento y prueba
train_texts, val_texts, train_labels, val_labels = train_test_split(train_texts, train_labels, test_size=0.2, random_state=42)

train_inputs = tokenizer(train_texts, return_tensors="pt", padding=True, truncation=True)
val_inputs = tokenizer(val_texts, return_tensors="pt", padding=True, truncation=True)

train_labels = torch.tensor(train_labels)
val_labels = torch.tensor(val_labels)

print(val_labels)

# Entrenamiento
optimizer = AdamW(model.parameters(), lr=1e-5)

for epoch in range(500):  # Número de épocas
    outputs = model(**train_inputs, labels=train_labels)
    loss = outputs.loss
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1} - Loss: {loss.item()}")

# Evaluación en el conjunto de prueba
with torch.no_grad():
    val_outputs = model(**val_inputs)
    predicted_labels = torch.argmax(val_outputs.logits, dim=1)
    accuracy = accuracy_score(val_labels, predicted_labels)
    print(f"Accuracy on validation set: {accuracy:.2f}")

 # Guardar el modelo y el tokenizer en un directorio
relative_path_fine_tunned = os.path.join(script_dir, ".cache/app-models-fine-tunned/model_base_fine_tunned")

model.save_pretrained(relative_path_fine_tunned)
tokenizer.save_pretrained(relative_path_fine_tunned)