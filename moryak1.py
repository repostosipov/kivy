from kivymd.app import MDApp
from kivymd.uix.list import ImageLeftWidget
from kivy.lang import Builder
from kivymd.uix.list import ThreeLineAvatarListItem
from kivy.core.window import Window

Window.size = (500,800)

list_helper = """

Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Моряк Инфо'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["dots-vertical", lambda x: app.callback()]]
            elevation:5
        ScrollView:
            MDList:
                id: container 
        MDBottomAppBar:
            MDToolbar:
                icon: 'sail-boat'
                type: 'bottom'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                on_action_button: app.navigation_draw()
                
"""

class MoryakApp(MDApp):
    
    def build(self):
        screen = Builder.load_string(list_helper)
        return screen

    def on_start(self):
        for i in range(20):
            items = ThreeLineAvatarListItem(text='Вакансия ' + str(i), secondary_text="Описание ",tertiary_text='Дата')
            image = ImageLeftWidget(source='mini3.png')
            items.add_widget(image)
            self.root.ids.container.add_widget(items)

    def navigation_draw(self):
        print("Navigation")

MoryakApp().run()