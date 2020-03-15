# -*- coding: utf-8 -*-
"""
@author: CrazyCatOxO
"""

from PyQt5.QtWidgets import QApplication
import mainWindowModule
import multiprocessing

if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    app = QApplication([])
    window = mainWindowModule.myUi()
    window.show()
    app.exec_()
