from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.switch import Switch
from kivy.uix.label import Label
import json

CONFIG_FILE = "config.json"

def salvar(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f)

def carregar():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except:
        return {"aim": False, "esp": False}

class Painel(App):
    def build(self):
        self.config = carregar()

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        titulo = Label(text="🔥 Painel PRO", font_size=24)
        layout.add_widget(titulo)

        self.aim_switch = Switch(active=self.config["aim"])
        layout.add_widget(Label(text="AIM"))
        layout.add_widget(self.aim_switch)

        self.esp_switch = Switch(active=self.config["esp"])
        layout.add_widget(Label(text="ESP"))
        layout.add_widget(self.esp_switch)

        btn = Label(text="[ Clique para salvar ]", markup=True)
        btn.bind(on_touch_down=self.salvar_config)
        layout.add_widget(btn)

        return layout

    def salvar_config(self, *args):
        data = {
            "aim": self.aim_switch.active,
            "esp": self.esp_switch.active
        }
        salvar(data)

Painel().run()
