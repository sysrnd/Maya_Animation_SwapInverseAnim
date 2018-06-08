

from Modules.Qt import QtCore, QtGui, QtWidgets
import  Animacion.Maya_Animation_SwapInverseAnim.swapUI.swapInverse_UI_v003
reload( Animacion.Maya_Animation_SwapInverseAnim.swapUI.swapInverse_UI_v003)
from  Animacion.Maya_Animation_SwapInverseAnim.swapUI.swapInverse_UI_v003 import Ui_window_SwapInverseAnim

import  Animacion.Maya_Animation_SwapInverseAnim.swapCore.SwapInverse_Bridge
reload( Animacion.Maya_Animation_SwapInverseAnim.swapCore.SwapInverse_Bridge)
from  Animacion.Maya_Animation_SwapInverseAnim.swapCore.SwapInverse_Bridge import *

class MyApplication(QtWidgets.QMainWindow, Ui_window_SwapInverseAnim):
    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.setupUi(self)


if __name__ != "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
    except:
        app = QtCore.QCoreApplication.instance()
    window = MyApplication()
    window.setWindowFlags(
        window.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
    interfaceMacho = swapInverseBridge(window=window)
    window.show()
    try:
        sys.exit(app.exec_())
    except:
        "error al intentar salir"
