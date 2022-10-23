from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.clock import Clock
import datetime

class RootWidget(Widget):
    state = StringProperty(str(datetime.date(2022, 12, 25) - datetime.date.today()))

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        Clock.schedule_interval(self.update_state, 2.5)

    def update_state(self, dt):
        self.state = str(datetime.date(2022, 12, 25) - datetime.date.today())

class HelloWorldApp(App):

    def build(self):
        return RootWidget()

kv = """
<RootWidget>:
    Label:
        
        text: "Christmas is: " + root.state + " away"
        size: root.size
        pos: root.pos
        color: (1., 1., 1., 1.)
    """

if __name__ == '__main__':
    Builder.load_string(kv)
    HelloWorldApp().run()