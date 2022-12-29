# from PySide6 import QtWidgets, QtCore, QtGui
# from PySide6.QtCore import *  # type: ignore
# from PySide6.QtGui import *  # type: ignore
# from PySide6.QtWidgets import *  # type: ignore

from PySide2 import QtCore, QtGui, QtWidgets
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


from abc import ABC, abstractmethod
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
    def resume(self):
        self.e_safe.set()
    def dismiss(self):
        self.stop()

class Performer(QThread):
    """
    # main
    performer = Performer(task,*args,**kws)
    performer.signal_end.connect(self.work_end)
    performer.start()
    def work_end(self,ins:int):
        print(f'get_int{ins}')
        self.open = 1
    """
    signal_end = Signal(int)
    signal_updated = Signal(int)
    signal_pause = Signal(int)
    def __init__(self,task,e_stop,*argv,**kwargv):
        super().__init__()
        self.task = task
        self.argv = argv
        self.kwargv = kwargv
        self.e_stop:Event = e_stop #terminate

    def run(self):
        self.task(self.e_stop,self.signal_updated,*self.argv,**self.kwargv)
        self.signal_end.emit(0)

    def stop(self):
        ...
    def pause(self):
        ...
    def resume(self):
        ...
    def dismiss(self):
        ...

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
    clicked = Signal()
    def closeEvent(self,event):
        event.ignore()

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button()==Qt.LeftButton:
            self.clicked.emit()
    def on_clicked(self,event=None):
        print("mouse pressed")
        
class MyQProgressDialog(QProgressDialog):
    def closeEvent(self,event):
        if self.value()>=98:
            event.accept()
        else:
            event.ignore()
        
    def wait_to_exit(self,event:Event=Event(),timeout=0.01):
        # for val in range(71):
        #     self.setValue(val)
        #     # QCoreApplication.processEvents()
        #     if self.wasCanceled():
        #         break
        #     event.wait(0.01)
        #     if event.is_set():
        #         break
        # event.wait(timeout)
        # for i in range(71,101):
        #     self.setValue(i)
        #     time.sleep(0.01)
        # self.setValue(100)

        event.wait(timeout)
        self.cancel()
