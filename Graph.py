#undirected graph
import GLOBAL_VAR as gl_var



class Node:
    _index = 0
    def __init__(self,id: int):
        self.id = id
        self.adyacents = {} # List of nodes
        self.index = Node._index 
        Node._index +=1

    def __repr__(self):
        return f"Node: {self.id}"

class Graph:
    def __init__(self, name: str="unnamed"):
        self.name = name
        self.nodes = []
        self.edges = []

    def create_edge(self):
        pass
    

    def graph_matrix():
        pass

if __name__ == '__main__':
    print(Node._index)
    n = Node(32)
    print(n.index)
    print(Node._index)
    n2 = Node(323)
    print(n.index)
    print(n2.index)
    print(Node._index)
