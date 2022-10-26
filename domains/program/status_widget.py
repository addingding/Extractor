from ecosys import *
from prots import *

from app.board import info

grid_key_style = """
    QPushButton{background-color:rgba(230,230,230,70%);border:0.5px solid gray;border-radius:25;font:24px;}
    QPushButton:hover{background-color:rgba(240,240,240,80%);border:1px solid lightblue;font:36px bold;}
    QPushButton:pressed,QpushButton:checked{background-color:rgba(0,252,50,90%);border:3px solid white;font:40px bold;border-style:inset;border-radius:12px;}
  """

status_map ={
    "graph":"label",
    "table":"gridLayout_23",
    "temp_1":"label_31",
    "temp_2":"label_32",
    "time_label":"label_11",
    "time_bar":"progressBar_2",
    "lbl_op_name":"label_13",
    "lbl_step":"label_15",
    "lbl_disk":"label_16",
    "lbl_wait":"label_18",
    "lbl_stir":"label_20",
    "lbl_mag":"label_22",
    "lbl_volumn":"label_24",
    "lbl_speed":"label_25",
    "lbl_temperature":"label_28",
    "btn_p1":"pushButton_43",
    "btn_p2":"pushButton_44",
    "btn_p3":"pushButton_45",
    "btn_p4":"pushButton_46",
    "btn_p5":"pushButton_47",
    "btn_p6":"pushButton_48",
    "btn_p7":"pushButton_49",
    "btn_p8":"pushButton_50",
    "btn_task_start":"pushButton_57",
    "btn_task_pause":"pushButton_19",
    "btn_task_stop":"pushButton_18",
    "btn_task_return":"pushButton_20",
}

font_style ="""QLabel{font-size:28px;} """

class StatusWidget(QWidget,aWidget):
    disk_key_pressed = Signal(int)
    pause_signal = Signal(int)
    stop_signal = Signal(int)

    def __init__(self, ui, map,event_working,e_safe_perform, e_stop_perform):
        super().__init__()
        aWidget.__init__(self,ui, map)
        if event_working is None:
            event_working = Event()
        if e_safe_perform is None:
            e_safe_perform = Event()
        if e_stop_perform is None:
            e_stop_perform = Event()

        self.event_working=event_working
        self.e_safe = e_safe_perform
        self.e_stop = e_stop_perform
        self.btn_task_start:QPushButton = self.btn_task_start

        self.btn_task_pause.clicked.connect(self.btn_pause_clicked)
        self.btn_task_stop.clicked.connect(self.btn_stop_clicked)
        self.btn_task_return.clicked.connect(self.return_to_start)

        self.btn_task_start.setEnabled(False)
        self.btn_task_pause.setEnabled(False)
        self.btn_task_stop.setEnabled(False)

        disk_img = os.path.join(BASE_DIR,'app/settings/imgs/disk360.png')
        self.show_selected_image(disk_img)

        self.btn_p1.clicked.connect(lambda n: self.key_pressed(self.btn_p1.text()))
        self.btn_p2.clicked.connect(lambda n: self.key_pressed(self.btn_p2.text()))
        self.btn_p3.clicked.connect(lambda n: self.key_pressed(self.btn_p3.text()))
        self.btn_p4.clicked.connect(lambda n: self.key_pressed(self.btn_p4.text()))
        self.btn_p5.clicked.connect(lambda n: self.key_pressed(self.btn_p5.text()))
        self.btn_p6.clicked.connect(lambda n: self.key_pressed(self.btn_p6.text()))
        self.btn_p7.clicked.connect(lambda n: self.key_pressed(self.btn_p7.text()))
        self.btn_p8.clicked.connect(lambda n: self.key_pressed(self.btn_p8.text()))

        self.keys =(
            self.btn_p1,
            self.btn_p2,
            self.btn_p3,
            self.btn_p4,
            self.btn_p5,
            self.btn_p6,
            self.btn_p7,
            self.btn_p8,
            )
        self.set_keys_checkable(True)

        self.ui.tabWidget.setStyleSheet(font_style)

    def btn_pause_clicked(self):
        if self.btn_task_pause.text()==lang("pause"):
            self.btn_task_pause.setText(lang("go_on"))
        else:
            self.btn_task_pause.setText(lang("pause"))
        self.working_pause_set()
        
    def working_pause_set(self):
        if (info.get("door_at_spot")!= 0) and self.btn_task_pause.text == lang("pause"):
            self.e_safe.set()
        else:
            self.e_safe.clear()

    def btn_stop_clicked(self):
        if self.ui.popup(question=(lang("Alert"),lang("Eorror would happen.Are you sure?"))):
            self.e_stop.set()

    def return_to_start(self):
        self.ui.tabWidget.setCurrentIndex(1)

    def set_keys_checkable(self,enabled:bool):
        for key in self.keys:
            key.setCheckable(enabled)
            key.setStyleSheet(grid_key_style)
    def set_keys_enable(self,enabled:bool):
        for key in self.keys:
            key.setEnabled(enabled)

    def show_selected_image(self, filename):
        self.graph.setPixmap(QPixmap(filename))

    @Slot(str)
    def key_pressed(self,n:str):
        if self.event_working.is_set():
            self.ui.popup(about=(lang('Alert'),lang('Could not start while working')))
            return
        self.event_working.set()

        self.btn_p1.setChecked(False) #TODO not working
        self.btn_p1.setDown(False)

        self.set_keys_enable(False)
        
        n = int(n)
        self.disk_key_pressed.emit(n)

        # code for test
        # time.sleep(1)
        # self.disk_arrived_and_work_done(n)
    
    def disk_arrived(self,n:int):
        info.update({"disk":n})
        self.disk_look_update(n)

    def disk_look_update(self, n):
        self.refresh_disk_key_order(n)
        btn = getattr(self,f"btn_p{n}")
        btn.setChecked(False)

        self.btn_p1.setChecked(True)
        self.btn_p1.setDown(True)

    def disk_arrived_and_work_done(self,n:int):
        self.disk_arrived(n)
        self.set_keys_enable(True)
        self.event_working.clear()
        
    def refresh_disk_key_order(self,n:int):
        for i in range(8):
            key:QPushButton = self.keys[i]
            key.setText(str((n-1+i)%8+1))
        


    def get_device(self,machine:aMachine):
        self.machine = machine

    def update(self):
        self.lbl_op_name.setText(str(info.get("op_name"))),
        self.lbl_step.setText(str(info.get("step_idx"))),
        self.lbl_disk.setText(str(info.get("disk"))),
        self.lbl_wait.setText(str(info.get("sec_wait"))),
        self.lbl_stir.setText(str(info.get("sec_mix"))),
        self.lbl_mag.setText(str(info.get("sec_mag"))),
        self.lbl_volumn.setText(str(info.get("ul_volumn"))),
        self.lbl_speed.setText(str(info.get("speed_mix"))),
        self.lbl_temperature.setText(str(info.get("temperature"))),

        self.temp_1.setText(f'{info.get("disk_1_temperature")}/{info.get("disk_1_preset")} ℃')
        self.temp_2.setText(f'{info.get("disk_8_temperature")}/{info.get("disk_8_preset")} ℃')

        pg_time_past = int(time.time()- int(info.get("pg_start_time")))
        pg_time_left = int(info.get("pg_total_time")-pg_time_past)
        if pg_time_left<0:
            pg_time_left =0
        step_time_past = int(time.time()- int(info.get("step_start_time")))
        step_time_left = int(info.get("step_total_time")-step_time_past)
        if step_time_left<0:
            step_time_left =0
        
        _value = int(pg_time_past/int(info.get("pg_total_time"))*100)
        if _value>=100:
            _value =100
        if _value<0:
            _value =0
        self.time_bar.setValue(_value),
        self.time_label.setText(\
            f'{lang("step needs:")} {step_time_left}s,{lang("program needs:")} {pg_time_left}s'
            )

        self.disk_look_update(int(info.get("disk")))

    def check_signals(self,info):
        door_safe = info.get("door_at_spot")
        sheath_safe = info.get("sheath_at_spot")


class StatusWidgets():
    def status_widget(self,ui,event_working=None,e_safe_perform=None, e_stop_perform=None):
        return StatusWidget(ui,status_map,event_working,e_safe_perform, e_stop_perform)

status_widgets = StatusWidgets()

class TestStatusWidget():
    def __init__(self):
        from domains.ui.uis import application,uis
        self.app = application
        self.main_win = uis.main_win()
        self.main_win.show()
    def test_status_widget(self):
        pg = status_widgets.status_widget(self.main_win)
        pg.update()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    TestStatusWidget().test_status_widget()