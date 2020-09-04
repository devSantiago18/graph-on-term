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

  
  
def main():
    print(f'GRAPHS: {GRAPHS}')
    create_graph()
    print(f'GRAPHS: {GRAPHS}')
    create_node()



if __name__ == '__main__':
    main()

