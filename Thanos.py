import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.factory import Factory
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.animation import Animation
from kivy.properties import NumericProperty, ObjectProperty, StringProperty, AliasProperty

from kivy.uix.screenmanager import ScreenManager

#Main window layout for the first screen of the app
class Controller(BoxLayout):

    label_wid = ObjectProperty
    label_wid2 = ObjectProperty
    button_wid = ObjectProperty
    save_wid = StringProperty


#Popup dialog to handle any errors
    def warning_popup(self):
        popup = Popup(title='Save File',
        content= Label(text='File successfully saved'),
        size_hint=(None, None), size=(700, 700))
        popup.open()
    
     
class ThanosApp(App):
    def build(self):
        return Controller()

if __name__== '__main__':
    ThanosApp().run()