import warnings
warnings.filterwarnings("ignore")
import os

from transformers import AutoTokenizer, BertForSequenceClassification, AdamW
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import torch

import json


script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(script_dir, '.cache','huggingface')
os.environ["HF_HOME"] = relative_path

model_base = "mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"

tokenizer = AutoTokenizer.from_pretrained(model_base)
model = BertForSequenceClassification.from_pretrained(model_base, num_labels=5, ignore_mismatched_sizes=True)  

train_texts = [
            "esto es muy bueno!, es excelente el producto",
            "el producto es regular",
            "excelente entrega",
            "excelente",
            "malisimo"
]

train_labels = [4, 3, 4, 4,0]

train_texts, val_texts, train_labels, val_labels = train_test_split(train_texts, train_labels, test_size=0.2, random_state=42)

train_inputs = tokenizer(train_texts, return_tensors="pt", padding=True, truncation=True)
val_inputs = tokenizer(val_texts, return_tensors="pt", padding=True, truncation=True)

train_labels = torch.tensor(train_labels)
val_labels = torch.tensor(val_labels)

print(val_labels)

# Entrenamiento
optimizer = AdamW(model.parameters(), lr=1e-5)

for epoch in range(20):  # Número de épocas
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
relative_path_fine_tunned = os.path.join(script_dir, '.cache','app-models-fine-tunned','model_base_fine_tunned')
        
model.save_pretrained(relative_path_fine_tunned)
tokenizer.save_pretrained(relative_path_fine_tunned)


os.environ["HF_HOME"] = os.path.join(script_dir, '..','.cache','huggingface')
model_base_fine_tunned = ".cache/app-models-fine-tunned/model_base_fine_tunned"

tokenizer = AutoTokenizer.from_pretrained(model_base_fine_tunned)
model = BertForSequenceClassification.from_pretrained(model_base_fine_tunned)
