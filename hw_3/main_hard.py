import numpy as np
from functools import lru_cache


class ArrayHash:
    @lru_cache(maxsize=None)
    def hash(self):
        return hash(str(self.data))


class Numpy4(ArrayHash):
    def __init__(self, data):
        self.data = np.array(data)

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices have different shapes")
        return Numpy4(self.data + other.data)

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices have different shapes")
        return Numpy4(self.data * other.data)

    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Matrices have incompatible shapes")
        return Numpy4(self.data @ other.data)

    def __str__(self):
        return str(self.data)

    @classmethod
    def random(cls, shape, seed):
        return cls(np.random.RandomState(seed).randint(0, 10, shape))


# создание двух матриц
np.random.seed(0)
A = Numpy4.random((10, 10), 0)
B = Numpy4.random((10, 10), 0)
C = Numpy4.random((10, 10), 1)
D = Numpy4.random((10, 10), 0)

# проверка операций
AB = A @ B
CD = C @ D
assert hash(AB) != hash(CD)
assert hash(A) == hash(C)
assert hash(B) == hash(D)
assert A + B == B + A
assert A * B == B * A
assert A @ B == B @ A
assert (A + B) @ C == A @ C + B @ C
assert (A * B) * C == A * (B * C)

# запись матриц в файлы
with open("artifacts/hard/A.txt", "w") as f:
    f.write(str(A))
with open("artifacts/hard/B.txt", "w") as f:
    f.write(str(B))
with open("artifacts/hard/C.txt", "w") as f:
    f.write(str(C))
with open("artifacts/hard/D.txt", "w") as f:
    f.write(str(D))
with open("artifacts/hard/AB.txt", "w") as f:
    f.write(str(AB))
with open("artifacts/hard/CD.txt", "w") as f:
    f.write(str(CD))

# запись хэша в файл
with open("artifacts/hard/hash.txt", "w") as f:
    f.write(str(hash(AB)) + "\n" + str(hash(CD)))