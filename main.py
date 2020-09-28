import eel                      # Importando la librería 'eel'

@eel.expose                     # Lleva la función de abajo a JavaScript, agregarlo para cada función!
def hello():                    # Definiendo la función 'hello'
    print('Hello World!')           # Cuerpo de la función 'hello'

@eel.expose                     
def segunda():                   
    print('Vamos bien')

eel.init("templates")           # Primero se invoca a la carpeta del front-end
eel.start("index.html")         # Segundo: se llama al html de la página principal