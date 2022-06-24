import pyglet, sys
from PyQt6 import QtCore
from PyQt6.QtOpenGLWidgets import QOpenGLWidget as OpenGLWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebChannel import QWebChannel
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

class HTMLPage(QWebEngineView):
        def __init__(self, html):
            self.html = None
            self.app = QApplication(sys.argv)
            QWebEngineView.__init__(self)
            self.loadFinished.connect(self._loadFinished)
            self.webchannel = QWebChannel(self)
            self.setHtml(html)

            self.page().setWebChannel(self.webchannel)
            self.webchannel.registerObject('Radium', self)

            while self.html is None:
                self.app.processEvents(QtCore.QEventLoop.ExcludeUserInputEvents | QtCore.QEventLoop.ExcludeSocketNotifiers | QtCore.QEventLoop.WaitForMoreEvents)
            self.app.quit()

        def _callable(self, data):
            self.html = data

        def _loadFinished(self, result):
            self.page().toHtml(self._callable)
        
        @QtCore.pyqtSlot(str)
        def _callback(self, code):
            exec(code)

        def run_js(self, code):
            self.page().runJavaScript(code)
