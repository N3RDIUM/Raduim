import pyglet

class RadiumWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.tabs = []
        self.current_tab = 0

    def add_tab(self, tab):
        self.tabs.append(tab)

    def on_draw(self):
        self.clear()
        try:
            self.tabs[self.current_tab].draw()
        except IndexError:
            pass

    def on_key_press(self, symbol, modifiers):
        try:
            self.tabs[self.current_tab].on_key_press(symbol, modifiers)
        except IndexError:
            pass

    def on_key_release(self, symbol, modifiers):
        try:
            self.tabs[self.current_tab].on_key_release(symbol, modifiers)
        except IndexError:
            pass

    def on_mouse_press(self, x, y, button, modifiers):
        try:
            self.tabs[self.current_tab].on_mouse_press(x, y, button, modifiers)
        except IndexError:
            pass

    def on_mouse_release(self, x, y, button, modifiers):
        try:
            self.tabs[self.current_tab].on_mouse_release(x, y, button, modifiers)
        except IndexError:
            pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        try:
            self.tabs[self.current_tab].on_mouse_drag(x, y, dx, dy, buttons, modifiers)
        except IndexError:
            pass

    def on_mouse_motion(self, x, y, dx, dy):
        try:
            self.tabs[self.current_tab].on_mouse_motion(x, y, dx, dy)
        except IndexError:
            pass

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        try:
            self.tabs[self.current_tab].on_mouse_scroll(x, y, scroll_x, scroll_y)
        except IndexError:
            pass

    def on_resize(self, width, height):
        try:
            self.tabs[self.current_tab].on_resize(width, height)
        except IndexError:
            pass

if __name__ == "__main__":
    window = RadiumWindow(800, 600, "Radium")
    pyglet.app.run()
