'''
Cycles of War - python version by Ewa & Markus
==============================================

Detail description may follow if applicable
'''

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget

from kivy.uix.screenmanager import ScreenManager, Screen, FallOutTransition, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.properties import ListProperty, StringProperty

from kivy.uix.image import Image
from fonts import fonts


class MenuThumbnail(Button):
    pass

class MenuButton(Button):
    button_font = StringProperty(fonts.FONTS['nakki'])
    pass

class MainMenu(BoxLayout):
    # menu_button_color = ListProperty([0.9, 0.9, 0.9, 0.1])
    title_font = StringProperty(fonts.FONTS['nakki'])
    pass

class MenuScreen(Screen):
    pass

class SettingsLabel(Label):
    settings_font = StringProperty(fonts.FONTS['nakki'])
    pass

class StretchToggle(ToggleButton):
    settings_font = StringProperty(fonts.FONTS['nakki'])
    pass

class SettingsToggle(ToggleButton):
    settings_font = StringProperty(fonts.FONTS['nakki'])
    pass

class SettingsMenu(BoxLayout):
    settings_font = StringProperty(fonts.FONTS['nakki'])
    pass

class SettingsScreen(Screen):
    pass

class CoWApp(App):
    Window.size = (1366, 768)
    Window.fullscreen = True

    def __init__(self):
        super(CoWApp, self).__init__()
        self.screen_manager = None

    def build(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.transition = FadeTransition()
        self.screen_manager.add_widget(MenuScreen(name='menu'))
        self.screen_manager.add_widget(SettingsScreen(name='settings'))

        return self.screen_manager

if __name__ == '__main__':
    Window.fullscreen = 'auto'
    CoWApp().run()

