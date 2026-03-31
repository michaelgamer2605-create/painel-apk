from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.switch import Switch

class Linha(BoxLayout):
    def __init__(self, texto, **kwargs):
        super().__init__(orientation='horizontal', size_hint_y=None, height=50, **kwargs)
        self.add_widget(Label(text=texto))
        self.add_widget(Switch())

class Painel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.add_widget(Label(text="PAINEL 🔥"))

        self.add_widget(Linha("Aimbot"))
        self.add_widget(Linha("ESP"))
        self.add_widget(Linha("Wallhack"))

class MeuApp(App):
    def build(self):
        return Painel()

if __name__ == "__main__":
    MeuApp().run()