from kivy.app import App
from kivy.uix.button import Button

class Painel(App):
    def build(self):
        return Button(text="Painel Funcionando 🔥")

Painel().run()
