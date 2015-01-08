#!/usr/bin/env python
# encoding: utf-8

from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np

app = QtGui.QApplication([])
win = pg.GraphicsWindow(title="Xmusic power by dejavu")
pl = win.addPlot(title="utest show")
y = np.random.normal(size=100)
#x = np.random.normal(size=10)
pl.plot(y, pen=(0,255,0), symbol='o')
# start the Qt event loop
if __name__ == '__main__':
  import sys
  if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
    QtGui.QApplication.instance().exec_()
