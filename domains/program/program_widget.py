from prots import *
from domains.program.programs import *
from domains.program.lock_widget import LockWidget


program_map = {
    "table":"treeWidget",
    "btn_create":"pushButton_13",
    "btn_copy":"pushButton_15",
    "btn_edit":"pushButton_21",
    "btn_save":"pushButton_14",
    "btn_delete":"pushButton_16",
    "btn_delete_all":"pushButton_22",
}

operation_map = {
    "table":"tableWidget_3",
    "btn_create":"pushButton_33",
    "btn_copy":"pushButton_35",
    "btn_edit":"pushButton_36",
    "btn_save":"pushButton_34",
    "btn_delete":"pushButton_17",
    "btn_delete_all":"pushButton_37",
    
}

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
]

tree_style_1 = """
    QTreeWidget{
        font:22px;
        border:1px solid gray;
    }

  """
table_style = """

    QHeaderView::section
    {
        font-size:18px;
        color:black;
        background:rgba(255,255,255,0);
        border:1px solid gray;
        margin-left:0px;
        padding-left:0px;
    }

    QTableWidget
    {
        font-size:22px;
        background:rgba(255,255,255,0);
        border:1px solid gray;
        border-radius:10px;
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

class ProgramWidget(aProgrameWidget):
    def __init__(self,ui,map):
        self.program_handler:Objsoner=programers.program_handler()
        self.operation_handler:Objsoner=programers.operation_handler()
        aProgrameWidget.__init__(self,ui,map)
        table:QTreeWidget = self.table
        table.setStyleSheet(tree_style_1)
        table.header().setDefaultAlignment(Qt.AlignCenter)

        self.lock_widget = LockWidget(ui,"2022",locked_buttons,button_lock)
        self.lock_widget.lock_buttons()

        self.table_show()


    def create(self):
        text = self.ui.popup(dialog=('输入程序名称', '程序名称:'))
        if text:
            obj:aProgram = self.program_handler.create()
            obj.pg_name = text
            obj.steps = []
            counts = self.ui.popup(dialog=('输入步骤数', '步骤数'))
            try:
                counts = int(counts)
                if isinstance(counts,int):
                    for i in range(1,int(counts)+1):
                        obj.steps.append([i,i,""])
                self.program_handler.update(obj)
            except Exception as e:
                # print(e)
                pass
        self.table_update()
    def copy(self):
        try:
            idx = self.selected_idx
            new_obj = self.program_handler.copy(idx)
        except Exception as e:
            print(e)
        self.table_update()
        pass

    def edit(self):
        item = self.tree.currentItem()
        if item is None: return
        if item.parent() is None:
            text, ok = MyQInputDialog.getText(self.ui, '输入程序名称', '程序名称:')
            if ok and text:
                item.setText(0, text)
        else:
            disks =  [str(i) for i in range(1,9)]
            operations = self.operation_handler.obj_names()
            disk, ok = MyQInputDialog.getItem(self.ui, '选择盘位', '盘位(1-8):',disks,0,True)
            if ok and disk:
                item.setText(1, f"盘位 {str(disk)}")
                op_name, ok = MyQInputDialog.getItem(self.ui, '选择操作', '操作:',operations,0,True)
                if ok and op_name:
                    idx = self.operation_handler.obj_idxes()[operations.index(op_name)]
                    op = self.operation_handler.obj(idx)
                    item.setText(2,op.op_name)
                    item.setText(3,str(op.sec_wait))
                    item.setText(4,str(op.sec_mix))
                    item.setText(5,str(op.sec_mag))
                    item.setText(6,str(op.ul_volumn))
                    item.setText(7,str(op.speed_mix))
                    item.setText(9,str(op.temperature))
    def save(self): #TODO
        n = self.tree.topLevelItemCount()
        for i in range(1, n+1):
            item = self.tree.topLevelItem(i-1)
            text = item.text(0)
            idx = int(item.text(1))
            pg:aProgram = self.program_handler.obj(idx)
            pg.pg_name = text
    
            count = item.childCount()
            steps = []
            for j in range(0, count):
                child = item.child(j)
                step_idx = j+1
                step_partition = child.text(1).split(" ")[1]
                try:
                    step_operation_idx = self.operation_handler.get_obj_by_name(child.text(2)).idx
                except ValueError:
                    step_operation_idx = 1
                except Exception as e:
                    print(e)
                    step_operation_idx = 1
                steps.append([step_idx,step_partition,str(step_operation_idx)])
            pg.steps = steps
            self.program_handler.update(pg)
        self.table_update()
    def delete(self):
        if not self.ui.popup(question=(lang("Alert"),lang("Sure to Delete?"))):
            return
        try:
            self.program_handler.delete(int(self.selected_idx))
            self.table_update()
        except Exception as e:
            print(e)
        pass
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
        ico = os.path.join(BASE_DIR,'domains/ui/image/home.png')
        program_handler = self.program_handler
        operation_handler = self.operation_handler
        self.tree:QTreeWidget = self.table

        self.tree.setColumnCount(9)
        self.tree.setColumnWidth(0,150)
        self.tree.setColumnWidth(1,120)
        self.tree.setColumnWidth(2,150)
        for i in range(3,9):
            self.tree.setColumnWidth(i,75)
        # self.tree.header().setSectionResizeMode(QHeaderView.Fixed)
        self.tree.setHeaderHidden(True)

        for pg in program_handler.obj_all():
            child = QTreeWidgetItem(self.tree)
            child.setText(0,pg.pg_name)
            child.setText(1,str(pg.idx))
            child.setIcon(0,QIcon(ico))
            steps:list = pg.steps
            for step in steps:
                try:
                    chd = QTreeWidgetItem(child)
                    chd.setText(0,f"{lang('step')} {step[0]}")
                    chd.setText(1,f"{lang('disk')} {step[1]}    ")
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
        if item is None: return
        if item.parent() is None:
            idx = item.text(1)
            self.selected_idx = idx

    

class OperationWidget(aOperationWidget):
    def __init__(self,ui,map):
        self.handler:Objsoner=programers.operation_handler()
        super().__init__(ui,map)
        self.table.setStyleSheet(table_style)
        self.table_show()
        self.items = ['op_name','sec_wait','sec_mix','sec_mag','ul_volumn','speed_mix','temperature']


    def create(self):
        self.handler.create()
        self.table_update()
        self.edit()
        pass
    def copy(self):
        try:
            idx = self.table.currentIndex().row()
            if idx<0: return
            origin_obj = self.handler.obj(idx)

            new_obj = self.handler.create()
            for item in self.items:
                setattr(new_obj,item,getattr(origin_obj,item))
            self.handler.update(new_obj)
        except Exception as e:
            print(e)
        self.table_update()
        self.edit()
        pass
    def edit(self):
        self.table.setEditTriggers(QAbstractItemView.AllEditTriggers)#編輯

    def save(self):
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)#禁止編輯
        handler = self.handler
        table:QTableWidget = self.table
        objs =handler.obj_all()
        rows = len(objs)
        columns = 7
        items = self.items

        for r in range(rows):
            obj = objs[r]
            for c in range(columns):
                item = items[c]
                table_item = table.item(r,c)
                data_type = type(getattr(obj,item))
                try:
                    setattr(obj,item,data_type(table_item.text()))
                    # table_item.setTextAlignment(Qt.AlignCenter)
                except Exception as e:
                    print(e)
            handler.update(obj)
        
        self.table_update()

    def delete(self):
        if not self.ui.popup(question=(lang("Alert"),lang("Sure to Delete?"))):
            return
        try:
            idx = self.table.currentIndex().row()
            obj = self.handler.obj_all()[idx]
            self.handler.delete(int(obj.idx))
            self.table_update()
        except Exception as e:
            print(e)
        pass
    def delete_all(self):
        pass

    def table_update(self):
        # self.table.hide()
        # self.table.show()
        self.table.clear()
        self.table_show()
        pass
    def table_show(self):
        handler = self.handler
        table:QTableWidget = self.table
        objs =handler.obj_all()
        rows = len(objs)
        columns = 7
        items = ['op_name','sec_wait','sec_mix','sec_mag','ul_volumn','speed_mix','temperature']

        table.setColumnCount(columns)
        table.setRowCount(rows)
        table.setHorizontalHeaderLabels(lang(items))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)#禁止編輯
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setSortingEnabled (False)
        for r in range(rows):
            obj = objs[r]
            for c in range(columns):
                item_content = items[c]
                table.setItem(r,c,QTableWidgetItem(str(getattr(obj,item_content))))
                table.item(r,c).setTextAlignment(Qt.AlignHCenter)


    def onTreeClicked(self,qmodelindex):
        item = self.tree.currentItem()
        if item is None: return
        if item.parent() is None:
            idx = item.text(1)
            self.selected_idx = idx
    


class Widgets():
    def program_widget(self,ui):
        return ProgramWidget(ui,program_map)
    def operation_widget(self,ui):
        return OperationWidget(ui,operation_map)

programer_widgets = Widgets()


class TestProgramerWidget():
    def __init__(self):
        from domains.ui.uis import application,uis
        self.app = application
        self.main_win = uis.main_win()
        self.main_win.show()
    def test_programer(self):
        pg = programer_widgets.program_widget(self.main_win)
        op = programer_widgets.operation_widget(self.main_win)
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    TestProgramerWidget().test_programer()