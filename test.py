from kivymd.app import MDApp
from kivymd.uix.list import ImageLeftWidget
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.uix.list import ThreeLineAvatarListItem
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.size = (500,800)

list_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
<MenuScreen>:
    name: 'menu'
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
                                on_action_button: root.manager.current = 'profile'
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
                                on_press: root.manager.current = 'upload'
                                IconLeftWidget:
                                    icon: 'pump'
                                    
                            OneLineIconListItem:
                                text: 'Личный кабинет'
                                on_press: root.manager.current = 'profile'
                                IconLeftWidget:
                                    icon: 'account'
                                    
<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Личный кабинет'
        text_size: self.size
        halign: 'center'
        valign: 'top'
    MDSlider:
        min: 0
        max: 100
        value: 40
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
        
<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'Справочник компаний'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Назад'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
  


"""

class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))

class MoryakApp(MDApp):

    def build(self):
        self.title = 'Моряк Инфо'
        self.icon = 'mini3.png'
        screen = Builder.load_string(list_helper)
        return screen
    # def on_start(self):
    #     for i in range(20):
    #         items = ThreeLineAvatarListItem(text='Вакансия ' + str(i), secondary_text="Описание ",tertiary_text='Дата')
    #         image = ImageLeftWidget(source='mini3.png')
    #         items.add_widget(image)
    #         self.root.ids.container.add_widget(items)

    def navigation_draw(self):
        print(" Жопа")
    
  
if __name__ == '__main__':
    MoryakApp().run()