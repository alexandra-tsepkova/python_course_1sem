import numpy as np


class Matrix:
    def __init__(self, init_array):
        self.data = []
        for row in init_array:
            current_row = []
            for element in row:
                current_row.append(element)
            self.data.append(current_row)

    def shape(self):
        return len(self.data), len(self.data[0])

    def __add__(self, other):
        if self.shape() != other.shape():
            raise ValueError("Cannot add matrices with different shapes")
        return Matrix(
            [
                [i + j for i, j in zip(self.data[k], other.data[k])]
                for k in range(self.shape()[0])
            ]
        )

    def __mul__(self, other):
        if self.shape() != other.shape():
            raise ValueError(
                "Cannot element-wise multiply matrices with different shapes"
            )
        return Matrix(
            [
                [i * j for i, j in zip(self.data[k], other.data[k])]
                for k in range(self.shape()[0])
            ]
        )

    def __matmul__(self, other):
        if self.shape()[1] != other.shape()[0]:
            raise ValueError(
                "Cannot multiply matrices: first matrix doesn't have the same "
                "number of columns as the second matrix has rows"
            )

        other_columns = Matrix(list(zip(*other.data)))
        result = [[0 for _ in range(self.shape()[1])] for _ in range(self.shape()[0])]

        for i in range(self.shape()[0]):
            for j in range(other_columns.shape()[0]):
                result[i][j] = sum(
                    [x * y for x, y in zip(self.data[i], other_columns.data[j])]
                )
        return Matrix(result)

    def print(self):
        for i in range(self.shape()[0]):
            print(*self.data[i])


np.random.seed(0)
A = np.random.randint(0, 10, (10, 10))
B = np.random.randint(0, 10, (10, 10))

a = Matrix(A)
b = Matrix(B)
print("Matrix A")
a.print()
print("\nMatrix B")
b.print()
print("\nA + B")
(a + b).print()
print("\nA * B")
(a * b).print()
print("\nA @ B")
(a @ b).print()