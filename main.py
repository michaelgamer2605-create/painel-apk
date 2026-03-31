from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Painel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.add_widget(Label(text="PAINEL OK 🔥"))

class MeuApp(App):
    def build(self):
        return Painel()

if __name__ == "__main__":
    MeuApp().run()
