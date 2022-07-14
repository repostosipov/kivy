from turtle import color
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import ThreeLineIconListItem, MDList
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget
from kivy.uix.scrollview import ScrollView

class MoryakApp(MDApp):
    def build(self):
        screen = Screen()
        scroll = ScrollView()
        list_view = MDList()
        scroll.add_widget(list_view)

        for i in range(20):
            image = ImageLeftWidget(source='mini3.png')
            items = ThreeLineIconListItem(text='Вакансия ' + str(i),
            secondary_text='Моряк Инфо',
            tertiary_text='Дата')
            items.add_widget(image)
            list_view.add_widget(items)

        screen.add_widget(scroll)  
        # label = MDLabel(text="Всем привет",halign='center',theme_text_color='Secondary',font_style='H2')
        # icon_label = MDIcon(icon='account',halign='center')
            
        return screen

 

if __name__=="__main__":
    MoryakApp().run()

    