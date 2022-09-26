from ecosys import *

class aTimer():
    def __init__(self):
        self._timer = QTimer()

        self.head:QLabel = None
        self.face:QTimeEdit = None
        self.bar :QProgressBar = None

        self.start:QPushButton = None
        self.pause:QPushButton = None
        self.reset:QPushButton = None
        self.stop:QPushButton  = None

class aTimerWidget(aTimer,aWidget,QWidget):
    def __init__(self,ui,map):
        QWidget.__init__(self)
        super().__init__()
        aWidget.__init__(self,ui,map)