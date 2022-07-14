from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500,800)

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Moryak Info'
        MDLabel:
            text: 'Моряк Инфо'
            halign: 'center'
"""

class MoryakApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

MoryakApp().run()