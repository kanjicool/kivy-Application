from kivy.app import App
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.config import Config
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Color, Line

class MyButton(ToggleButton):
    def _do_press(self):
        if self.state == 'normal':
            ToggleButtonBehavior._do_press(self)
        


class PaintApp(App):
    def build(self):
        self.canvas_widget = CanvasWidget()
        self.canvas_widget.set_color(get_color_from_hex('#2980b9'))
        return self.canvas_widget

class CanvasWidget(Widget):
    def set_color(self, new_color):
        self.last_color = new_color
        self.canvas.add(Color(*new_color))


if __name__ == "__main__":
    from kivy.core.window import Window
    Config.set('graphics', 'width', '960')
    Config.set('graphics', 'height', '540')
    Window.clearcolor = get_color_from_hex('#ffffff')

    PaintApp().run()
