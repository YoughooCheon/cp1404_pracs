"""
class squarenumberapp inherits app:

    function build():
        set the window size to 300x150
        set the app title to "Square Number"
        load ui layout from 'squaring.kv'
        return the root widget

    function handle_calculate(value):
        try to:
            convert the input value to float
            calculate the square of the value
            display the result in the output label
        if conversion fails:
            display "Invalid input" in the output label

if this file is run as the main program:
    run the squarenumberapp
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class SquareNumberApp(App):
    """Kivy app to square a number."""

    def build(self):
        """Build the UI from KV file."""
        Window.size = (300, 150)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """Calculate square of input value and display result."""
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"

if __name__ == '__main__':
    SquareNumberApp().run()
