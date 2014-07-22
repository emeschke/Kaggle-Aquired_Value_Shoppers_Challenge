# -*- coding: utf-8 -*-
"""
Created on Thu May 29 22:54:13 2014

@author: meschke
"""

from pylab import *

t = arange(0.0, 2.0, 0.01)
s = sin(2*pi*t)
plot(t, s)

xlabel('time (s)')
ylabel('voltage (mV)')
title('About as simple as it gets, folks')
grid(True)
savefig("test.png")
show()