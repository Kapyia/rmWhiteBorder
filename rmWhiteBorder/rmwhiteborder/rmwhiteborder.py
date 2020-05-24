from krita import *

class RmWhiteBorder(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        window.qwindow().setStyleSheet("""
            QToolBar {
                border: none;
            }
        """)
        
Krita.instance().addExtension(RmWhiteBorder(Krita.instance()))
