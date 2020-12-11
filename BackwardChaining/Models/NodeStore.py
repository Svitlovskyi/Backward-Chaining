'''Save list of unique atom nodes'''''
from BackwardChaining.Models.Nodes import AtomNode
'''
Node format 
[Name: [State: III,  Child: III]]
'''
import time

class NodeStore:

    def __init__(self, initialized_unique_atoms):
        self.atom_node_list = initialized_unique_atoms
    '''@input: name of node, child of node, 
        set child for node 
    '''

    def set_child(self, name, child):
        index = self.__get_node_index(name)
        self.atom_node_list[index].child = child

    '''@input: index of node, new state
        change state of specific node in node list
    '''

    def change_node_state(self, index, state):
        self.atom_node_list[index].state = state

    '''@input name
        get node index by name
    '''

    def __get_node_index(self, name):
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


    '''@input: name of node, new state of node'''

    def set_state(self, name, state):
        index = self.__get_node_index(name)
        self.atom_node_list[index].state = state

