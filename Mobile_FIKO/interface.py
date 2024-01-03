import sys
import os
import importlib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.clock import Clock

sys.path.append(os.path.abspath('../'))

class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.fatigue_percentage = 0  # Initialize the attribute

    def build(self):
        # Set the window background color to white
        Window.clearcolor = (1, 1, 1, 1)

        # Create a BoxLayout as the root widget
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Add your logo image (replace 'path_to_logo.png' with the actual path)
        logo = Image(source='logo.png', size_hint=(.5, .5), pos=(200, 220))
        layout.add_widget(logo)

        # Define the bouncing animation
        bounce = Animation(pos=(200, 320), duration=1) + Animation(pos=(200, 220), duration=1)

        # Apply the bouncing animation to the logo indefinitely
        bounce.repeat = True
        bounce.start(logo)
        # Create a button that triggers the popup
        
        
             
             
        self.fatigue_label = Label(
            text="Fatigue Percentage: ",
            font_size='20sp',  # Set the font size
            color=(0, 0, 1, 1),  # Blue color (R, G, B, A)
            pos=(1, 1),
        )

        layout.add_widget(self.fatigue_label)
        Clock.schedule_interval(self.update_fatigue_label, 20)

       
          
        return layout
    
    def show_popup_medium(self, instance):
        # Load the sound file
        sound = SoundLoader.load('pop.mp3')  

        if sound:
            sound.play()  
        # Create a Popup with some content
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='We recommand you to rest in a gas station'))
        content.add_widget(Button(text='Close Popup', on_press=self.dismiss_popup))

        popup = Popup(title='Warning !', content=content, size_hint=(None, None), size=(400, 400))
        popup.open()
        Clock.schedule_once(lambda dt: popup.dismiss(),5)
        
    def show_popup_Hard(self, instance):
        # Load the sound file
        sound = SoundLoader.load('pop.mp3')  

        if sound:
            sound.play()  
        # Create a Popup with some content
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='YOU ARE SUPER TIRED ! WE INFORMED YOUR MENTOR'))
        content.add_widget(Button(text='Close Popup', on_press=self.dismiss_popup))

        popup = Popup(title='Warning !', content=content, size_hint=(None, None), size=(400, 400))
        popup.open()
        Clock.schedule_once(lambda dt: popup.dismiss(),5)

    def dismiss_popup(self, instance):
        # Dismiss the popup
        instance.parent.parent.parent.parent.dismiss()
        
    def update_fatigue_label(self, dt):
        import fatigue
        importlib.reload(fatigue)
        self.fatigue_percentage = round(fatigue.cluster_1_percentage, 2)
        
        self.fatigue_label.text = f"Fatigue Percentage: {self.fatigue_percentage}%"
        
        if (self.fatigue_percentage>50 and self.fatigue_percentage<75):
            self.show_popup_medium(None)
        if (self.fatigue_percentage>75):
            self.show_popup_Hard(None)
        

        

if __name__ == '__main__':

    app = MainApp()
    app.run()
