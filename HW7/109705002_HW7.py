# Exercise (3/3)
import numpy as np
import matplotlib.pyplot as plt

print('Exercise (1/3):')
# 1
images = 10
channels = 3
height = 200
width = 100

# 2
r = 0.2
g = 0.3
b = 0.5

# 3
A = np.zeros((images, channels, height, width))
A[:, 0, :, :] = r
A[:, 1, :, :] = g
A[:, 2, :, :] = b

print(A[0][0][150][0])
print(A[0][1][150][1])
print(A[0][2][150][2])


print('\nExercise (2/3):')
# 4
B = A.reshape(images, channels, height * width)
print(B.shape)

# 5
C = B[3, 1, ]
print(C.shape)

# 6
D = C.reshape(1, height, width)
print(D.shape)

print('\nExercise (3/3):')
# 7
E = np.moveaxis(A, 1, 3)  # images, height, width, channels
plt.imshow(E[0])
plt.show()

# 8
F = np.expand_dims(np.mean(E, axis=(2, 3)), axis=-1)
print(F)
