import numpy as np


class Numpy2:
    def __init__(self, data):
        self.data = np.array(data)

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must be the same shape to add")
        return Numpy2(self.data + other.data)

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must be the same shape to multiply")
        return Numpy2(self.data * other.data)

    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Matrices must have compatible dimensions for matrix multiplication")
        return Numpy2(self.data @ other.data)


np.random.seed(0)
matrix1 = Numpy2(np.random.randint(0, 10, (10, 10)))
matrix2 = Numpy2(np.random.randint(0, 10, (10, 10)))

with open("artifacts/easy/matrix+.txt", "w") as file:
    result = matrix1 + matrix2
    file.write(str(result.data))

with open(r'artifacts/easy/matrix_.txt', 'w') as file:
    result = matrix1 * matrix2
    file.write(str(result.data))

with open("artifacts/easy/matrix@.txt", "w") as file:
    result = matrix1 @ matrix2
    file.write(str(result.data))