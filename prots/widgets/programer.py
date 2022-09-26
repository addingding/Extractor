from ecosys import *

class aJsonWidget(aWidget,ABC):
    def __init__(self, ui, map):
        self.table = None
        self.btn_create:QPushButton = None
        self.btn_copy:QPushButton = None
        self.btn_edit:QPushButton = None
        self.btn_save:QPushButton = None
        self.btn_delete:QPushButton = None
        self.btn_delete_all:QPushButton = None

        super().__init__(ui, map)
        self.widget_activate()
        
    def widget_activate(self):
        self.btn_create.clicked.connect(self.create)
        self.btn_copy.clicked.connect(self.copy)
        self.btn_edit.clicked.connect(self.edit)
        self.btn_save.clicked.connect(self.save)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_delete_all.clicked.connect(self.delete_all)
    @abstractmethod
    def create(self):...
    @abstractmethod
    def copy(self):...
    @abstractmethod
    def edit(self):...
    @abstractmethod
    def save(self):...
    @abstractmethod
    def delete(self):...
    @abstractmethod
    def delete_all(self):...
    @abstractmethod
    def table_update(self):...
class aProgrameWidget(aJsonWidget):
    pass
class aOperationWidget(aJsonWidget):
    pass

class aStartWidget(aWidget,ABC):
    def __init__(self, ui, map):
        self.table = None
        self.btn_scan:QPushButton = None
        self.btn_start:QPushButton = None
        self.btn_view:QPushButton = None

        super().__init__(ui, map)
        # self.widget_activate()
        
    def widget_activate(self):
        # self.btn_scan.clicked.connect(self.scan)
        # self.btn_start.clicked.connect(self.start)
        # self.btn_view.clicked.connect(self.view)
        pass
    @abstractmethod
    def scan(self):...
    @abstractmethod
    def start(self):...
    @abstractmethod
    def view(self):...
    @abstractmethod
    def table_update(self):...