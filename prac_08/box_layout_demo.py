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
    def build(self):
        """loads the UI from the kv file and returns it as the root widget"""
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """gets user input and displays a greeting message"""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        """clears the input field and the output label"""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''

if __name__ == '__main__':
    BoxLayoutDemo().run()
