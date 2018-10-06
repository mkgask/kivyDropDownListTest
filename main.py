# -*- coding: utf-8 -*
import os
import kivy

from kivy.app import App
from kivy.factory import Factory
from kivy.properties import ObjectProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

# 日本語フォント表示対応
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

resource_add_path('{}\\{}'.format(os.environ['SYSTEMROOT'], 'Fonts'))
LabelBase.register(DEFAULT_FONT, 'MSGOTHIC.ttc')

class CustomDropDown(DropDown):
    pass

class MainRoot(BoxLayout):
    dropdown = ObjectProperty(None)
    
    def dropdown_open(self):
        print('self.dropdown: ' + str(self.dropdown))
        self.dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        self.dropdown.open()

class MainApp(App):

    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.title = 'Drop-Down List Test'

if __name__ == "__main__":
    MainApp().run()