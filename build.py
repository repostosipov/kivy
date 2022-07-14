from kivymd.app import MDApp
from kivymd.uix.list import ImageLeftWidget
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.uix.list import ThreeLineAvatarListItem
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


Window.size = (500,800)

list_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Моряк Инфо'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
                        elevation:5
                    ScrollView:
                        MDList:
                            id: container 
                    MDBottomAppBar:
                        MDToolbar:
                            icon: 'account'
                            type: 'bottom'
                            left_action_items: [["sail-boat", lambda x: app.navigation_draw()]]
                            on_action_button: app.navigation_draw()
        MDNavigationDrawer:
            id: nav_drawer  
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'logo.jpg'
                MDLabel:
                    text: '   dvmoryak@gmail.com'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Вакансии'
                            IconLeftWidget:
                                icon: 'sail-boat'
                        OneLineIconListItem:
                            text: 'Компании'
                            IconLeftWidget:
                                icon: 'pump'
                        OneLineIconListItem:
                            text: 'Личный кабинет'
                            IconLeftWidget:
                                icon: 'account'

"""

class MoryakApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper)
        return screen

    def on_start(self):
        for i in range(20):
            items = ThreeLineAvatarListItem(text='Вакансия ' + str(i), secondary_text="Описание ",tertiary_text='Дата',on_release=self.show_data)
            image = ImageLeftWidget(source='mini3.png')
            items.add_widget(image)
            self.root.ids.container.add_widget(items)

    def navigation_draw(self):
        print("Navigation")

    def show_data(self, obj):
        
        self.dialog = MDDialog(title='Вакансия ')
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        # do stuff after closing the dialog

MoryakApp().run()