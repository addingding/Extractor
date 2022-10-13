from prots import *
from app.board import *

from domains.program.lock_widget import LockWidget

locked_buttons = [
    "pushButton_10",
    "pushButton_11",
    "pushButton_41",

]
button_lock = "pushButton_56"
class CustomWidget(QWidget):
    def __init__(self,ui) -> None:
        self.ui = ui
        self.btn_directory = getattr(self.ui,"pushButton_52")
        self.line_directory = getattr(self.ui,"lineEdit_8")
        self.line_directory.setStyleSheet(u"border: 1px solid gray;border-radius:5px;")
        self.btn_input = getattr(self.ui,"pushButton_9")
        self.btn_output = getattr(self.ui,"pushButton_51")

        self.btn_directory.clicked.connect(self.get_dir)

        self.btn_input.clicked.connect(self.import_files)
        self.btn_output.clicked.connect(self.export_files)

        self.lock_widget = LockWidget(ui,"205413",locked_buttons,button_lock)
        self.lock_widget.lock_buttons()

    def get_dir(self,a=None):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, lang("select_directory"), "/")
        self.line_directory.setText(directory)
        
    def import_files(self,a=None):
        if QMessageBox.question(None,lang("Alert"),lang("Sure to import files?"),QMessageBox.Yes|QMessageBox.No,QMessageBox.No)==QMessageBox.Yes:
            directory = self.line_directory.text()
            self.replace_files(directory,is_in=True)
            QMessageBox.about(None,lang("Attention"),lang("Import done"))
    def export_files(self,a=None):
        if QMessageBox.question(None,lang("Alert"),lang("Sure to export files?"),QMessageBox.Yes|QMessageBox.No,QMessageBox.No)==QMessageBox.Yes:
            directory = self.line_directory.text()
            self.replace_files(directory,is_in=False)
            QMessageBox.about(None,lang("Attention"),lang("Export done"))

    def replace_files(self,directory,is_in:bool=True):
        data_names = ["programs.json","operations.json"]
        local_files = {
            "programs.json":program_file,
            "operations.json":operation_file
        }

        def file(name):
            return os.path.join(directory,name)
        def exist(name):
            return os.path.exists(file(name))

        for name in data_names:
            if is_in:
                if exist(name):
                    shutil.copyfile(src=file(name),dst=local_files.get(name))
            else:
                shutil.copyfile(src=local_files.get(name),dst=file(name))

class UpgradeWidget(QWidget):
    def __init__(self,ui) -> None:
        self.ui = ui
        self.btn_directory = getattr(self.ui,"pushButton_54")
        self.line_directory = getattr(self.ui,"lineEdit_9")
        self.line_directory.setStyleSheet(u"border: 1px solid gray;border-radius:5px;")
        self.btn_replace_ui = getattr(self.ui,"pushButton_53")
        self.btn_upgrade = getattr(self.ui,"pushButton_32")

        self.btn_directory.clicked.connect(self.get_dir)
        self.btn_replace_ui.clicked.connect(self.replace_ui_files)
        self.btn_upgrade.clicked.connect(self.upgrade_open)

    def get_dir(self,a=None):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, lang("select_directory"), "/")
        self.line_directory.setText(directory)
        
    def replace_ui_files(self,a=None):
        ret = QMessageBox.question(None,lang("Alert"),lang("Sure to import files?"),QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if ret==QMessageBox.Yes:
            directory = self.line_directory.text()
            self.replace_files(directory,is_in=True,is_data=False)        
            QMessageBox.about(None,lang("Attention"),lang("Import done"))

    def replace_files(self,directory,is_in:bool=True,is_data:bool=True):
        option_names = ["favicon.ico","background.png","logo.png","open.gif"]
        local_files = {
            "favicon.ico":ico_file,
            "background.png":background_png,
            "logo.png":logo_file,
            "open.gif":opening_gif,
        }

        def file(name):
            return os.path.join(directory,name)
        def exist(name):
            return os.path.exists(file(name))

        for name in option_names:
            if exist(name):
                shutil.copyfile(src=file(name),dst=local_files.get(name))

    def upgrade_open(self):
        directory = self.line_directory.text()
        if sys.platform.startswith('win'):
            os.startfile(directory)
        else:
            os.system(f'xdg-open {directory}')
    