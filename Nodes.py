'''Save list of unique atom nodes'''''


class NodeStore:

    def __init__(self):
        self.atom_node_list = []

    '''@input: Node
        add node to node store list
    '''

    def add_node(self, name, state):
        atom_node = AtomNode(name, state)
        self.atom_node_list.append(atom_node)

    '''@input: index of node, new state
        change state of specific node in node list
    '''

    def change_node_state(self, index, state):
        self.atom_node_list[index].state = state

    '''@input name
        get node index by name
    '''

    def get_node_index(self, name):
        for index, node in enumerate(self.atom_node_list):
            if node.name == name:
                return index

        raise Exception("Node with '{}', doesnt exists".format(name))

    '''@input: name
        get node by name'''

    def get_node(self, name):
        for index, node in enumerate(self.atom_node_list):
            if node.name == name:
                return node

        raise Exception("Node with '{}', doesnt exists".format(name))


class Node:
    def __init__(self):
        self.child = []


class ConnectorNode(Node):
    def __init__(self, operator):
        super().__init__()
        self.operator = operator


class AtomNode(Node):
    def __init__(self, name, state):
        super().__init__()
        self.name = name
        self.state = state

    def __repr__(self):
        return self.name + " " + str(self.state)