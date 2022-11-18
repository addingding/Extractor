from app.board import info
from ecosys import *
from prots import *

grid_key_style = """
    QPushButton{background-color:rgb(230,230,230);border:0.5px solid gray;border-radius:35;font:36px;}
    QPushButton:hover{background-color:rgba(240,240,240,80%);border:1px solid lightblue;font:42px bold;}
    QPushButton:pressed,QpushButton:checked{background-color:rgba(0,252,50,90%);border:3px solid white;font:40px bold;border-style:inset;border-radius:12px;}
  """
grid_key_style_ctx =""" 
    QPushButton{background-color:rgb(220,220,0);border:0.5px solid gray;border-radius:35;font:36px bold;}
    QPushButton:hover{background-color:rgba(240,240,240,80%);border:1px solid lightblue;font:36px bold;}
    QPushButton:pressed,QpushButton:checked{background-color:rgba(0,252,50,90%);border:3px solid white;font:36px bold;border-style:inset;border-radius:12px;}
 """

status_map ={
    "graph":"label",
    "table":"gridLayout_23",
    "temp_1":"label_31",
    "temp_2":"label_32",
    "time_label":"label_11",
    "time_bar":"progressBar_2",
}
op_buttons = {
    "btn_task_start":"pushButton_57",
    "btn_task_pause":"pushButton_19",
    "btn_task_stop":"pushButton_18",
    "btn_task_return":"pushButton_20",
}
step_info = {
    "lbl_op_name":"label_13",
    "lbl_step":"label_15",
    "lbl_disk":"label_16",
    "lbl_wait":"label_18",
    "lbl_stir":"label_20",
    "lbl_mag":"label_22",
    "lbl_volumn":"label_24",
    "lbl_speed":"label_25",
    "lbl_temperature":"label_28",}
disk_buttons = {
    "btn_p1":"pushButton_43",
    "btn_p2":"pushButton_44",
    "btn_p3":"pushButton_45",
    "btn_p4":"pushButton_46",
    "btn_p5":"pushButton_47",
    "btn_p6":"pushButton_48",
    "btn_p7":"pushButton_49",
    "btn_p8":"pushButton_50",
}

disk_labels = {
    "lbl_p1":"label_3",
    "lbl_p2":"label_10",
    "lbl_p3":"label_35",
    "lbl_p4":"label_36",
    "lbl_p5":"label_37",
    "lbl_p6":"label_38",
    "lbl_p7":"label_39",
    "lbl_p8":"label_40",
}

status_map.update(step_info)
status_map.update(op_buttons)
status_map.update(disk_buttons)
status_map.update(disk_labels)

font_style ="""QLabel{font-size:28px;} """

class StatusWidget(QWidget,aWidget):
    disk_key_pressed = Signal(int)
    pause_signal = Signal(int)
    stop_signal = Signal(int)

    def __init__(self, ui, map,e_work:Event, e_stop:Event):
        super().__init__()
        aWidget.__init__(self,ui, map)

        self.e_work=e_work
        self.e_stop = e_stop
        
        self.btn_task_start.setStyleSheet(u"font:36px bold black;")
        self.btn_task_pause.setStyleSheet(u"font:36px bold black;")
        self.btn_task_stop.setStyleSheet(u"font:36px bold black;")
        self.btn_task_return.setStyleSheet(u"font:36px bold black;")

        self.btn_task_pause.clicked.connect(self.btn_pause_clicked)
        self.btn_task_stop.clicked.connect(self.btn_stop_clicked)
        self.btn_task_return.clicked.connect(self.return_to_start)

        self.btn_task_start.setEnabled(False)
        self.btn_task_pause.setEnabled(False)
        self.btn_task_stop.setEnabled(False)

        disk_img = os.path.join(BASE_DIR,'app/settings/imgs/disk.png')
        self.show_selected_image(disk_img)

        def press_p1(): self.key_pressed("1")
        def press_p2(): self.key_pressed("2")
        def press_p3(): self.key_pressed("3")
        def press_p4(): self.key_pressed("4")
        def press_p5(): self.key_pressed("5")
        def press_p6(): self.key_pressed("6")
        def press_p7(): self.key_pressed("7")
        def press_p8(): self.key_pressed("8")

        self.btn_p1.clicked.connect(press_p1, type=Qt.UniqueConnection)
        self.btn_p2.clicked.connect(press_p2, type=Qt.UniqueConnection)
        self.btn_p3.clicked.connect(press_p3, type=Qt.UniqueConnection)
        self.btn_p4.clicked.connect(press_p4, type=Qt.UniqueConnection)
        self.btn_p5.clicked.connect(press_p5, type=Qt.UniqueConnection)
        self.btn_p6.clicked.connect(press_p6, type=Qt.UniqueConnection)
        self.btn_p7.clicked.connect(press_p7, type=Qt.UniqueConnection)
        self.btn_p8.clicked.connect(press_p8, type=Qt.UniqueConnection)

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
        self.labels = (
            self.lbl_p1,
            self.lbl_p2,
            self.lbl_p3,
            self.lbl_p4,
            self.lbl_p5,
            self.lbl_p6,
            self.lbl_p7,
            self.lbl_p8,
            )
        self.set_keys_checkable(True)
        self.event_finished = Event()

        self.ui.tabWidget.setStyleSheet(font_style)

        # for test
        # self.disk_key_pressed.connect(self.act_after_pressed)

    # for test
    @Slot(int)
    def act_after_pressed(self,n:int):
        time.sleep(2)
        self.disk_arrived_and_work_done(n)
    
    @Slot(int)
    def btn_pause_status_trans(self,n:int):
        if n==1:
            # logger.debug(f"btn_pause_pressed {n} 1 for show resume")
            self.btn_task_pause.setText(lang("resume"))
            self.btn_task_pause.setChecked(True)
            self.btn_task_stop.setEnabled(False)
        else:
            # logger.debug(f"btn_pause_pressed {n} 0 for show pause")
            self.btn_task_pause.setText(lang("pause"))
            self.btn_task_pause.setChecked(False)
            self.btn_task_stop.setEnabled(True)

    @Slot()    
    def btn_pause_clicked(self):
        if info.get("door_at_spot"): 
            if self.btn_task_pause.text() == lang("pause"):
                self.pause_signal.emit(1) #pause start
            else:
                self.pause_signal.emit(0) #pause end
        else:
            self.ui.popup(about=((lang("Alert"),lang("close_the_door"))))
            self.btn_task_pause.setChecked(True)

    @Slot()
    def btn_stop_clicked(self):
        if self.ui.popup(question=(lang("Alert"),lang("Error would happen.Are you sure?"))):
            self.stop_signal.emit(1)

    def return_to_start(self):
        self.ui.tabWidget.setCurrentIndex(1)

    def set_keys_checkable(self,enabled:bool):
        for key in self.keys:
            key.setCheckable(enabled)
            key.setStyleSheet(grid_key_style)
    def set_keys_enabled(self,enabled:bool):
        for key in self.keys:
            key.setEnabled(enabled)

    def show_selected_image(self, filename):
        self.graph.setPixmap(QPixmap(filename))

    @Slot(str)
    def key_pressed(self,n:str):
        if self.e_work.is_set():
            self.ui.popup(about=(lang('Alert'),lang('Busy for new job')))
            return
        self.e_work.set()
        self.event_finished.clear()
        btn = getattr(self,f"btn_p{n}")
        n = int(btn.text())
        self.disk_key_pressed.emit(n)
        pb = self.ui.popup(pb_dialog=("Wait","Processing"))
        pb.wait_to_exit(self.event_finished,3)
        




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
        self.event_finished.set()
        self.e_work.clear()
        self.disk_arrived(n)
        
    def refresh_disk_key_order(self,n:int):
        for i in range(8):
            key:QPushButton = self.keys[i]
            key.setText(str((n-1+i)%8+1))

            label:QLabel = self.labels[i]
            ctx = str(info.get("disk_info")[int(key.text())-1])
            label.setText(ctx)
            if ctx=="":
                label.setStyleSheet(u"background-color: rgba(255,255,224,0);")
                key.setStyleSheet(u"background-color: rgba(255,127,0,98);")
                key.setStyleSheet(grid_key_style)
            else:
                key.setStyleSheet(grid_key_style_ctx)
                if i == 0:
                    label.setStyleSheet(u"font-size:24px;background-color: rgb(0,255,0);")
                else:
                    label.setStyleSheet(u"font-size:24px;background-color: rgba(255,255,224,98);")



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
            f'{lang("step_needs")} {step_time_left}s,{lang("program_needs")} {pg_time_left}s'
            )
        self.disk_look_update(int(info.get("disk")))

    def check_signals(self,info):
        door_safe = info.get("door_at_spot")
        sheath_safe = info.get("sheath_at_spot")


class StatusWidgets():
    def status_widget(self,ui,e_work=None, e_stop=None):
        return StatusWidget(ui,status_map,e_work, e_stop)

status_widgets = StatusWidgets()

class TestStatusWidget():
    def __init__(self):
        from domains.ui.uis import application, uis
        self.app = application
        self.main_win = uis.main_win()
        self.main_win.show()
    def test_status_widget(self):
        pg = status_widgets.status_widget(self.main_win)
        pg.update()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    TestStatusWidget().test_status_widget()
    pass