from domains.program.lock_widget import LockWidget
from domains.program.programs import *
from prots import *

font_scale = 1
grid = int(60*font_scale)
font_size = int(28*font_scale)

program_map = {
    "table":"treeWidget",
    "btn_create":"pushButton_13",
    "btn_copy":"pushButton_15",
    "btn_edit":"pushButton_21",
    "btn_save":"pushButton_14",
    "btn_delete":"pushButton_16",
    "btn_delete_all":"pushButton_22",
    "btn_insert_up":"pushButton_58",
    "btn_insert_down":"pushButton_59",
}

# operation_map = {
#     "table":"tableWidget_3",
#     "btn_create":"pushButton_33",
#     "btn_copy":"pushButton_35",
#     "btn_edit":"pushButton_36",
#     "btn_save":"pushButton_34",
#     "btn_delete":"pushButton_17",
#     "btn_delete_all":"pushButton_37",
    
# }

button_lock = "pushButton_55"

locked_buttons = [
    "pushButton_13",
    "pushButton_15",
    "pushButton_21",
    "pushButton_14",
    "pushButton_16",
    "pushButton_22",
    "pushButton_33",
    "pushButton_35",
    "pushButton_36",
    "pushButton_34",
    "pushButton_17",
    "pushButton_37",
    "pushButton_58",
    "pushButton_59",
]

fold_img =  os.path.join(BASE_DIR,'app','settings','imgs','fold.png')
expand_img =  os.path.join(BASE_DIR,'app','settings','imgs','expand.png')


table_style = """

    QTreeWidget{
        border:1px solid gray;
        border-radius:5px;
        background:rgba(255,255,255,0);
    }
    QTreeWidget::item{margin:8px;}
    QTreeWidget::branch:open:has-children {image: url('""" + fold_img + """');}
    QTreeWidget::branch:closed:has-children {image: url('""" + expand_img + """');}
    QHeaderView::section
    {
        font-size:"""+f'{font_size}'+"""px;
        color:black;
        background:rgba(0,156,230,30);
        border:1px solid gray;
        margin-left:0px;
        padding-left:0px;
    }

    QTableWidget::item
    {
        border-bottom:1px solid #EEF1F7 ;
    }

    QTableWidget::item::selected
    {
        color:red;
        background:#EFF4FF;
    }


    QScrollBar::handle:vertical
    {
        background: rgba(255,255,255,20%);
        border: 0px solid grey;
        border-radius:3px;
        width: 6px;
    }


  """
table_style =  table_style.replace("\\","/")

class ProgramWidget(aProgrameWidget):
    def __init__(self,ui,map):
        self.program_handler:Objsoner=programers.program_handler()
        aProgrameWidget.__init__(self,ui,map)
        table:QTreeWidget = self.table
        self._set_default_style()

        self.lock_widget = LockWidget(ui,"2022",locked_buttons,button_lock)
        self.lock_widget.lock_buttons()
        self._selected_program_idx:int = None
        self._selected_step_idx:int = None
        self.btn_insert_up.clicked.connect(self.insert_blank_up)
        self.btn_insert_down.clicked.connect(self.insert_blank_down)

        self.table_show()

    def _set_default_style(self):
        global table_style
        self.table.header().setDefaultAlignment(Qt.AlignCenter)
        self.table.setStyleSheet(table_style)
        self.table.setIndentation(40)

    def edit(self):
        pass
    def create(self):
        text = self.ui.popup(dialog=(lang("Input"),lang("Program Name")))
        if text:
            obj:aProgram = self.program_handler.create()
            obj.pg_name = text
            obj.steps = []
            counts = self.ui.popup(dialog=(lang('Input'), lang('Steps number')))
            try:
                counts = int(counts)
                if isinstance(counts,int):
                    for i in range(1,int(counts)+1):
                        obj.steps.append([i,1,[""]*7])
                self.program_handler.update(obj)
            except Exception as e:
                # logger.error(e)
                pass
        self.table_update()
    def copy(self):
        try:
            idx:int = self._selected_program_idx
            new_obj = self.program_handler.copy(idx)
        except Exception as e:
            logger.error(e)
        self.table_update()
        pass


    def save(self): #TODO
        n = self.tree.topLevelItemCount()
        for i in range(1, n+1):
            item = self.tree.topLevelItem(i-1)
            idx = int(item.text(1))
            pg:aProgram = self.program_handler.obj(idx)
            
            pg.pg_name = item.text(0)

            count = item.childCount()
            steps = []
            for j in range(0, count):
                step = []
                child = item.child(j)
                step.append(j+1)
                step.append(child.text(1))

                settings = []
                for k in range(7):
                    settings.append(child.text(2+k))
                step.append(settings)
                steps.append(step)
            pg.steps = steps
            self.program_handler.update(pg)
        self.table_update()

    def insert_blank_up(self):
        if self._selected_step_idx is None:
            return
        self.program_handler.insert(self._selected_program_idx,self._selected_step_idx)
        self.table_update()
    def insert_blank_down(self):
        if self._selected_step_idx is None:
            return
        self.program_handler.insert(self._selected_program_idx,self._selected_step_idx+1)
        self.table_update()
    
    def delete_program(self,prg_idx:int):
        try:
            self.program_handler.delete(prg_idx)
        except Exception as e:
            logger.error(e)
    def delete_step(self,prg_idx:int,stp_idx:int):
        try:
            self.program_handler.delete(prg_idx,stp_idx)
        except Exception as e:
            logger.error(e)
        
    def delete(self):
        if not self.ui.popup(question=(lang("Alert"),lang("Sure_to_Delete?"))):
            return
        if self._selected_program_idx is None:
            return
        elif self._selected_step_idx is None:
            self.delete_program(self._selected_program_idx)
        else:
            self.delete_step(self._selected_program_idx,self._selected_step_idx)

        self.table_update()

    def delete_all(self):
        pass

    def table_update(self):
        # self.table.hide()
        # self.table.show()
        self.table.clear()
        self.table_show()
        self.ui.program_updated.emit(1)
        pass

    def table_show(self):
        program_handler = self.program_handler
        self.tree:QTreeWidget = self.table


        self.tree.setColumnCount(10)
        self.tree.setColumnWidth(0,int(grid*4.5))
        self.tree.setColumnWidth(1,int(grid*2.5))
        self.tree.setColumnWidth(2,int(grid*3))
        for i in range(3,9):
            self.tree.setColumnWidth(i,int(grid*2.1))
        self.tree.setColumnWidth(9,1)
        # self.tree.header().setSectionResizeMode(QHeaderView.Stretch)
        # self.tree.setHeaderHidden(True)
        # self.tree.header().setLineWidth(1)                          #设置外线宽度
        # self.tree.header().setMidLineWidth(0)
        # self.tree.header().setFrameStyle(QFrame.VLine|QFrame.Plain)                          #设置外线宽度
        
        # self.tree.header().setMidLineWidth(0)
        # self.tree.header().setFrameStyle(QFrame.VLine|QFrame.Plain)
        head:QTreeWidgetItem = self.tree.headerItem()
        heads = ['','disk','op_name','ul_volumn','sec_mix','speed_mix','sec_mag','sec_wait','temperature','']
        for i in range(10):
            head.setText(i,lang(heads[i]))
            head.setFont(i,QFont('times', 18, QFont.Normal))
            head.setBackgroundColor(i,QColor(0,156,230,30))
            # if i>2:
            head.setTextAlignment(i,Qt.AlignCenter)

        for pg in program_handler.obj_all():
            child = QTreeWidgetItem(self.tree)
            child.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable)
            child.setText(0,pg.pg_name)
            child.setFont(0,QFont('times', int(font_size), QFont.Black))
            child.setText(1,str(pg.idx))
            child.setTextColor(1,QColor(0,0,0,0))
            # child.setIcon(0,QIcon(ico))
            steps:list = pg.steps
            for step in steps:
                chd = QTreeWidgetItem(child)
                chd.setText(0,f"{lang('step')} {step[0]}")
                chd.setText(1,f"{step[1]}")
                chd.setText(2,str(step[2][0]))
                chd.setText(3,str(step[2][1]))
                chd.setText(4,str(step[2][2]))
                chd.setText(5,str(step[2][3]))
                chd.setText(6,str(step[2][4]))
                chd.setText(7,str(step[2][5]))
                chd.setText(8,str(step[2][6]))
                for i in range(9):
                    chd.setTextAlignment(i,Qt.AlignHCenter)
                    chd.setFont(i,QFont('times', int(font_size), QFont.Normal))
                for i in range(1,9):
                    chd.setFlags(Qt.ItemIsEnabled | Qt.ItemIsEditable)


            self.tree.addTopLevelItem(child)

            
        self.tree.expandAll()
        # self.tree.setItemsExpandable(False)

        self.tree.clicked.connect(self.onTreeClicked)
        self.tree.itemDoubleClicked.connect(self.expand_keyboard)

    def expand_keyboard(self,item=None,column=None):
        item = self.tree.currentItem()
        _is_editable = (Qt.ItemIsEditable & item.flags()) and (Qt.ItemIsEnabled & item.flags())
        _is_pg = item.parent() is None
        _is_step = item.parent() is not None
        _editable = _is_editable and ((_is_pg and column==0) or (_is_step and column>0))
        if _editable:
            Thread(target = os.system,args=("onboard&",),daemon=True).start()

    def onTreeClicked(self,qmodelindex):
        item = self.tree.currentItem()
        if item is None:
            self._selected_program_idx = None
            self._selected_step_idx = None
        else:
            if item.parent() is None: #根节点
                self._selected_program_idx = int(item.text(1))
                self._selected_step_idx = None

            else:
                self._selected_program_idx = int(item.parent().text(1))
                self._selected_step_idx = int((item.text(0).split(" "))[1])
        # print(self._selected_program_idx,self._selected_step_idx)


class Widgets():
    def program_widget(self,ui):
        return ProgramWidget(ui,program_map)
    # def operation_widget(self,ui):
    #     return OperationWidget(ui,operation_map)

programer_widgets = Widgets()


class TestProgramerWidget():
    def __init__(self):
        from domains.ui.uis import application, uis
        self.app = application
        self.main_win = uis.main_win()
        self.main_win.show()
    def test_programer(self):
        pg = programer_widgets.program_widget(self.main_win)
        # op = programer_widgets.operation_widget(self.main_win)
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    TestProgramerWidget().test_programer()