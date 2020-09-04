#undirected graph
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

    def create_edge(self, a:int, b:int) -> None:
        nodeA, nodeB = self.nodes[a], self.nodes[b]
        if nodeA and nodeB:
            self.edges.append((nodeA, nodeB))
            nodeA.adyacents.add(nodeB.id)
            nodeB.adyacents.add(nodeA.id)

    def add_node(self, node: Node) -> None:
        if node not in self.nodes:
            self.nodes.append(node)

    def graph_matrix() -> list:
        m = [[0 for y in self.nodes] for x in self.nodes]
        for nd_a, nd_b in self.edges:
            m[nd_a._index][nd_b._index] = 1
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
