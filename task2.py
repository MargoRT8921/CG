# поворот линии 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

angle = np.deg2rad(45)
lont = pd.Series([1, 2])
latt = pd.Series([4, 6])
R = (lont.diff()**2 + latt.diff()**2)**0.5
theta = np.arctan(latt.diff()/lont.diff())

Xnew = lont.shift(1)+ R*np.cos(angle + theta)
Ynew = latt.shift(1) + R*np.sin(angle+ theta)

fig=plt.figure()
plt.plot(lont, latt,'-ob')
plt.plot([lont.iloc[-2], Xnew.iloc[-1]], [latt.iloc[-2], Ynew.iloc[-1]], ":*r")
plt.show()
