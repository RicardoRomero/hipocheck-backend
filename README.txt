CONFIGURACION:
    #Verificar la version de python
    Python 3.12.0
    #Crear el entorno virtual
    python -m venv venv
    #Instalar las dependencias
    pip install -r requirements.txt

INICIAR SERVIDOR:
    #crear archivo.env en la ruta ./app
    #agregar las siguientes variables al archivo y guardar
        JWT_SECRET_KEY=key
        JWT_REFRESH_SECRET_KEY=secretkey
        MONGO_CONNECTION_STRING=mongodb://localhost:27017
        MONGO_DB=mortgageCalculatorDB
    
    #dirigirse a la ruta
    cd .\backend\ 
    #activar el entorno virtual
    .\venv\Scripts\activate  
    #iniciar el servidor
    

DOCUMENTACION DE ENDPOINTS
    #en el navegador pegar la siguiente ruta
    http://localhost:8000/docs#/