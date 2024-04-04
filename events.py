from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class EventsApp(App):
    def build(self):
        # Un BoxLayout acomoda cada widget en una caja rectangular
        # Horizontal o Verticalmente dependiendo del parametro orientation
        Contenedor = BoxLayout(orientation='vertical')

        # TextInput permite al usuario ingresar texto
        Texto = TextInput(font_size=50,
                      size_hint_y=None,
                      height=100,
                      text='Escriba aqui')
        Contenedor.add_widget(Texto)

        # Scatter contiene la lógica para poder ser arrastrado con el mouse
        Etiqueta = Label(text='Múeveme',
                  font_size=150)
        Contenedor.add_widget(Etiqueta)

        Boton = Button(text="Saludame")

        # El método bind() crea un enlace al cambiar las propiedades de un widget
        # para que se ejecute código en otro lugar
        Boton.bind(on_press=self.callback)

        Contenedor.add_widget(Boton)

        # Siempre se retorna el widget que contiene a todos los demás
        return Contenedor
    
    def callback( instance, value ):
        print( "Click!" )

if __name__ == "__main__":
    EventsApp().run()