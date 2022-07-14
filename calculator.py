from kivy. app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

KV = """
box:

    id: root_widget
    orientation: 'vertical'

    TextInput:
        id: entry
        font_size: 32
        multiline: False

    Button:
        text: '='
        font_size: 64
        on_press: root_widget.result (entry. text)

    Label:
        id: itog
        text: 'Итого'
        font_size: 64
"""

class box (BoxLayout):
    def result (self, entry_text):
        if entry_text:
            try:
                result = str (eval (entry_text))
                self.ids ['itog'].text = result
            except Exception:
                self.ids ['itog'].text = 'Ошибка'

class MainApp (App):
    def build (self):
        return Builder. load_string (KV)

MainApp().run ()