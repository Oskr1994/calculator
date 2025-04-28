from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class CalculadoraApp(App):
    def build(self):
        # Usamos BoxLayout para contener el resultado y los botones
        root = BoxLayout(orientation='vertical')
        
        # Campo de texto donde se muestra el resultado
        self.resultado = TextInput(
            font_size=32, 
            readonly=True, 
            halign='right', 
            multiline=False,
            size_hint=(1, None),  # Ocupa toda la fila (ancho completo)
            height=100  # Altura fija en 100 píxeles
        )
        
        # Agregamos el campo de texto al layout
        root.add_widget(self.resultado)
        
        # Creamos un GridLayout para los botones
        layout = GridLayout(cols=4)
        
        botones = [
            ('7', self.agregar_numero),
            ('8', self.agregar_numero),
            ('9', self.agregar_numero),
            ('/', self.agregar_operador),
            ('4', self.agregar_numero),
            ('5', self.agregar_numero),
            ('6', self.agregar_numero),
            ('*', self.agregar_operador),
            ('1', self.agregar_numero),
            ('2', self.agregar_numero),
            ('3', self.agregar_numero),
            ('-', self.agregar_operador),
            ('0', self.agregar_numero),
            ('.', self.agregar_numero),
            ('=', self.calcular),
            ('+', self.agregar_operador),
            ('C', self.borrar),
        ]
        
        # Agregar los botones al layout
        for texto, func in botones:
            boton = Button(text=texto, pos_hint={'center_x': 0.5, 'center_y': 0.5})
            boton.bind(on_press=func)
            layout.add_widget(boton)
        
        # Agregamos el GridLayout con los botones al root
        root.add_widget(layout)
        
        return root

    def agregar_numero(self, instance):
        self.resultado.text += instance.text

    def agregar_operador(self, instance):
        if self.resultado.text and self.resultado.text[-1] not in '+-*/':
            self.resultado.text += instance.text

    def calcular(self, instance):
        try:
            self.resultado.text = str(eval("eres bruto")) #self.resultado.text
        except Exception as e:
            self.resultado.text = 'Eres burro'

    def borrar(self, instance):
        self.resultado.text = ''

if __name__ == '__main__':
    CalculadoraApp().run()
