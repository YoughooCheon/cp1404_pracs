"""
class boxlayoutdemo inherits app:

    function build():
        load ui from 'box_layout.kv'
        set root widget to loaded ui
        return root

    function handle_greet():
        get text from input_name field
        set output_label text to "hello <name>"

    function handle_clear():
        clear text in input_name field
        clear text in output_label

if __name__ == '__main__':
    run boxlayoutdemo app
"""
from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    """Kivy app that greets the user based on input."""

    def build(self):
        """Load the UI from the KV file and return it."""
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Display a greeting using the input name."""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        """Clear both input and output fields."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''

if __name__ == '__main__':
    BoxLayoutDemo().run()
