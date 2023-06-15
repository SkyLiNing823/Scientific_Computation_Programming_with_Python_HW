import numpy as np
import matplotlib.pyplot as plt


def makePower(X):
    return np.concatenate((np.ones((len(X), 1)), X.reshape(
        len(X), 1), X.reshape(len(X), 1)**2, X.reshape(len(X), 1)**3), axis=1)


# 𝑓2 =10;𝑓4 =50;𝑓6 =70;𝑓8 =75;𝑓10 =40;𝑓12 =10;𝑓14 =30;𝑓16 =35
X = np.array([2, 4, 6, 8, 10, 12, 14, 16])
Y = np.array([10, 50, 70, 75, 40, 10, 30, 35])
A = np.matrix(makePower(X))
b = np.matrix(Y.reshape(-1, 1))
R = np.linalg.lstsq(A, b, rcond=None)
x = R[0]
print(f'a:{x[3]}')
print(f'b:{x[2]}')
print(f'c:{x[1]}')
print(f'd:{x[0]}')
plt.plot(np.linspace(2, 16, 100), makePower(np.linspace(2, 16, 100))
         * x, color='blue', linestyle='solid')
plt.plot(X, Y, 'ro', color='red', linestyle='solid')
plt.show()
