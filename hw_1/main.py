import ast, inspect
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

def fib():
    n = int(input())
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

def build_ast(source):
    tree = ast.parse(source)
    G = nx.DiGraph()
    node_count = 0

    def add_node(node, value=None):
        nonlocal node_count
        # if not isinstance(node, ast.AST):
        #     return None
        node_name = f'"{node_count}.{type(node).__name__}:{value}"' if value is not None else f"{node_count}.{type(node).__name__}"
        G.add_node(node_name, label=f"{type(node).__name__}")
        node_count += 1
        return node_name

    def add_edge(source, dest):
        G.add_edge(source, dest)

    def traverse(node, parent=None):
        node_name = add_node(node)
        if parent is not None:
            add_edge(parent, node_name)
        if isinstance(node, ast.Constant):
            add_node(node, value=node.value)
        for child in ast.iter_child_nodes(node):
            traverse(child, node_name)

    traverse(tree)
    return G

source = inspect.getsource(fib)
G = build_ast(source)
pos = graphviz_layout(G, prog='dot')
node_colors = []
for node in G.nodes():
    node_label = G.nodes[node]['label']
    if 'Name' in node_label:
        node_colors.append('lightblue')
    elif 'Call' in node_label:
        node_colors.append('lightgreen')
    elif 'Constant' in node_label:
        node_colors.append('pink')
    else:
        node_colors.append('gray')
plt.figure(figsize=(25, 20))
nx.draw(G, pos, with_labels=True, font_size=5, node_size=2000, node_color=node_colors, edge_color='gray', arrowsize=20, linewidths=1, font_weight='bold')
plt.savefig('artifacts/graph.png')
plt.show()




