from prots import *


class LockWidget(QWidget):
    def __init__(self,ui,key:str,locked_buttons:List[str],locker:str):
        super().__init__()
        self.ui = ui
        self.key=key
        self.locked_buttons = locked_buttons

        self.locker:QPushButton = getattr(self.ui,locker)
        self.locker.setText(lang("unlock"))
        self.locker.clicked.connect(self.locker_pressed)

    def locker_pressed(self):
        lock = (self.locker.text()==lang("lock"))
        if lock:
            self.lock_pages()
            self.lock_buttons()
        else:
            self.unlock_buttons()

    def lock_buttons(self,lock:bool=True):
        for button in self.locked_buttons:
            btn:QPushButton = getattr(self.ui,button)
            btn.setEnabled(not lock)
        self.locker.setText(lang("unlock" if lock else "lock"))

    def lock_pages(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def unlock_buttons(self):
        text = self.ui.popup(dialog=(lang("Input"),lang("Input_unlock_key")))
        
        if text not in [None,""] and text == self.key:
            self.lock_buttons(False)
        else:
            self.ui.popup(about=(lang("Alert"),lang("No_Entry")))