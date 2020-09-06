from Graph import Node, Graph
from GLOBAL_VAR import NODES, GRAPHS


def create_graph():
    name = input("Graph name is: ")
    gra = Graph(name)
    GRAPHS.append(gra)

def get_graph(name: str) -> Graph:
    for g in GRAPHS:
        if g.name == name: return g

def create_node():
    g = get_graph(input("Graph name is: "))
    id_node = int(input("Id Node is: "))
    node = Node(id_node)
    g.add_node(node)
    print(node)
    print(g)

def show_matrix():
    g = get_graph(input("Graph name is: "))
    m = g.graph_matrix()
    print(m)
    sr = str()
    for x in range(len(m)):
        sr += '[ '
        for y in range(len(m[x])):
            sr+= '{} '.format(m[x][y])
        sr += "]\n"
    print(sr)
def main():
    """print(f'GRAPHS: {GRAPHS}')
    create_graph()
    print(f'GRAPHS: {GRAPHS}')
    create_node()
    create_node()
    create_node()
    create_node()
    show_matrix()
    """
    g = Graph("s")
    g.add_node(Node(1))
    g.add_node(Node(2))
    g.add_node(Node(3))
    g.add_node(Node(4))
    print(g.nodes)
    g.create_edge(1,2)
    g.create_edge(1,4)
    g.create_edge(2,1)
    g.create_edge(3,2)
    g.create_edge(4,2)
    GRAPHS.append(g)
    show_matrix()


if __name__ == '__main__':
    main()

