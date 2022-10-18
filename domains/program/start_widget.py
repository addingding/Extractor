from prots import *
from domains.program.programs import *

checked_img = os.path.join(BASE_DIR,'app','settings','imgs','checked.png')
unchecked_img = os.path.join(BASE_DIR,'app','settings','imgs','unchecked.png')

start_map:dict = {
    "table":"treeWidget_2",
    "btn_scan":"pushButton_25",
    "btn_start":"pushButton_26",
    "btn_view":"pushButton_27",
}

        # border:1px golid gray;
tree_style = """

    QHeaderView{
        }
    QHeaderView::section{
        background:rgba(0,156,230,30);
        margin:0px;
        height:30px;
        font: 18px;
    }
    QTreeWidget{
        font:24px;
        border:1px solid gray;
    }
    QTreeWidget::item{margin:4px;}
    QTreeWidget::indicator {
        width:40px;
        height:30px;
        }
    QTreeWidget::indicator:checked {
        image:url('""" + checked_img + """');
        }
    QTreeWidget::indicator:unchecked {
        image:url('""" +unchecked_img+ """');
        }

  """
tree_style =  tree_style.replace("\\","/")


class StartWidget(aStartWidget):
    def __init__(self,ui,map):
        self.program_handler:Objsoner=programers.program_handler()
        self.operation_handler:Objsoner=programers.operation_handler()
        super().__init__(ui,map)

        self._selected_idx = 0
        self._checked_step_idxes = list()

        self.table:QTreeWidget = self.table
        self.table.setIconSize(QSize(60,30))
        self.table.setStyleSheet(tree_style)
        self.btn_scan.hide()
        self.btn_view.hide()
        self.btn_start.setStyleSheet(u"QPushButton{font:32px;}")
        self.table_show()

    def scan(self):
        pass
    def start(self):
        try:
            idx = self.selected_idx
        except Exception as e:
            print(e)
    def view(self):
        self.ui.tabWidget.setCurrentIndex(2)
        pass

    @property
    def selected_idx(self):
        return self._selected_idx

    @property
    def selected_program(self)->aProgram:
        if self.selected_idx is None: return None
        return self.program_handler.obj(self.selected_idx)
    def get_checked_steps(self):
        #DONE! TODO get checked steps
        if self.selected_program is None: return
        steps = list()
        _steps = self.selected_program.steps
        checked_idxes = self.__get_checked_step_idxes()
        for idx in checked_idxes:
            steps.append(_steps[idx])
        return steps
    def __get_checked_step_idxes(self):
        if self.selected_program is None: return
        step_idxes = list()
        item = self.tree.currentItem()
        if not item.parent() is None:
            item = item.parent()
        children_cnt = item.childCount()
        for idx in range(children_cnt):
            child = item.child(idx)
            if child.checkState(0) == Qt.Checked:
                step_idxes.append(idx)
        return step_idxes
    def table_update(self):
        self.table.clear()
        self.table_show()
        pass
    def table_show(self):
        ico = os.path.join(BASE_DIR,'domains/ui/image/home.png')
        program_handler = self.program_handler
        operation_handler = self.operation_handler
        self.tree:QTreeWidget = self.table

        self.tree.setColumnCount(9)
        self.tree.setColumnWidth(0,200)
        self.tree.setColumnWidth(1,120)
        self.tree.setColumnWidth(2,120)
        for i in range(3,9):
            self.tree.setColumnWidth(i,80)
        # self.tree.header().setSectionResizeMode(QHeaderView.Stretch)
        # self.tree.setHeaderHidden(True)
        # self.tree.header().setLineWidth(1)                          #设置外线宽度
        # self.tree.header().setMidLineWidth(0)
        # self.tree.header().setFrameStyle(QFrame.VLine|QFrame.Plain)                          #设置外线宽度
        self.tree.header().setMidLineWidth(0)
        self.tree.header().setFrameStyle(QFrame.VLine|QFrame.Plain)
        head = self.tree.headerItem()
        heads = ['','disk','op_name','sec_wait','sec_mix','sec_mag','ul_volumn','speed_mix','temperature']
        for i in range(9):
            head.setText(i,lang(heads[i]))
            # if i>2:
            #     head.setTextAlignment(i,Qt.AlignHCenter)

        for pg in program_handler.obj_all():
            child = QTreeWidgetItem(self.tree)
            child.setText(0,pg.pg_name)
            child.setText(1,str(pg.idx))
            child.setIcon(0,QIcon(ico))
            steps:list = pg.steps
            for step in steps:
                try:
                    chd = QTreeWidgetItem(child)
                    chd.setCheckState(0,Qt.Checked)
                    chd.setText(0,f"{lang('step')} {step[0]}")
                    chd.setText(1,f"{lang('disk')} {step[1]}")
                    op = operation_handler.obj(int(step[2])) 
                    chd.setText(2,op.op_name)
                    chd.setText(3,str(op.sec_wait))
                    chd.setText(4,str(op.sec_mix))
                    chd.setText(5,str(op.sec_mag))
                    chd.setText(6,str(op.ul_volumn))
                    chd.setText(7,str(op.speed_mix))
                    chd.setText(8,str(op.temperature))
                except Exception as e:
                    # print(e)
                    pass
            self.tree.addTopLevelItem(child)
        self.tree.expandAll()
        self.tree.clicked.connect(self.onTreeClicked)
    
    def onTreeClicked(self,qmodelindex):
        item = self.tree.currentItem()
        if item is None:
            self._selected_idx = None
        else:
            if item.parent() is None:
                idx = item.text(1)
            else:
                idx = item.parent().text(1)
            self._selected_idx = idx


class Widgets():
    def start_widget(self,ui):
        return StartWidget(ui,start_map)

start_widgets = Widgets()


class TestProgramerWidget():
    def __init__(self):
        from domains.ui.uis import application,uis
        self.app = application
        self.main_win = uis.main_win()
        self.main_win.show()
    def test_start_widget(self):
        pg = start_widgets.start_widget(self.main_win)
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    TestProgramerWidget().test_start_widget()