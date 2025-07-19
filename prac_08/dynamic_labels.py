"""
class dynamiclabelsapp extends app:

    function __init__():
        call super().__init__()
        set self.names to ["alice", "bob", "charlie", "david", "eve"]

    function build():
        set title to "dynamic labels"
        load kv file "dynamic_labels.kv" into self.root
        for each name in self.names:
            create label with text = name
            add label to self.root.ids.main
        return self.root

if __name__ == '__main__':
    create dynamiclabelsapp instance
    run the app
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Kivy app that creates labels dynamically from a list."""

    def __init__(self, **kwargs):
        """Initialize with a list of names."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "David", "Eve"]

    def build(self):
        """Load UI and add labels for each name."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)
        return self.root

if __name__ == '__main__':
    DynamicLabelsApp().run()
