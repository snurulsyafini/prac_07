from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERT_MILES_TO_KM = 1.60934


class ConvertMilesToKmApp(App):
    """ ConvertMilesToKmApp is a Kivy App to convert Miles to Kilometres"""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file"""
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation (could be button press or other call)"""
        miles = self.convert_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        """Handle up or down button press, text input updates with new value, calculation function"""
        miles = self.convert_number(text) + change
        self.root.ids.input_number.text = str(miles)

    def update_result(self, miles):
        self.output_km = str(miles * CONVERT_MILES_TO_KM)

    @staticmethod
    def convert_number(text):
        """Convert text to float, if invalid input show 0.0"""
        try:
            return float(text)
        except ValueError:
            return 0.0


if __name__ == '__main__':
    ConvertMilesToKmApp().run()
