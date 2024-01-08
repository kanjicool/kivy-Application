from kivy.app import App
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

class PaintApp(App):
    def build(self):
        self.canvas_widget = CanvasWidget()
        return self.canvas_widget

class CanvasWidget(Widget):
    pass


if __name__ == "__main__":
    from kivy.core.window import Window
    Window.clearcolor = get_color_from_hex("#ffffff")

    PaintApp().run()