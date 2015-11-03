import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

%matplotlib

camera_1d=np.loadtxt('camera.txt')

camera_1d=camera_1d.reshape(512,512)
camera_1d=camera_1d.T

plt.imshow(camera_1d,cmap=cm.Greys)
binary_camera_1d = camera_1d>0.5
plt.imshow(binary_camera_1d, cmap=cm.Greys_r)
