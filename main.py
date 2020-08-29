import random

from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.widget import Widget
from kivy.uix.button import Button

# RGBA = Red,Green,Blue, Opacity
Window.clearcolor = (1, 1, 1, 1)


class PaintWindow(Widget):
    def on_touch_down(self, touch):
        colorR = random.randint(0, 255)
        colorG = random.randint(0, 255)
        colorB = random.randint(0, 255)
        self.canvas.add(Color(rgb=(colorR / 255.0, colorG / 255.0, colorB / 255.0)))
        d = 30
        self.canvas.add(Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d)))
        touch.ud['line'] = Line(points=(touch.x, touch.y))
        self.canvas.add(touch.ud['line'])

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


# Root Window = Paint Window + Button
class PaintApp(App):
    def build(self):
        rootWindow = Widget()
        self.painter = PaintWindow()
        clearnBtn = Button(text='Clear')
        clearnBtn.bind(on_release=self.clear_canvas)
        rootWindow.add_widget(self.painter)
        rootWindow.add_widget(clearnBtn)

        return rootWindow

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


PaintApp().run()

# 1) Import Line Graphics
# 2) Create a Touch dictionary -> Store the initial touch point in it
# 3) When the moose is dragged to extend the line store the next points inside dictionary
# 4) Store it inside the canvas
# 5) Random colours