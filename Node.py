class Node:
    _index = 0
    def __init__(self,_id: int):
        self.id = _id
        self.adyacents = set() # List of nodes
        self.index = Node._index
        Node._index +=1

    def __repr__(self):
        return f"Node: {self.id}"
