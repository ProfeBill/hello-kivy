from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class InputApp(App):
    def build(self):
        # Un BoxLayout acomoda cada widget en una caja rectangular
        # Horizontal o Verticalmente dependiendo del parametro orientation
        Contenedor = BoxLayout(orientation='vertical')

        # TextInput permite al usuario ingresar texto
        Texto = TextInput(font_size=50,
                      size_hint_y=None,
                      height=100,
                      text='Escriba aqui')

        # Scatter contiene la lógica para poder ser arrastrado con el mouse
        Movible = Scatter()
        Etiqueta = Label(text='Múeveme',
                  font_size=150)
        
        # Ponemos la etiqueta dentro del Scatter
        Movible.add_widget(Etiqueta)

        # FloatLayout permite que los widgets que contiene cambien de posición        
        ContenedorLibre = FloatLayout()
        ContenedorLibre.add_widget(Movible)

        # Ponemos los dos controles dentro del panel principal
        Contenedor.add_widget(Texto)
        Contenedor.add_widget(ContenedorLibre)

        # El método bind() crea un enlace al cambiar las propiedades de un widget
        # para que se ejecute código en otro lugar
        Texto.bind(text=Etiqueta.setter('text'))

        # Siempre se retorna el widget que contiene a todos los demás
        return Contenedor

if __name__ == "__main__":
    InputApp().run()