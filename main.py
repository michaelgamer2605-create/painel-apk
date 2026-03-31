from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.switch import Switch
from kivy.uix.label import Label

class Painel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.add_widget(Label(text="PAINEL ADMIN 🔥"))

        self.add_widget(Label(text="Aimbot"))
        self.add_widget(Switch())

        self.add_widget(Label(text="ESP"))
        self.add_widget(Switch())

        self.add_widget(Label(text="Wallhack"))
        self.add_widget(Switch())

class MeuApp(App):
    def build(self):
        return Painel()

MeuApp().run()
