from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class MeasurementConverter(App):

    def build(self):
        self.title = "Measurement Converter"
        self.root = Builder.load_file('converter.kv')
        Window.size = (400, 200)
        return self.root

MeasurementConverter().run()