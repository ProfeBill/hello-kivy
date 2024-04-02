# hello.py
#
# Aplicación Kivy Mínima
#
# Para poder ejecutar, primero debe haber instalado Kivy en el proyecto
# usando el comando
#
#     pip install "kivy[base]"  
#

# Para poder utilizar Kivy en su aplicación, lo primero es importar
# la clasee App del módulo kivy.app
from kivy.app import App

# Cada componente que vaya a utilizar, debe ser importado 
from kivy.uix.label import Label

# Cada aplicación Kivy es una clase descendiente de la clase kivy.app.App
class HelloApp(App):
    
    # El método Build es el encargado de crear los controles visuales
    # que comprenden la ventana principal de la aplicación
    def build(self):
        # build() debe retornar el componente que contiene a todos los
        # demás controles de la ventana
        return Label(text="Hello World!")
    
# Para ejecutar la aplicación, se debe llamar al método run() de
# la clase principal descendiente de kivy.app.App
if __name__ == "__main__":
    HelloApp().run()