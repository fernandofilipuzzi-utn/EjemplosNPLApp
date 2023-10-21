
Ejecutar: 

==por primera vez, sitonía fina ==

bajado del repositorio, hay que descargar el modelo preentenado y sintonizarlo, por lo
tanto se crearán carpetas como .cache, y se alojaran varios archivos en .cache y .venv.
Se requiere varios gigas libres 

correr:

mkdir .venv
pipenv install
pipenv shell

luego, para la sintonía fina:

python app_fine_tunning.py

seguido, se puede probar si todo está correcto con:

python app_test_fine_tunning.py

finalmente, cambiar la ip en app_rest_api.py y correr con:

python app_rest_api.py


==para lanzar el servicio, realizado los pasos anteriores ==
mkdir .venv
pipenv shell
python app_rest_api.py


==consulta de la api==
http://ip_configurada/swagger