from prots import *
LANGUAGES[0] = 0

trans_map = {
    "btn_Chinese":"pushButton_29",
    "btn_traditional":"pushButton_30",
    "btn_English":"pushButton_31"
}

def retranslate_ui(window):
    window.label_29.setText(lang("temp_control"))
    window.label_30.setText(f'{lang("disk")} 1')
    window.label_33.setText(f'{lang("disk")} 8')
    window.label_21.setText(lang("sec_mag"))
    window.label_23.setText(lang("ul_volumn"))
    window.label_17.setText(lang("sec_wait"))
    window.label_14.setText(lang("disk"))
    window.label_12.setText(lang("op_name"))
    window.label_27.setText(lang("temperature"))
    window.label_34.setText(lang("step"))
    window.label_19.setText(lang("sec_mix"))
    window.label_26.setText(lang("speed_mix"))
    window.tabWidget.setTabText(window.tabWidget.indexOf(window.tab_status), lang("status_inspection"))
    window.pushButton_25.setText(lang("scan"))
    window.pushButton_26.setText(lang("start"))
    window.pushButton_27.setText(lang("view"))
    window.tabWidget.setTabText(window.tabWidget.indexOf(window.tab_run), lang("program_start"))
    window.groupBox_7.setTitle(lang("programs"))
    window.pushButton_13.setText(lang("new_program"))
    window.pushButton_15.setText(lang("copy"))
    window.pushButton_21.setText(lang("edit"))
    window.pushButton_14.setText(lang("save"))
    window.pushButton_16.setText(lang("delete"))
    window.pushButton_22.setText(lang("delete_all"))
    window.groupBox_6.setTitle(lang("steps"))
    window.pushButton_33.setText(lang("new_step"))
    window.pushButton_35.setText(lang("copy"))
    window.pushButton_36.setText(lang("edit"))
    window.pushButton_34.setText(lang("save"))
    window.pushButton_17.setText(lang("delete"))
    window.pushButton_37.setText(lang("delete_all"))
    window.tabWidget.setTabText(window.tabWidget.indexOf(window.tab_program), lang("program_manage"))
    window.pushButton_8.setText(lang("time_set"))
    window.pushButton_12.setText(lang("language"))
    window.pushButton_11.setText(lang("upgrade"))
    window.pushButton_10.setText(lang("program_io"))
    window.groupBox_2.setTitle(lang("device_set"))
    
    window.groupBox.setTitle(lang("time_set"))
    window.pushButton_28.setText(lang("accept"))
    window.groupBox_3.setTitle(lang("program_io"))
    window.groupBox_4.setTitle(lang("upgrade"))
    window.groupBox_5.setTitle(lang("language"))
    window.tabWidget.setTabText(window.tabWidget.indexOf(window.tab_manage), lang("device_manage"))
    window.pushButton_23.setText(lang("stop"))
    window.pushButton_6.setText(lang("reset"))
    window.pushButton_7.setText(lang("start"))
    window.pushButton_24.setText(lang("pause"))
    window.tabWidget.setTabText(window.tabWidget.indexOf(window.tab_sterilize), lang("sterilize"))
    window.toolBox.setItemText(window.toolBox.indexOf(window.page_status), lang("status_inspection"))
    window.toolBox.setItemText(window.toolBox.indexOf(window.page_run), lang("program_start"))
    window.toolBox.setItemText(window.toolBox.indexOf(window.page_program), lang("program_manage"))
    window.toolBox.setItemText(window.toolBox.indexOf(window.page_manage), lang("device_manage"))
    window.toolBox.setItemText(window.toolBox.indexOf(window.page_sterilize), lang("sterilize"))
    window.toolBox.setItemText(window.toolBox.indexOf(window.page_3), lang("version"))
    window.tabWidget.setTabText(window.tabWidget.indexOf(window.tab_help), lang("helps"))
    window.pushButton.setText(lang("quit"))
    window.pushButton_2.setText(lang("cw_jog"))
    window.pushButton_3.setText(lang("ccw_jog"))
    window.pushButton_4.setText(lang("fan"))
    window.pushButton_5.setText(lang("light"))
    window.pushButton_18.setText(lang("stop"))
    window.pushButton_19.setText(lang("pause"))
    window.pushButton_20.setText(lang("home"))
    window.pushButton_38.setText(lang("stir_calib"))
    window.pushButton_39.setText(lang("mag_calib"))
    window.pushButton_40.setText(lang("disk_calib"))
    window.pushButton_41.setText(lang("calibration"))
    window.pushButton_42.setText(lang("return"))
    window.groupBox_8.setTitle(lang("calibration"))
    window.pushButton_9.setText(lang("Import Programs"))
    window.pushButton_51.setText(lang("Export Programs"))
    window.pushButton_52.setText(lang("Directory"))

# retranslateUi

class LanguageTrans(aWidget):
    def __init__(self, ui):
        super().__init__(ui, trans_map)
        self.ui = ui
        self.tables = ()
        self.activate_lang()
    
    def activate_lang(self):
        self.btn_Chinese.clicked.connect(self.lang_chinese)
        self.btn_traditional.clicked.connect(self.traditional)
        self.btn_English.clicked.connect(self.lang_english)
    def lang_chinese(self):
        self.lang_trans(1)
    def traditional(self):
        self.lang_trans(1)
    def lang_english(self):
        self.lang_trans(0)
    def lang_trans(self,idx):
        LANGUAGES[0] = idx
        retranslate_ui(self.ui)
        self.trans_tables()

    
    def collect_tables(self,*args):
        self.tables = args
    def trans_tables(self):
        for table in self.tables:
            table.table_update()

class Translators:
    def translator(self,ui):
        return LanguageTrans(ui)

translators = Translators()