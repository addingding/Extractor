# from PySide6 import QtWidgets, QtCore, QtGui
# from PySide6.QtCore import *  # type: ignore
# from PySide6.QtGui import *  # type: ignore
# from PySide6.QtWidgets import *  # type: ignore

from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore
# from PySide2.QtWebEngineWidgets import *

# from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtCore import *  # type: ignore
# from PyQt5.QtGui import *  # type: ignore
# from PyQt5.QtWidgets import *  # type: ignore
# from PyQt5.QtCore import pyqtSignal as Signal



# from pyqtgraph.graphicsItems import ViewBox
# import pyqtgraph as pg


def clear_layout(layout:QGridLayout):
    for i in range(layout.count()):
        layout.itemAt(i).widget().deleteLater()


from abc import ABC,abstractmethod
from threading import Event
class Worker(QThread):
    """
    # main
    self.worker = Worker(task,*args,**kws)
    self.worker.signal_end.connect(self.work_end)
    self.worker.start()
    def work_end(self,ins:int):
        print(f'get_int{ins}')
        self.open = 1
    """
    # signal_end = Signal(int)
    # signal_updated = Signal(int)
    def __init__(self,task,e_safe,e_stop,*argv,**kwargv):
        super().__init__()
        self.task = task
        self.argv = argv
        self.kwargv = kwargv
        self.e_stop:Event = e_stop #terminate
        self.e_safe:Event = e_safe #pause

    @abstractmethod
    def run(self):
        self.e_safe.set()
        while not self.e_stop.is_set():
            self.e_safe.wait()
            self.task(*self.argv,**self.kwargv)
            self.signal_updated.emit(1)
        self.signal_end.emit(0)
        
    def get_info(self,info):
        self.info = info
        
    def stop(self):
        self.e_stop.set()
    def pause(self):
        self.e_safe.clear()
    def work_on(self):
        self.e_safe.set()
    def dismiss(self):
        self.stop()
class Performer(QThread):
    """
    # main
    self.worker = Worker(task,*args,**kws)
    self.worker.signal_end.connect(self.work_end)
    self.worker.start()
    def work_end(self,ins:int):
        print(f'get_int{ins}')
        self.open = 1
    """
    # signal_end = Signal(int)
    # signal_updated = Signal(int)
    def __init__(self,task,e_safe,e_stop,*argv,**kwargv):
        super().__init__()
        self.task = task
        self.argv = argv
        self.kwargv = kwargv
        self.e_stop:Event = e_stop #terminate
        self.e_safe:Event = e_safe #pause

    def run(self):
        self.e_safe.set()
        self.task(self.e_safe,self.e_stop,self.signal_updated,*self.argv,**self.kwargv)
        self.signal_end.emit(0)

    def stop(self):
        self.e_stop.set()
    def pause(self):
        self.e_safe.clear()
    def work_on(self):
        self.e_safe.set()
    def dismiss(self):
        self.stop()

class ClickableLabel(QLabel):
    clicked = Signal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()

class aWidget():
    def __init__(self,ui,map):
        self.ui = ui
        for key,value in map.items():
            setattr(self,key,getattr(ui,value))
    def widget_activate(self):
        ...

class MyQInputDialog(QInputDialog):
    def closeEvent(self,event):
        event.ignore()