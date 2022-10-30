from ecosys import *

from app.stage import application


from app.board import logo_file,opening_gif,defaults

from domains.ui.__styles import *
from domains.ui.translate_ui import *
from domains.ui.designer.main import Ui_MainWindow as MainWin
from domains.ui.designer.open import Ui_MainWindow as Opening
from domains.ui.designer.info import Ui_MainWindow as info_win

class WithPop:
    
    def popup(self,*args,about:tuple=None,question:tuple=None,dialog:tuple=None,input:tuple=None,pb_dialog:tuple=None):
        if len(args)>0:
            a_ = args[0]
            about = a_.get("about")
            question = a_.get("question")
            dialog = a_.get("dialog")
            input = a_.get("input")
            
        if about is not None:
            t_ = 30 if len(about)==2 else int(about[2])
            ret = QMessageBox.about(self,about[0],about[1])
            self.pop_ret = ret
            return ret
        if question is not None:
            t_ = 10 if len(question)==2 else int(question[2])
            reply = QMessageBox.question(self,question[0],question[1])            
            
            ret = True if reply == QMessageBox.Yes else False
            self.pop_ret = ret
            return ret

        if pb_dialog is not None:
            _dialog = MyQProgressDialog(lang("progress"),lang("cancel"),0,100,None) #XXX
            _dialog.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
            _dialog.setFocusPolicy(Qt.ClickFocus)
            _dialog.setWindowModality(Qt.WindowModal)
            _dialog.setStyleSheet(message_style+button_style)
            _dialog.setCancelButton(None)
            _dialog.setLabel(None)
            _dialog.setWindowTitle("waiting...")
            _dialog.show()
            return _dialog

        if dialog is not None:
            _dialog = MyQInputDialog(None) #XXX
            _dialog.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
            _dialog.setFocusPolicy(Qt.ClickFocus)
            _dialog.setTextEchoMode(QLineEdit.Normal)
            _dialog.setStyleSheet(message_style+button_style)
            _dialog.setWindowTitle(dialog[0])
            _dialog.setLabelText(dialog[1])
            _dialog.setInputMode(QInputDialog.TextInput)

            if len(dialog)==3:
                _dialog.setTextValue(dialog[2])
            
            ok = _dialog.exec_()
            if ok:
                text_ = _dialog.textValue()
                if text_:
                    self.pop_ret = text_
                    return text_
                else:
                    self.pop_ret = None
                    return None

"""                     
    def popup_no_frame(self,*args,about:tuple=None,question:tuple=None,dialog:tuple=None,input:tuple=None):
        if len(args)>0:
            a_ = args[0]
            about = a_.get("about")
            question = a_.get("question")
            dialog = a_.get("dialog")
            input = a_.get("input")
        message = QMessageBox(self.tabWidget)
        message.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
        message.setAttribute(Qt.WA_TranslucentBackground)
        message.setStyleSheet(message_style+button_style)

        if about is not None:
            t_ = 30 if len(about)==2 else int(about[2])

            message.setWindowTitle(about[0])
            message.setText(about[1])
            message.setIcon(QMessageBox.Icon.Information)
            message.setStandardButtons(QMessageBox.Ok)
            message.button(QMessageBox.Ok).animateClick(t_*000)
            message.exec_()
            ret = None
            self.pop_ret = ret
            return ret
        if question is not None:
            # frame = QtWidgets.QFrame(message)
            # frame.setFrameRect(message.rect())
            # frame.setStyleSheet(round_frame_style)
            t_ = 10 if len(question)==2 else int(question[2])
            
            
            message.setWindowTitle(question[0])
            message.setText(question[1])
            message.setIcon(QMessageBox.Icon.Question)
            message.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            message.button(QMessageBox.No).animateClick(t_*1000)

            # message.open()
            # message.show()
            # frame.resize(message.width(),message.height())

            reply = message.exec_()

            ret = True if reply == QMessageBox.Yes else False
            self.pop_ret = ret
            return ret

        if dialog is not None:
            _dialog = MyQInputDialog(None)
            _dialog.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
            _dialog.setStyleSheet(message_style+button_style)
            _dialog.setWindowTitle(dialog[0])
            _dialog.setInputMode(QInputDialog.TextInput)
            _dialog.setLabelText(dialog[1])
            _dialog.setWindowModality(Qt.WindowModal)
            if len(dialog)==3:
                _dialog.setTextValue(dialog[2])
                
            ok = _dialog.exec_()
            text_ = _dialog.textValue()

            if ok and text_:
                self.pop_ret = text_
                return text_
            else:
                self.pop_ret = None
                return None
 """

class PopThread(QThread):
    _signal = Signal(dict) 
    def __init__(self,_contents:dict):
        super().__init__()
        self._contents = _contents
    def run(self):
        self._signal.emit(self._contents)



class SplashScreen(QSplashScreen):
    def __init__(self):
        super().__init__(QPixmap(logo_file))  #启动程序的图片

    #效果 fade =1 淡入   fade= 2  淡出，  t sleep 时间 毫秒
    def effect(self):
        self.setWindowOpacity(0)
        t = 0
        while t <= 50:
            newOpacity = self.windowOpacity() + 0.02     #设置淡入
            if newOpacity > 1:
                break
            self.setWindowOpacity(newOpacity)
            self.show()
            t -= 1
            time.sleep(0.01)

        time.sleep(1)
        t = 0
        while t <= 50:
            newOpacity = self.windowOpacity() - 0.02         #设置淡出
            if newOpacity < 0:
                break
            self.setWindowOpacity(newOpacity)
            t += 1
            time.sleep(0.02)
        self.close()
        
      
class MainInterface(QMainWindow,MainWin,WithPop):
    clicked = Signal(int)
    collector_end = Signal(int)
    collector_updated = Signal(int)
    program_updated = Signal(int)

    def __init__(self) -> None:
        super().__init__()
        MainWin.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)
        self.languages_retranslate()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(main_win_style+frame_widget_style+scroll_vertical + button_style+main_tab_widget_style)
        # self.setAttribute(Qt.WA_AcceptTouchEvents, True)
        self.set_styles()

        self.tabWidget.setCurrentIndex(0)

        self.activate_management_buttons()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.stackedWidget.setCurrentIndex(4)
        self.pushButton_30.hide() #traditional
        self.pushButton.hide()
        self.pushButton_2.hide() #cw
        self.pushButton_3.hide() #ccw
        self.pushButton_15.hide() #copy
        self.pushButton_35.hide() #copy
        self.pushButton_22.hide() #program delete all
        self.pushButton_37.hide() #process delete all
        # self.pushButton_10.hide() #program io
        self.pushButton_28.clicked.connect(lambda x: self.tabWidget.setCurrentIndex(1))
        self.pushButton.clicked.connect(self.close_window)
        

    def close_window(self):
        if self.popup(question=(lang("Alert"),lang("Are you sure?"))):
            self.close()

    def languages_retranslate(self):
        LANGUAGES[0] = defaults.get("language")
        retranslate_ui(self)

    def set_styles(self):
        # self.progressBar.setStyleSheet(u"background-color: rgba(255, 255, 255,0);\n"
        #     "min-height: 10px;\n"
        #     "max-height: 10px;\n"
        #     "border:0.5px solid lightgray;\n"
        #     "border-radius:5px;")
        self.dateTimeEdit.setStyleSheet(u"background-color: rgba(255,255,255,0);")
        self.timeEdit.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.toolBox.setStyleSheet(tool_box_style)
        

    def update_time(self):
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.dateTimeEdit_2.setDateTime(QDateTime.currentDateTime())
        self.timer.start(1000)

    def activate_management_buttons(self):
        def show_page(n):
            self.stackedWidget.setCurrentIndex(n)
        def show_page_time():
            show_page(1)
        def show_page_export():
            show_page(2)
        def show_page_upgrade():
            show_page(3)
        def show_page_language():
            show_page(4)
        def show_page_calibration():
            show_page(5)
        self.pushButton_8.clicked.connect(show_page_time)
        self.pushButton_10.clicked.connect(show_page_export)
        self.pushButton_11.clicked.connect(show_page_upgrade)
        self.pushButton_12.clicked.connect(show_page_language)
        self.pushButton_41.clicked.connect(show_page_calibration)
        self.pushButton_42.clicked.connect(show_page_calibration)

class Infowin(QMainWindow,info_win,WithPop):
    def __init__(self) -> None:
        super().__init__()
        info_win.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet(info_win_style)

        self.label:QLabel = self.label
        self.infos = []
    def show_info(self,info:str):
        self.infos.append(lang(info))
        to_show = self.infos[-5:] if len(self.infos)>5 else self.infos
        self.label.setText("\n".join(to_show))

class Open(QMainWindow,Opening):
    def __init__(self) -> None:
        super().__init__()
        Opening.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

    def playmovie(self,next_action=None):
        self.movie = QMovie(opening_gif)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setScaledSize(QtCore.QSize(1280,720))
        self.movie.setBackgroundColor(QColor("blue"))
        self.label.setMovie(self.movie)
        self.movie.setSpeed(80)
        self.movie.jumpToFrame(0)
        self.movie.finished.connect(self.close)
        self.i = 0
        def _finished():
            self.i += 1
            if self.i == self.movie.frameCount():
                self.movie.stop()
                self.close()
                del self.movie
                if next_action:
                    next_action()
        self.movie.frameChanged.connect(_finished)
        self.movie.start()
        pass    

class Uis:
    windows = {}
    def __init__(self):
        pass

    def splash_win(self):
        return SplashScreen()
    def info_win(self):
        return Infowin()
    def flash_win(self):
        if os.path.exists(opening_gif):
            return Open()
        else:
            return
    def main_win(self):
        return MainInterface()
    def review_win(self):
        ...

uis = Uis()

def main():
    main_win = uis.main_win()
    main_win.show()
    # splash = uis.splash_win()
    
    # opening = uis.flash_win()
    # opening.show()
    # opening.playmovie(main_win.show)

    # splash.effect()
    # main_win.close()
    pb = main_win.popup(pb_dialog=("title","txt"))
    pb.wait_to_exit(timeout=5)

    sys.exit(application.exec_())

if __name__ == "__main__":
    main()

