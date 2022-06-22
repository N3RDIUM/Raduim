import pyglet

class _typeBase:
    def __init__(self, window, _html_file):
        self.window = window

        self.html_file = open(_html_file, 'r').read()
        self.html_file = pyglet.resource.html(self.html_file)
        self.widget = pyglet.text.Label()
        self.widget.text = self.html_file

    def on_draw(self):
        self.html_file.draw()
