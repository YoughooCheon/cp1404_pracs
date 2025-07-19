"""
constant miles_to_km = 1.60934

class milesconverterapp extends app:

    output_km is a string property, default "0.0"

    function build():
        set title to "convert miles to kilometres"
        load kv file 'convert_miles_km.kv' into self.root
        return self.root

    function handle_calculate():
        get value from get_validated_miles()
        set output_km to value * miles_to_km as string

    function handle_increment(change):
        get value from get_validated_miles() and add change
        set self.root.ids.input_miles.text to value as string
        call handle_calculate()

    function get_validated_miles():
        try to return float from self.root.ids.input_miles.text
        if error, return 0.0

run milesconverterapp
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """Kivy app to convert miles to kilometers."""

    output_km = StringProperty("0.0")

    def build(self):
        """Build the UI from KV file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Convert miles to km and update output."""
        value = self.get_validated_miles()
        self.output_km = str(value * MILES_TO_KM)

    def handle_increment(self, change):
        """Adjust miles input by change amount."""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """Return valid float from input or 0.0."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0

MilesConverterApp().run()
