#undirected graph
class Node:
    _index = 0
    def __init__(self,_id: int):
        self.id = _id
        self.adyacents = set() # List of nodes
        self.index = Node._index 
        Node._index +=1

    def __repr__(self):
        return f"Node: {self.id}"

class Graph:
    def __init__(self, name: str="unnamed"):
        self.name = name
        self.nodes = []
        self.edges = set()

    def create_edge(self, a:int, b:int) -> None:
        nodeA, nodeB = 0,0
        print(a,b)
        for n in self.nodes:
            if n.id == a:
                nodeA = n
            elif n.id == b:
                nodeB = n
        self.edges.add((nodeA, nodeB))


    def add_node(self, node: Node) -> None:
        if node not in self.nodes:
            self.nodes.append(node)

    def graph_matrix(self) -> list:
        m = [[0 for y in self.nodes] for x in self.nodes]
        for nd_a, nd_b in self.edges:
            m[self.nodes.index(nd_a)][self.nodes.index(nd_b)] = 1
        return m
    
    def __repr__(self):
        return f"Graph: {self.name}\nNodes: {self.nodes}"



if __name__ == '__main__':
    print(Node._index)
    n = Node(32)
    print(n.index)
    print(Node._index)
    n2 = Node(323)
    print(n.index)
    print(n2.index)
    print(Node._index)
