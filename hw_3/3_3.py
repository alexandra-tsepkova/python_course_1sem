from collections import defaultdict


class Matrix:
    cache = defaultdict()

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
        hashes = (hash(self), hash(other))
        if hashes in self.cache:
            return self.cache[hashes]
        else:
            other_columns = Matrix(list(zip(*other.data)))
            result = [
                [0 for _ in range(self.shape()[1])] for _ in range(self.shape()[0])
            ]

            for i in range(self.shape()[0]):
                for j in range(other_columns.shape()[0]):
                    result[i][j] = sum(
                        [x * y for x, y in zip(self.data[i], other_columns.data[j])]
                    )
            result = Matrix(result)
            self.cache[hashes] = result
            return result

    def print(self):
        for i in range(self.shape()[0]):
            print(*self.data[i])

    def __hash__(self):
        """
        Для каждой строки считаем сумму ее элементов по модулю длины строки,
        умноженного на неизменный коэффициент
        Для матрицы хэш - сумма таких значений от всех строк
        """
        s = self.shape()[1] * 11
        return int(sum([sum(row) % s for row in self.data]))


# This code was used to produce artifacts for this task

A = [[12, 15, 0], [3, 3, 7], [9, 19, 18]]
C = [[24, 26, 32], [21, 26, 27], [33, 37, 25]]


a = Matrix(A)
c = Matrix(C)
b = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
d = b
print("Matrix A")
a.print()
print("\nMatrix B/D")
b.print()
print("\nMatrix C")
c.print()

print("\nA @ B")
AB = a @ b
AB.print()

print("\nC @ D with cache - wrong because of same hashes")
CD = c @ d
CD.print()

print("\nC @ D without cache")
c.cache.clear()
CD = c @ d
CD.print()

print("\nHashes")
print("Hash A, hash C:", hash(a), hash(c))
print("Hash AB, hash CD:", hash(AB), hash(CD))
