
from sentimental_model import SentimentalModel

model=SentimentalModel()

new_texts = ["Estoy enamorado!", "Odio este producto.", "Me parece bien.","Me resultó satisfactorio","No voy a volver a comprarlo!","Es un desastre todo","Me resulto tremendamente inutil"]

result_texts=model.Evaluar(new_texts)

for result in result_texts:
    print(f"{result['mensaje']} {result['calificacion']}")

    