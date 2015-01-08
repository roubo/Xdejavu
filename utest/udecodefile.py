#!/usr/bin/env python
# encoding: utf-8

"""
@ Make Everything Simple
@ Just read the audio file, and display the wave
@ By yinkeedai
"""
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
from pydub import AudioSegment
import sys
argc = len(sys.argv)
app = QtGui.QApplication([])
win = pg.GraphicsWindow(title="Xmusic power by dejavu")
pl  = win.addPlot(title="utest show")

if argc == 1 :
  song = AudioSegment.from_file("../roubotest/艾怡良-我不知道爱是什么.m4a.mp3")
else:
  song = AudioSegment.from_file(sys.argv[1])
#song = song[:1000*4000]
data = np.fromstring(song._data, np.int16)
data = 10 * np.log10(data)
data[data == -np.inf] = 0  # replace infs with zeros
song_rate = song.frame_rate
song_channels = song.channels
data_channel = []
for chn in xrange(song_channels):
  data_channel.append(data[chn::song_channels])
spend_time = np.arange(0, len(data_channel[0]))*(1.0/song_rate)
pl.plot(spend_time, data_channel[0], pen=(0,255,0))
pl.setYRange(-10, 200, padding=None)

# start the Qt event loop
if __name__ == '__main__':
  import sys
  if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
    QtGui.QApplication.instance().exec_()
