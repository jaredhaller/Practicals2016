from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class MeasurementConverter(App):

    def build(self):
        self.title = "Measurement Converter"
        self.root = Builder.load_file('converter.kv')
        Window.size = (400, 200)
        return self.root

    def handle_adjustment(self, value):
        self.root.ids.input_number.text = str(int(self.root.ids.input_number.text) + value)

    def handle_convert(self):
        try:
            self.root.ids.output_label.text = str(round(float(self.root.ids.input_number.text)/0.62137, 2))
        except ValueError:
            self.root.ids.output_label.text = '0'
        except TypeError:
            self.root.ids.output_label.text = '0'

MeasurementConverter().run()