import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class HelloWorldApp(toga.App):
    def startup(self):
        # Create a Box widget with a "Hello World" label and a button
        self.main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        label = toga.Label('Hello World!', style=Pack(padding=(0, 5)))
        button = toga.Button('Click Me', on_press=self.on_button_click)

        self.main_box.add(label)
        self.main_box.add(button)

        # Set the main window content
        self.main_window = toga.MainWindow(self.name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def on_button_click(self, widget):
        print('Button clicked!')

def main():
    app = HelloWorldApp('Hello World', 'org.beeware.helloworld')
    app.main_loop()

if __name__ == '__main__':
    main()
