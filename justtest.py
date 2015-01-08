#!/usr/bin/env python
# encoding: utf-8

from dejavu import Dejavu
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import pyqtgraph.ptime as ptime

config = {
  "database" : {
    "host"   : "127.0.0.1",
    "user"   : "root",
    "passwd" : "",
    "db"     : "dejavu",
  }
}
filename="roubotest/艾怡良-我不知道爱是什么.m4a.mp3"

app = QtGui.QApplication([])
win = pg.GraphicsWindow(title="Xdejavu by roubo")
win.resize(1000,600)
win.setWindowTitle('Xdejavu by roubo')
pg.setConfigOptions(antialias=True)
view = pg.ViewBox()
win.setCentralItem(view)
## lock the aspect ratio
view.setAspectLocked(True)
## Create image item


img = pg.ImageItem(border='w')
view.addItem(img)
data = np.random.normal(size=(15, 600, 600), loc=1024, scale=64).astype(np.uint16)
updateTime = ptime.time()
fps = 0

def updateData():
    global img, data,  updateTime, fps

    ## Display the data
    img.setImage(data)

    QtCore.QTimer.singleShot(1, updateData)
    now = ptime.time()
    fps2 = 1.0 / (now-updateTime)
    updateTime = now
    fps = fps * 0.9 + fps2 * 0.1

updateData()

djv = Dejavu(config)
djv.fingerprint_directory("roubotest", [".mp3"], 3)
channelcount=djv.getchannelamount(filename)
for i in range(0,channelcount):
  print "-> process the channel %d" %i
  data, maxima = djv.get2doriginaldata(filename, i)



## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()
