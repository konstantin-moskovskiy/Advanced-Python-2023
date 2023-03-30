import numpy as np


class ArrayFile:
    def save(self, filename):
        np.savetxt(filename, self.data)

    def load(self, filename):
        self.data = np.loadtxt(filename)
        return self.data


class ArrayStr:
    def __str__(self):
        return str(self.data)


class ArrayGetterSetterSize:
    def shape(self):
        return self.data.shape

    def size(self):
        return self.data.size

    def get(self, idx):
        return self.data[idx]

    def set(self, idx, value):
        self.data[idx] = value


class Numpy3(ArrayFile, ArrayStr, ArrayGetterSetterSize):
    def __init__(self, data):
        self.data = np.array(data)


    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must be the same shape to add")
        return Numpy3(self.data + other.data)

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must be the same shape to multiply")
        return Numpy3(self.data * other.data)

    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Matrices must have compatible dimensions for matrix multiplication")
        return Numpy3(self.data @ other.data)

np.random.seed(0)
matrix1 = Numpy3(np.random.randint(0, 10, (10, 10)))
matrix2 = Numpy3(np.random.randint(0, 10, (10, 10)))

with open("artifacts/medium/matrix+.txt", "w") as file:
    result = matrix1 + matrix2
    file.write(str(result.data))

with open(r'artifacts/medium/matrix_.txt', 'w') as file:
    result = matrix1 * matrix2
    file.write(str(result.data))

with open("artifacts/medium/matrix@.txt", "w") as file:
    result = matrix1 @ matrix2
    file.write(str(result.data))