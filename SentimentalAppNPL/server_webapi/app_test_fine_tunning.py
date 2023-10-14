
from models.sentimental_model import SentimentalModel

model=SentimentalModel()
model.CargaPretrained()

new_texts = ["fue lo espectacular, remendada!", "horrible espectáculo, no se la recomiendo a nadie"]

result_texts=model.Evaluar(new_texts)

for result in result_texts:
    print(f"{result['comentario']} {result['valoracion']}")

    