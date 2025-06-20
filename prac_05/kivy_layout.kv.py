"""
CP1404/CP5632 Practical
Kivy_layout

function main
    create kivydemo instance
    run the app

class kivydemo (inherits from app)
    property: status_text ← "hello. click the buttons :)"

    function __init__
        call superclass initializer
        set counter ← 0
        set names ← ["lindsay", "osmond", "paul"]

    function build
        set app title to "hello world!"
        load interface from 'kivy_layout.kv'
        for each name in names:
            create button with text = name
            bind button press to function handle_name_button
            add button to names_box in layout
        return root widget

    function handle_name_button(instance)
        print "hello" and instance.text

    function handle_press(amount)
        add amount to counter
        update status_text to "the count is: {counter}"
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button

def main():
    """Entry point of the program: runs the KivyDemo app."""
    KivyDemo().run()

class KivyDemo(App):
    """Kivy program to demo some basic interactive functionality."""
    status_text = StringProperty("Hello. Click the buttons :)")

    def __init__(self, **kwargs):
        """Construct main Kivy app."""
        super().__init__(**kwargs)
        self.counter = 0
        self.names = ["Lindsay", "Osmond", "Paul"]

    def build(self):
        """Construct the dynamic widgets."""
        self.title = "Hello world!"
        self.root = Builder.load_file('kivy_layout.kv')
        for name in self.names:
            button = Button(text=name)
            button.bind(on_press=self.handle_name_button)
            self.root.ids.names_box.add_widget(button)
        return self.root

    def handle_name_button(self, instance):
        """Handle presses on the name button to greet people."""
        print("Hello", instance.text)

    def handle_press(self, amount):
        """Handle presses on the up/down buttons to change counter."""
        self.counter += amount
        self.status_text = f"The count is: {self.counter}"


if __name__ == "__main__":
    main()
