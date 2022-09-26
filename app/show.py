from ecosys import *
from app.params import ico_file

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)


application = QtWidgets.QApplication([])
application.setWindowIcon(QtGui.QIcon(ico_file))
application.processEvents()
application.setStyle(QStyleFactory.create("Windows"))

