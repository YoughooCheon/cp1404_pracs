from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App that dynamically creates Labels from a list of names."""

    def __init__(self, **kwargs):
        """Initialize the app with a list of names (the model)."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "David", "Eve"]

    def build(self):
        """Build the GUI and dynamically create Label widgets."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)
        return self.root


if __name__ == '__main__':
    DynamicLabelsApp().run()