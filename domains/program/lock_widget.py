from prots import *

class LockWidget(QWidget):
    def __init__(self,ui,key:str,locked_buttons:List[str],button_lock:str):
        super().__init__()
        self.ui = ui
        self.key=key
        self.locked_buttons = locked_buttons
        self.button_lock = button_lock
        self.set_unlock_button()

    def lock_buttons(self):
        for button in self.locked_buttons:
            self.lock_button(button,True)

    def set_unlock_button(self):
        btn:QPushButton = getattr(self.ui,self.button_lock)
        btn.clicked.connect(self.to_unlock_buttons)

    def unlock_buttons(self):
        for button in self.locked_buttons:
            self.lock_button(button,False)
    def lock_button(self,button:str,lock:bool=True):
        btn:QPushButton = getattr(self.ui,button)
        btn.setEnabled(not lock)

    def to_unlock_buttons(self):
        text = self.ui.popup(dialog=(lang("Input"),lang("Input unlock key")))
        if text not in [None,""] and text == self.key:
            self.unlock_buttons()
        else:
            self.ui.popup(about=(lang("Alert"),lang("No Entry")))