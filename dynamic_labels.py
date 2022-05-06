from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """DynamicLabelsApp is a Kivy App to create Dynamic Labels"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app and create a list of names dictionary"""
        super().__init__(**kwargs)
        self.list_of_names = {"Bob Brown", "Cat Cyan", "Oren Ochre"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from dictionary entries and add them to the GUI."""
        for name in self.list_of_names:
            temp_button = Button(text=name)
            temp_button.bind(on_text=self.press_entry)
            self.root.ids.main_box.add_label(temp_button)

    def press_entry(self, instance):
        """Handle pressing entry labels"""
        name = instance.text
        self.status_text = "{}".format(name)

    def clear_all(self):
        """Clear all labels that are children of the "main_box" layout widget."""
        self.root.ids.main_box.clear_labels()


if __name__ == '__main__':
    DynamicLabelsApp().run()
