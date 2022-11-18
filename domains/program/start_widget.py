from domains.program.programs import *
from prots import *

checked_img = os.path.join(BASE_DIR,'app','settings','imgs','checked.png')
unchecked_img = os.path.join(BASE_DIR,'app','settings','imgs','unchecked.png')
fold_img =  os.path.join(BASE_DIR,'app','settings','imgs','fold.png')
expand_img =  os.path.join(BASE_DIR,'app','settings','imgs','expand.png')
ico = os.path.join(BASE_DIR,'domains/ui/image/home.png')

start_map:dict = {
    "table":"treeWidget_2",
    "btn_scan":"pushButton_25",
    "btn_start":"pushButton_26",
    "btn_view":"pushButton_27",
}

# border:1px golid gray;
tree_style = """
    QTreeWidget{
        font-size:42px;
        border:1px solid gray;
    }
    QHeaderView::section
    {
        font-size: 32px;
        color:black;
        background:rgba(0,156,230,30);
        margin:5px;
        padding:0px;
    }
    QTreeWidget::item{margin:10px;}
    QTreeWidget::indicator {
        width:90px;
        height:60px;
        }
    QTreeWidget::indicator:checked {
        image:url('""" + checked_img + """');
        }
    QTreeWidget::indicator:unchecked {
        image:url('""" +unchecked_img+ """');
        }
    QTreeView::branch:open:has-children:!has-siblings{}
    QTreeView::branch:closed:has-children:!has-siblings{}
    QTreeView::branch:open:has-children {image: url('""" + fold_img + """');}
    QTreeView::branch:closed:has-children {image: url('""" + expand_img + """');}

  """
tree_style =  tree_style.replace("\\","/")


class StartWidget(aStartWidget):
    def __init__(self,ui,map):
        self.program_handler:Objsoner=programers.program_handler()
        super().__init__(ui,map)

        self._selected_idx = None
        self._checked_step_idxes = list()

        self.table:QTreeWidget = self.table
        self.table.setIconSize(QSize(90,60))
        self.table.header().setDefaultAlignment(Qt.AlignCenter)
        self.btn_scan.hide()
        self.btn_view.hide()
        self.btn_start.setStyleSheet(u"QPushButton{font:32px;}")
        self.table.setStyleSheet(tree_style)
        self.table_show()

    def scan(self):
        pass
    def start(self):
        try:
            idx = self.selected_idx
        except Exception as e:
            logger.error(e)
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
            if child.checkState(9) == Qt.Checked:
                step_idxes.append(idx)
        return step_idxes
    def table_update(self):
        self.table.clear()
        self.table_show()
        pass
    def table_show(self):
        program_handler = self.program_handler
        self.tree:QTreeWidget = self.table

        self.tree.setColumnCount(11)
        self.tree.setColumnWidth(0,270)
        self.tree.setColumnWidth(1,180)
        self.tree.setColumnWidth(2,180)
        for i in range(3,9):
            self.tree.setColumnWidth(i,120)
        self.tree.setColumnWidth(9,120)
        # self.tree.header().setSectionResizeMode(QHeaderView.Stretch)
        # self.tree.setHeaderHidden(True)
        self.tree.header().setLineWidth(0)                          #设置外线宽度
        self.tree.header().setMidLineWidth(0)
        self.tree.header().setFrameStyle(QFrame.VLine|QFrame.Plain)
        
        head = self.tree.headerItem()
        heads = ['','disk','op_name','ul_volumn','sec_mix','speed_mix','sec_mag','sec_wait','temperature','activated','']
        for i in range(11):
            head.setText(i,lang(heads[i]))
            # if i>2:
            head.setTextAlignment(i,Qt.AlignCenter)
            head.setFont(i,QFont('times', 18, QFont.Normal))
            head.setBackgroundColor(i,QColor(0,156,230,30))

        for pg in program_handler.obj_all():
            child = QTreeWidgetItem(self.tree)
            child.setText(0,pg.pg_name)
            child.setFont(0,QFont('times', 24, QFont.Black))
            child.setText(1,str(pg.idx))
            child.setTextColor(1,QColor(0,0,0,0))
            # child.setIcon(0,QIcon(ico))
            steps:list = pg.steps
            for step in steps:
                try:
                    chd = QTreeWidgetItem(child)
                    chd.setCheckState(9,Qt.Checked)
                    chd.setText(0,f"{lang('step')} {step[0]}")
                    chd.setText(1,f"{lang('disk')} {step[1]}")
                    chd.setText(2,str(step[2][0]))
                    chd.setText(3,str(step[2][1]))
                    chd.setText(4,str(step[2][2]))
                    chd.setText(5,str(step[2][3]))
                    chd.setText(6,str(step[2][4]))
                    chd.setText(7,str(step[2][5]))
                    chd.setText(8,str(step[2][6]))
                    for i in range(9):
                        chd.setTextAlignment(i,Qt.AlignCenter)
                        chd.setFont(i,QFont('times', 24, QFont.Normal))
                except Exception as e:
                    # logger.error(e)
                    pass
            self.tree.addTopLevelItem(child)
            
        # self.tree.expandAll()
        # self.tree.setItemsExpandable(False)
        # self.tree.setIconSize(QSize(48,48))
        # self.tree.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tree.setSelectionMode(QAbstractItemView.SingleSelection)

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
        print(self._selected_idx,"clicked")


class Widgets():
    def start_widget(self,ui):
        return StartWidget(ui,start_map)

start_widgets = Widgets()


class TestProgramerWidget():
    def __init__(self):
        from domains.ui.uis import application, uis
        self.app = application
        self.main_win = uis.main_win()
        self.main_win.show()
    def test_start_widget(self):
        pg = start_widgets.start_widget(self.main_win)
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    TestProgramerWidget().test_start_widget()