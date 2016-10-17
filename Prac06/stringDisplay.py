from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class LoopStrings(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.strings = ['Jared', 'Bob', 'Fred', 'Henry', 'Lindsay', 'Joel', 'Adam', 'Lawrence']

    def build(self):
        self.title = "String Loop Display"
        self.root = Builder.load_file('stringDisplay.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.strings:
            self.root.ids.entriesBox.add_widget(Label(text=name, markup=True))

LoopStrings().run()
