def link_ui_fuction(self):
    self.item_sub.clicked.connect(self._sub)


def _update_items(self):
    self._update_items_data()
    self._update_items_ui()

def _update_items_data(self):
    item_list = []
    instances = self.database.get_ins_list(self.model_name,user=self.user)
    for _item in instances:
        item_list.append(_item.name)

def _update_items_ui(self):
    self.item_list.clear()
    self.item_list.addItems(self.types_)
    self.item_list.itemClicked.connect(self.type_item_clicked)

    # editor = self.ui.lineEdit_2
    # editor.setFont(QFont("宋体",18))
    # editor.setAttribute(Qt.WA_InputMethodEnabled,True)
    # QInputMethodEvent.setCommitString(editor.inputMethodEvent,QInputMethodEvent.commitString(editor.inputMethodEvent))
