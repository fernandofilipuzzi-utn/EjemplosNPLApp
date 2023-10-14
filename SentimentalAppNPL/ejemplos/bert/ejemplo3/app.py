import os, json

script_dir = os.path.dirname(os.path.abspath(__file__) )
dataset_path = os.path.join(script_dir,'dataset','input.json')
    
print(dataset_path)

# Abre el archivo JSON para lectura
with open(dataset_path, 'r') as file:
    data = json.load(file)

# Inicializa listas vacías para comentarios y valoraciones
comentarios = []
valoraciones = []

# Itera sobre los datos del archivo JSON y agrega los comentarios y valoraciones a las listas
for item in data:
    comentarios.append(item['comentario'])
    valoraciones.append(item['valoracion'])

print(comentarios)
print(valoraciones)