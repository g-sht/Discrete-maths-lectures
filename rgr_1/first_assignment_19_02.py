import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class BooleanMatrix:
    def __init__(self, np_matrix):
        self.matrix = np_matrix

    #дизъюнкция
    def disjunction(self, other):
        out = np.zeros_like(self.matrix)
        m, n = self.matrix.shape

        for i in range(m):
            for j in range(n):
                out[i, j] = self.matrix[i, j] | other.matrix[i, j]

        return BooleanMatrix(out)

    #транспонирование
    def transpose(self):
        self.matrix = np.transpose(self.matrix)

    #инверсирование
    def inverse(self):
        m, n = self.matrix.shape
        for i in range(m):
            for j in range(n):
                self.matrix[i, j] = 1 - self.matrix[i, j]

    #умножение матриц
    def __mul__(self, other):
        m, n = self.matrix.shape #кол во строк и столбцов в 1ой матрице
        p = self.matrix.shape[1] #кол во столбоцв в 2ой матрице

        out = np.zeros((m, p), dtype=int)

        for i in range(m):
            for j in range(p):
                for k in range(n):
                    if self.matrix[i, k] and other.matrix[k, j]:
                        out[i, j] = 1
                        break

        return BooleanMatrix(out)

    #вычитание матриц
    def __sub__(self, other):
        out = np.zeros_like(self.matrix)
        m, n = self.matrix.shape

        for i in range(m):
            for j in range(n):
                out[i, j] = self.matrix[i, j] & (1 - other.matrix[i, j])

        return BooleanMatrix(out)

    #отрисовка графа по матрице смежности
    def draw(self):
        graph = nx.DiGraph(directed=True)
        m, n = self.matrix.shape

        graph.add_nodes_from(range(1, m + 1))

        for i in range(m):
            for j in range(n):
                if self.matrix[i, j] == 1:
                    graph.add_edge(i + 1, j + 1)

        nx.draw(graph, with_labels=True, node_color='lightblue')
        plt.show()


a = BooleanMatrix(np.matrix('1, 0; 0, 1'))
b = BooleanMatrix(np.matrix('0, 1; 1, 0'))
d = a * b

print(d.matrix)

d.inverse()
print(d.matrix)

d.transpose()
print(d.matrix)

c = a.disjunction(b)
print(c.matrix)

e = a - b
print(e.matrix)

e.draw()