from graph.Graph import Node


def main():
    node = Node(12)
    node.add_neighbor(2)
    node.add_neighbor(7)
    node.add_neighbor(3)
    print(node)
    pass


if __name__ == '__main__':
    main()

