from prots.roles._uis import *
from prots.roles._database import aDatabase
from domains.database.database_models import User
import re
from peewee import IntegerField,FloatField

class ModelEditor(ABC):
    def __init__(self,ui_table:QTableWidget,model_name:str,database:aDatabase,user:str=None,cbox:dict=None):
        self.table:QTableWidget = ui_table

        self.model_name = model_name
        self.database = database
        self.user = user
        self.cbox:dict = cbox
        self._setup_table()
        self._enable_itemchange()
        self._update_contents()
        self._set_table_function()

    def _setup_table(self):
        self._load_fields()
        # self.table.setWordWrap(True)
        self.table.setAlternatingRowColors(True)
        self.table.setColumnCount(self.col)
        self.table.setHorizontalHeaderLabels(self.aliases)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setStyleSheet("QHeaderView::section{background-color:rgb(232,232,255)}")

    def _load_fields(self):
        fields,_aliases = self.database.get_fields(self.model_name)
        
        for field in fields:
            if (field in ["id","user"]):
                fields.remove(field)
        for field in fields:
            if (field.endswith("_id")):
                fields.remove(field)

        self.fields = fields
        self.aliases = [self._cut_name(_aliases.get(f)) for f in self.fields]
        self.col:int = len(self.fields)
    def _cut_name(self,name):
        # if name is None:
        #     return ""
        # if len(name)>8:
        #     name = name[:8]
        # _parts= re.findall(r'.{2}',name)
        # name = "\n".join(_parts)
        return name
    def _update_contents(self):
        self._clear_contents()
        self._load_instances()
        self._set_rows()
        self._set_ids()
        self._set_instances()
        self._put_blank_row()
        self._put_add_button()

    def _enable_itemchange(self):
        # print("itemChanged activated")
        self.table.itemChanged.connect(self._update)
    def _disable_itemchanged(self):
        # print("itemChanged disconnect")
        self.table.itemChanged.disconnect()


    def _clear_contents(self):
        self.table.clearContents()
    def _set_rows(self):
        self.table.setRowCount(self.row+1)
    def _load_instances(self):
        self.instances = self.database.get_ins_list(self.model_name)#,User=self.user)
        self.row:int = len(self.instances)
    def _set_ids(self):
        _ids = [str(ins.id) for ins in self.instances]
        _ids.append('+')
        self.table.setVerticalHeaderLabels(_ids)
    def _set_instances(self):
        r = 0
        for instance in self.instances:
            for c in range(self.col):
                try:
                    key = self.fields[c]
                    if (self.cbox is not None) and (key in self.cbox.keys()):
                        self._set_cbox_item(r,c,key,self.cbox.get(key))
                    else:
                        _v = getattr(instance,key)
                        item = QTableWidgetItem()
                        item.setText(str(_v))
                        self.table.setItem(r,c,item)
                except Exception as e:
                    print("setting_instance_error",e)
            r += 1
    def _set_cbox_item(self,r,c,key,value):
        cb = QComboBox()
        if isinstance(value,str):
            instances = self.database.get_ins_list(value)
            cb_value = [ins.name for ins in instances]
        else:
            cb_value = value
        cb.addItems(cb_value)
        cb.currentIndexChanged.connect(self._update)
        self.table.setCellWidget(r,c,cb)
        setattr(self,f"cb_{key}",cb)

    def _put_blank_row(self):
        for c in range(self.col):
            key = self.fields[c]
            if (self.cbox is not None) and (key in self.cbox.keys()):
                self._set_cbox_item(self.row,c,key,self.cbox.get(key))
            else:
                item =QTableWidgetItem()
                self.table.setItem(self.row,c,item)
    def _put_add_button(self):
        self.table.verticalHeader().sectionClicked.connect(self._add)
        
    def _set_table_function(self):
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table.setSortingEnabled(True)


    def _sub(self):
        pass
    def _update(self,item=None):
        if self.table.verticalHeaderItem(item.row()).text() in ["+"]:
            return
        _widget = self.table.cellWidget(item.row(),item.column())
        if _widget is not None:
            text = _widget.text()
            field = self.fields[item.column()]
            ins = self.database.get_ins(self.model_name,id=item.row()+1)
            fld = getattr(ins,field)
            if isinstance(fld,IntegerField):
                text = int(text)
            if isinstance(fld,FloatField):
                text = float(text)
            setattr(ins,field,text)
            ins.save()
        
    def __add(self,row=None):
        kwargs ={}
        for col in range(len(self.fields)):
            item = self.table.item(row,col)
            if item is not None:
                _v = item.text()
            else:
                _v = ""
            kwargs.update({self.fields[col]:_v})
        self.database.create_ins(self.model_name,**kwargs)

    def _add(self,row=None):
        if row is None:
            return
        if self.table.verticalHeaderItem(row).text() in ["+"]:
            self._disable_itemchanged()
            try:
                self.__add(row)
            except Exception as e:
                print(e)
            self._update_contents()
            self._enable_itemchange()

class Editors:
    def get_configor_editors(self,db,ui):
        editors = dict(
            screw_type_editor = ModelEditor(ui.tableWidget,"ScrewType",db,cbox={"cw":["正","反"],"mtd":"InspectSet"}),
            inspect_editor = ModelEditor(ui.tableWidget_2,"InspectSet",db,cbox={"acceleration":["S曲线加速","梯形加速"],
                "limit_means":["光电开关定位","限位定位"],"inspect_type":"InspectType"}),
            inspect_type_editor = ModelEditor(ui.tableWidget_3,"InspectType",db),
            user_editor = ModelEditor(ui.tableWidget_4,"User",db)
        )
        return editors
    def get_operator_editors(self,db,ui,user):
        editors = dict(

        )

class TestEditor:
    def __init__(self,db,ui):
        self.db = db
        self.ui = ui
    def test_editor(self):
        editors = dict(
            screw_type_editor = ModelEditor(ui.tableWidget,"ScrewType",db,cbox={"cw":["正","反"],"mtd":"InspectSet"}),
            inspect_editor = ModelEditor(ui.tableWidget_2,"InspectSet",db,cbox={"acceleration":["S曲线加速","梯形加速"],
                "limit_means":["光电开关定位","限位定位"],"inspect_type":"InspectType"}),
            inspect_type_editor = ModelEditor(ui.tableWidget_3,"InspectType",db),
            user_editor = ModelEditor(ui.tableWidget_4,"User",db)
        )
        return editors

if __name__=="__main__":
    import sys
    from domains.ui._uis import application

    from domains.database.database import dbs
    db = dbs.get_default_database()

    from domains.ui._uis import uis
    ui = uis.configor_win()
    test = TestEditor(db,ui)

    test.test_editor()

    ui.show()

    application.exec()
    sys.exit(0)

    