import warnings, os

warnings.filterwarnings("ignore")

script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(script_dir, "../.cache/huggingface")
os.environ["HF_HOME"] = relative_path

from transformers import AutoTokenizer, BertForSequenceClassification, AdamW
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import torch, json  


class SentimentalModel:

    def __init__(self):
        self.script_dir=script_dir
        self.relative_path=relative_path

        if not os.path.exists(self.relative_path):
            os.makedirs(self.relative_path)     
         
        #model_base = "bert-base-uncased"
        self.model_base = "mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"

        print(self.relative_path)
        

    def FineTunning(self):
        # Preparación de datos y tokenización
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_base)
        self.model = BertForSequenceClassification.from_pretrained(self.model_base, num_labels=11, ignore_mismatched_sizes=True)  

        train_texts, train_labels=self.__GetDataset()
        
        lengths = [len(item) for item in train_texts]
        average_length = sum(lengths) / len(lengths)
        model_max_length = int(average_length + 10)  # Agrega un pequeño margen


        # División de datos en conjunto de entrenamiento y prueba
        train_texts, val_texts, train_labels, val_labels = train_test_split(train_texts, train_labels, test_size=0.2, random_state=42)

        train_inputs = self.tokenizer(train_texts, return_tensors="pt", padding=True, truncation=True,max_length=model_max_length)
        val_inputs = self.tokenizer(val_texts, return_tensors="pt", padding=True, truncation=True,max_length=model_max_length)

        train_labels = torch.tensor(train_labels)
        val_labels = torch.tensor(val_labels)

        print(val_labels)

        # Entrenamiento
        optimizer = AdamW(self.model.parameters(), lr=1e-5)

        for epoch in range(500):  # Número de épocas 500
            outputs = self.model(**train_inputs, labels=train_labels)
            loss = outputs.loss
            loss.backward()
            optimizer.step()
            print(f"Epoch {epoch+1} - Loss: {loss.item()}")

        # Evaluación en el conjunto de prueba
        with torch.no_grad():
            val_outputs = self.model(**val_inputs)
            predicted_labels = torch.argmax(val_outputs.logits, dim=1)
            accuracy = accuracy_score(val_labels, predicted_labels)
            print(f"Accuracy on validation set: {accuracy:.2f}")
        
        # Guardar el modelo y el tokenizer en un directorio
        relative_path_fine_tunned = os.path.join(script_dir, '..','.cache','app-models-fine-tunned','model_base_fine_tunned')
        
        self.model.save_pretrained(relative_path_fine_tunned)
        self.tokenizer.save_pretrained(relative_path_fine_tunned)

    def CargaPretrained(self):
        model_base_fine_tunned = ".cache/app-models-fine-tunned/model_base_fine_tunned"

        self.tokenizer = AutoTokenizer.from_pretrained(model_base_fine_tunned)
        self.model = BertForSequenceClassification.from_pretrained(model_base_fine_tunned)

    def Evaluar(self, new_texts):
        # Predicciones en nuevos textos
        new_inputs = self.tokenizer(new_texts, return_tensors="pt", padding=True, truncation=True)
        new_outputs = self.model(**new_inputs)
        predicted_labels = torch.argmax(new_outputs.logits, dim=1)

        evaluaciones=[]

        for text, label in zip(new_texts, predicted_labels):
            evaluaciones.append({"comentario":text, "valoracion": label})
                    
        return evaluaciones

    def __GetDataset(self):
        script_dir = os.path.dirname(os.path.abspath(__file__)) 
        dataset_path = os.path.join(script_dir,'..','dataset','input.json')
    
        with open(dataset_path, 'r', encoding='utf-8') as file:        
            data = json.load(file)

        comentarios = []
        valoraciones = []

        for item in data:
            comentarios.append(item['comentario'])
            valoraciones.append(item['valoracion'])
        
        #print(comentarios)
        #print(valoraciones)

        return comentarios, valoraciones