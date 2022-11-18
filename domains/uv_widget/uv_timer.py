from ecosys import *
from prots import *

DEFAULT_UV_TIME = 1800
DEFAULT_STOP_TIME = DEFAULT_UV_TIME

timer_map:dict = dict(
    head = "label_2",
    face = "timeEdit",

    start = "pushButton_7",
    pause = "pushButton_24",
    reset = "pushButton_6",
    stop = "pushButton_23",
)

class UvTimerWidget(aTimerWidget):
    def __init__(self,ui,map,e_work:Event =None,uv:aUV = None):
        super().__init__(ui,map)
        if e_work is None:
            e_work = Event()
        self.e_work = e_work
        self._uv:aUV = uv
        self.stop.clicked.connect(self.stop_clicked)
        self.reset.clicked.connect(self.reset_clicked)
        self.pause.clicked.connect(self.pause_clicked)
        self.start.clicked.connect(self.start_clicked)

        self._timer.timeout.connect(self.update_time)
        self.time_count:int = DEFAULT_STOP_TIME
        self.time_passed:int = 0
        self.time_total:int = DEFAULT_STOP_TIME

    @property
    def uv(self)->aUV:
        return self._uv
    @uv.setter
    def uv(self,value):
        self._uv = value
        
    def update_time(self):
        if self.time_count>0:
            self.time_count -=1
            self.time_passed +=1
        else:
            self.ring()
            return
        self.set_face_time(self.time_count)
        self._timer.start(1000)

    def read_face_time(self):
        _time = self.face.time()
        time_seconds = _time.hour()*3600+_time.minute()*60+_time.second()
        return time_seconds
    def set_face_time(self,time_counts:int):
        h = time_counts//3600
        m = time_counts//60
        s = time_counts%60
        _time = QTime(h,m,s)
        self.face.setTime(_time)
        return

    def ring(self):
        self.stop_clicked()
        logger.info("Time reached!")
        self.head.setText("UV Time Satified!!!")

    def start_clicked(self):
        if self.e_work.is_set():
            self.ui.popup(about=(lang('Alert'),lang('Busy for new job')))
            return
        self.e_work.set() 
        self.head.setText("UV Time")
        self.time_count = self.read_face_time()
        self.time_total = self.time_count
        self.time_passed = 0
        self.face.setReadOnly(True)
        self.start.setEnabled(False)
        self.reset.setEnabled(False)
        if not self.uv is None:
            self.uv.turn_on()
        self._timer.start(1000)
        pass
    def stop_clicked(self):
        self._timer.stop()
        if not self.uv is None:
            self.uv.turn_off()
        self.face.setReadOnly(False)
        self.start.setEnabled(True)
        self.reset.setEnabled(True)
        self.e_work.clear()
        pass
    def reset_clicked(self):
        self.time_count = DEFAULT_STOP_TIME
        self.set_face_time(self.time_count)
        self.head.setText("UV Time")
        pass
    def pause_clicked(self):
        self._timer.stop()
        self.start.setEnabled(True)
        pass

class JobTimer():
    def __init__(self):
        self._timer = QTimer()

    def __getattr__(self,attr):
        return getattr(self._timer,attr)
    def get_job(self,seconds:float,next_operation):
        self.wait_seconds = seconds
        self.nex_opertation = next_operation
        self._timer.timeout.connect(self.stop_operation)
        self.init_time = time.time()

    @property
    def __past_seconds(self):
        if hasattr(self,'start_time'):
            return time.time()-self.start_time
        else:
            return 0
    @property
    def __left_time(self):
        return  self.wait_seconds- self.__past_seconds
    def start(self):
        logger.info(f"wait {self.wait_seconds} seconds.")
        self._timer.start(int(self.wait_seconds*1000))
        self.start_time =  time.time()
    def pause(self):
        self._timer.stop()
        self.wait_seconds = self.__left_time
        # logger.info(f"time_left {self.wait_seconds}",)
    def restart(self):
        self.start()
    def stop_operation(self):
        if self.__left_time<=0:
            self._timer.stop()
            self.nex_opertation()

class Timers():
    def uv_widget(self,ui,timer_map,e_work=None,uv:aUV=None):
        return UvTimerWidget(ui,e_work,timer_map,uv)
    def job_timer(self):
        return JobTimer()

timers = Timers()


class TestTimer():
    def __init__(self):
        from domains.ui.uis import application, uis
        self.app = application
        self.main_win = uis.main_win()
        self.main_win.show()
    def test_timer(self):
        UvTimerWidget = timers.uv_widget(self.main_win,timer_map)
        sys.exit(self.app.exec_())
    def print_ok(self):
        print("I'm definitely OK.")
    def test_job_timer(self):
        UvTimerWidget = timers.job_timer()
        UvTimerWidget.get_job(5,self.print_ok)
        UvTimerWidget.start()
        time.sleep(2)
        UvTimerWidget.pause()
        print("time passed 2s, pause UvTimerWidget.")
        time.sleep(2)
        print("2 seconds later,continue.")
        UvTimerWidget.restart()
        sys.exit(self.app.exec_())
if __name__ == "__main__":
    # TestTimer().test_timer()
    TestTimer().test_job_timer()