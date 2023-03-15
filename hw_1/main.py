import ast, inspect
import networkx as nx
import matplotlib.pyplot as plt

def fib():
    n = int(input("Сколько чисел Фибоначчи необходимо?: "))
    fib1 = fib2 = 1
    if n == 0:
        return []
    elif n == 1:
        return [fib1]
    elif n == 2:
        return [fib1, fib2]
    else:
        ls = [fib1, fib2]
        for i in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2
            ls.append(fib2)
        return ls

source = inspect.getsource(fib)
tree = ast.parse(source)

def label(node):
    if hasattr(node, 'name'):
        return node.name
    elif type(node) == ast.arguments:
        return ', '.join([item.arg for item in node.args])
    else:
        return node.__class__.__name__

G = nx.DiGraph()
nodes = []
nodes.append(next(ast.walk(tree)).body[0])
G.add_node(next(ast.walk(tree)).body[0].name)
while len(nodes) > 0:
    node = nodes.pop()
    for nod in ast.iter_child_nodes(node):
        G.add_node(label(nod))
        G.add_edge(label(node), label(nod))
        nodes.append(nod)

nx.draw(G, with_labels=True)
plt.savefig('artifacts/graph.png')
plt.show()




