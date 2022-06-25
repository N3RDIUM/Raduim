from curses import KEY_ENTER
import pyglet
from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import QOpenGLWidget as OpenGLWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebChannel import QWebChannel
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtGui import *
from pyglet.gl import *

class PygletPage(OpenGLWidget):
    def __init__(self, width, height, parent=None):
        super().__init__(parent)
        self.setMinimumSize(width, height)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self._pyglet_update)
        self.timer.setInterval(0)
        self.timer.start()

    def _pyglet_update(self):
        # Tick the pyglet clock, so scheduled events can work.
        pyglet.clock.tick()  
        
        # Force widget to update, otherwise paintGL will not be called.
        self.update()  # self.updateGL() for pyqt5

    def paintGL(self):
        """Pyglet equivalent of on_draw event for window"""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        self.batch.draw()

    def initializeGL(self):
        """Call anything that needs a context to be created."""
        self.batch = pyglet.graphics.Batch()
        size = self.size()
        w, h = size.width(), size.height()
        
        self.projection = pyglet.window.Projection2D()
        self.projection.set(w, h, w, h)


class HTMLPage(QWidget):
        def __init__(self, html):
            super().__init__()

            self.html = None

            class View(QWebEngineView):
                def __init__(self, parent=None):
                    super().__init__(parent)
                    
                @QtCore.pyqtSlot(str)
                def run(self, what):
                    exec(what)
                
            self.view = View()
            vbox = QVBoxLayout(self)
            self.view.setHtml(html)

            vbox.addWidget(self.view)

            self.view.loadFinished.connect(self._loadFinished)
            self.webchannel = QWebChannel(self.view)
            self.view.setHtml(html)

            self.view.page().setWebChannel(self.webchannel)
            self.webchannel.registerObject('Radium', self.view)

            self.setLayout(vbox)
            self.show()

        def _callable(self, data):
            self.html = data

        def _loadFinished(self, result):
            self.view.page().toHtml(self._callable)

        def run_js(self, code):
            self.view.page().runJavaScript(code)

class Terminal(QTextEdit):
    def __init__(self, text="", defaultInput=">"):
        super().__init__()
        self.text = text + "\n" + defaultInput + " "
        self.input = defaultInput
        self.quickedit = True
        self.inputs = []

        self.append(self.text)

    def setInput(self, input):
        self.input = "\n" + input  + " "

    def _print(self, text):
        self.append(text)

    def _acceptControl(self):
        self._print(self.input + " ")

    def _acceptCommand(self):
        text = self.textCursor().block().text()
        text = text.replace(self.input + " ", "")
        self.inputs.append(text)
        try:
            self.quickedit = False
            self.callback(text)
            self.quickedit = True
        except NameError:
            pass
        self._acceptControl()

    def keyPressEvent(self, event):
        if self.quickedit:
            if event.key() in (16777220, 43):
                self._acceptCommand()
            else:
                if event.key() == 16777235:
                    pass
                elif event.key() == 16777237:
                    pass
                else:
                    super().keyPressEvent(event)
