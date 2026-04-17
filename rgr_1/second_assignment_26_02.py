import matplotlib.pyplot as plt
import networkx as nx

R = [(1, 2), (2, 3), (3, 4), (3, 5), (5, 6)]
G = nx.DiGraph()
G.add_edges_from(R)
G.add_nodes_from(set(el[0] for el in R))

#Функция топологической сортировки. Записывает линейный порядок в linear_order
def topological_sort(bin_relation, visited, stack):
    linear_order = []
    while len(stack) != 0:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            linear_order.append(node)

        for el in bin_relation:
            if el[0] == node:
                stack.append(el[1])

    return linear_order

linear_order = topological_sort(R, set(), [1])
print(linear_order)

nx.draw(G, with_labels=True)
plt.show()
