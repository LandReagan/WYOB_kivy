from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('menu.kv')


class Menu(BoxLayout):

    def __init__(self, **kwargs):
        BoxLayout.__init__(self, **kwargs)