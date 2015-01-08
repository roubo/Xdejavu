#!/usr/bin/env python
# encoding: utf-8

"""
@ Make Everything Simple
@ Just read the audio file, and display the wave and it`s fft waveshow
@ By yinkeedai
"""
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
from pydub import AudioSegment
import sys
from scipy.ndimage.filters import maximum_filter
import matplotlib.mlab as mlab
from scipy.ndimage.morphology import (generate_binary_structure,
                                      iterate_structure, binary_erosion)
argc = len(sys.argv)
app = QtGui.QApplication([])
win = pg.GraphicsWindow(title="Xmusic power by dejavu")
imw = pg.ImageView()
pl  = win.addPlot(title="utest show")
win.nextRow()
pl_fft  = win.addPlot(title="utest show fft")

if argc == 1 :
  song = AudioSegment.from_file("../roubotest/艾怡良-我不知道爱是什么.m4a.mp3")
else:
  song = AudioSegment.from_file(sys.argv[1])
#song = song[:1000*4000]
data = np.fromstring(song._data, np.int16)
#data = 10 * np.log10(data)
data[data == -np.inf] = 0  # replace infs with zeros
song_rate = song.frame_rate
song_channels = song.channels
data_channel = []
for chn in xrange(song_channels):
  data_channel.append(data[chn::song_channels])
spend_time = np.arange(0, len(data_channel[0]))*(1.0/song_rate)
fft_size = 512
freqs = np.linspace(0, song_rate/2, fft_size/2+1)
fft_data = np.fft.rfft(data_channel[0][fft_size-1:fft_size*2])
fft_point = 20*np.log10(np.clip(np.abs(fft_data), 1e-20, 1e100))
pl.plot(spend_time, data_channel[0], pen=(0,255,0))
pl.setYRange(-50000, 50000, padding=None)
pl_fft.plot(freqs, fft_point, pen=(255,0,0))

#  show the freq image
struct = generate_binary_structure(2, 1)
neighborhood = iterate_structure(struct, 20)

arr2D = mlab.specgram(data_channel[0])
# find local maxima using our fliter shape
local_max = maximum_filter(arr2D, footprint=neighborhood) == arr2D
background = (arr2D == 0)
eroded_background = binary_erosion(background, structure=neighborhood,
                                                      border_value=1)

# Boolean mask of arr2D with True at peaks
detected_peaks = local_max - eroded_background

# extract peaks
amps = arr2D[detected_peaks]
j, i = np.where(detected_peaks)

# filter peaks
amps = amps.flatten()
peaks = zip(i, j, amps)
peaks_filtered = [x for x in peaks if x[2] > amp_min]  # freq, time, amp

# get indices for frequency and time
frequency_idx = [x[1] for x in peaks_filtered]
time_idx = [x[0] for x in peaks_filtered]

fig, ax = plt.subplots()
ax.imshow(arr2D)
ax.scatter(time_idx, frequency_idx)

imw.setImage(arr2D)
# start the Qt event loop
if __name__ == '__main__':
  import sys
  if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
    QtGui.QApplication.instance().exec_()



