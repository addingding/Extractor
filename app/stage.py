from app.board import ico_file
from ecosys import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)


application = QtWidgets.QApplication([])
application.setWindowIcon(QtGui.QIcon(ico_file))
application.setStyle(QStyleFactory.create("Windows"))
application.setOverrideCursor(QtCore.Qt.BlankCursor)
application.processEvents()

