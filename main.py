from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class Linha(BoxLayout):
    def __init__(self, texto, **kwargs):
        super().__init__(orientation='horizontal', size_hint_y=None, height=50, **kwargs)

        self.add_widget(Label(text=texto, color=(1,1,1,1)))
        self.add_widget(Switch())

class Painel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        # Fundo preto
        with self.canvas.before:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

        # Título
        self.add_widget(Label(text="PAINEL PRO 🔥", font_size=24, color=(1,0,1,1)))

        # Seções
        self.add_widget(Label(text="AIM", color=(1,0,1,1)))
        self.add_widget(Linha("Aimbot"))
        self.add_widget(Linha("Aim Suave"))

        self.add_widget(Label(text="ESP", color=(1,0,1,1)))
        self.add_widget(Linha("ESP Linha"))
        self.add_widget(Linha("ESP Caixa"))
        self.add_widget(Linha("ESP Nome"))
        self.add_widget(Linha("ESP Vida"))

        self.add_widget(Label(text="MISC", color=(1,0,1,1)))
        self.add_widget(Linha("Velocidade"))
        self.add_widget(Linha("Pulo Alto"))

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class MeuApp(App):
    def build(self):
        return Painel()

if __name__ == "__main__":
    MeuApp().run()
