from Graph import Graph
from Node import Node
from GLOBAL_VAR import GRAPHS
from pynput import keyboard
from view_terminal import *



def on_press(key):
    pass



def on_release(key):
    pass

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
    sr = str()
    for x in range(len(m)):
        sr += '[ '
        for y in range(len(m[x])):
            sr+= '{} '.format(m[x][y])
        sr += "]\n"
    print(sr)

def infinity_while():
    pass

def main():
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
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release
            ) as listener:

        main()
        listener.join()

