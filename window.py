'''
Cycles of War - python version by Ewa & Markus
==============================================

Detail description may follow if applicable
'''

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ListProperty, StringProperty

from kivy.uix.image import Image
from fonts import fonts


class MainMenu(BoxLayout):
    # menu_button_color = ListProperty([0.9, 0.9, 0.9, 0.1])
    title_font = StringProperty(fonts.FONTS['nakki'])
    pass

class MenuButton(Button):
    button_font = StringProperty(fonts.FONTS['nakki'])
    pass

class CoWGame(Widget):
    pass


class CoWApp(App):
    Window.size = (1366, 768)
    Window.fullscreen = True
    def build(self):
        return CoWGame()


if __name__ == '__main__':
    Window.fullscreen = 'auto'
    CoWApp().run()

