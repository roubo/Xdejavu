#!/usr/bin/env python
# encoding: utf-8
"""
@ Make Everything Simple
@ Just read the Microphone, and display the wave timing.
@ By yinkeedai
"""
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import pyaudio

app = QtGui.QApplication([])
win = pg.GraphicsWindow(title="Xmusic power by dejavu")
pl  = win.addPlot(title="utest show")
wave_curve  = pl.plot(pen=(0,255,0))
pl.setYRange(-10000, 10000, padding=None)

def updateview():
  global pl, wave_curve, spend_time, audio_data, stream, ptr
  stream.start_stream()
  string_data = stream.read(DEFAULT_NUM_SAMPLES)
  stream.stop_stream()
  audio_data  = np.fromstring(string_data, dtype=np.short)
  spend_time  = np.arange(0, len(audio_data))*(1.0/DEFAULT_SAMPLING_RATE)
  wave_curve.setData(spend_time, audio_data)

timer = QtCore.QTimer()
timer.timeout.connect(updateview)

DEFAULT_NUM_SAMPLES   = 2000
DEFAULT_SAMPLING_RATE = 8000
DEFAULT_NUM_CHANNEL   = 1
DEFAULT_FORMAT        = pyaudio.paInt16

micp = pyaudio.PyAudio()
stream = micp.open(format=DEFAULT_FORMAT, channels=DEFAULT_NUM_CHANNEL,
    rate=DEFAULT_SAMPLING_RATE, input=True, frames_per_buffer=DEFAULT_NUM_SAMPLES)
timer.start(100)

# start the Qt event loop
if __name__ == '__main__':
  import sys
  if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
    QtGui.QApplication.instance().exec_()
