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
        self.Texto = TextInput(font_size=50,
                      size_hint_y=None,
                      height=100,
                      text='Escriba aqui')
        Contenedor.add_widget(self.Texto)

        # Scatter contiene la lógica para poder ser arrastrado con el mouse
        self.Etiqueta = Label(text='...',font_size=50)
        Contenedor.add_widget(self.Etiqueta)
        Boton = Button(text="Saludame",font_size=30)
        Contenedor.add_widget(Boton)

        # Conectar con el callback con el evento press del boton
        Boton.bind( on_press=self.callback )

        # Siempre se retorna el widget que contiene a todos los demás
        return Contenedor
    
    # instance es el widget que generó el evento
    # value es el valor actual que tiene el widget
    def callback( self, value ):
        self.Etiqueta.text =  "Hola " + self.Texto.text


if __name__ == "__main__":
    EventsApp().run()