from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    output_km = StringProperty("0.0")

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle the calculation triggered by text input change"""
        value = self.get_validated_miles()
        self.output_km = str(value * MILES_TO_KM)

    def handle_increment(self, change):
        """Handle 'Up' or 'Down' button press"""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """Return the float version of the input, or 0.0 if invalid"""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0

MilesConverterApp().run()