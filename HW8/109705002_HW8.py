import numpy as np
import matplotlib.pyplot as plt


Ay, Ax = np.mgrid[1:-1:256j, -1:1:256j]
ux = np.array([0.0, 0.5, -0.5])
uy = np.array([0.0, 0.25, -0.25])
sx = np.array([1.0, 0.4, 0.3])
sy = np.array([1.0, 0.2, 0.5])
ux = np.expand_dims(ux, axis=(1, 2))  # or np.reshape(ux, (???))
uy = np.expand_dims(uy, axis=(1, 2))  # or np.reshape(uy, (???))
sx = np.expand_dims(sx, axis=(1, 2))  # or np.reshape(sx, (???))
sy = np.expand_dims(sy, axis=(1, 2))  # or np.reshape(sy, (???))
I = np.exp(-((Ax - ux)**2 / (2 * sx**2) + (Ay - uy)**2 / (2 * sy**2)))
print(I.shape)  # The shape of I should be (3, 256, 256)
plt.imshow(I[0])
plt.show()
plt.imshow(I[1])
plt.show()
plt.imshow(I[2])
plt.show()
