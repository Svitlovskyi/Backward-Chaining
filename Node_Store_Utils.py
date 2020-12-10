import re
from Nodes import *
from Operator import *


class Utils:
    # operator symbols
    __operators = ["+", "=>", "|", "^", "!"]

    '''@input: rules list 2d array
               facts (node name which state is true)
       @output: initialized atom node store 
    '''

    def initialize_atom_nodes_store_from_rules(self, rules_list, facts):
        unique_atoms = self.__search_unique_atom_nodes(rules_list)
        initialized_unique_atoms = self.__initialize_atom_nodes(unique_atoms, facts)
        node_store = NodeStore(initialized_unique_atoms)
        self.__set_child_of_atom_nodes(rules_list, node_store)
        return node_store



    def __initialize_child(self, node_store):
        for node in node_store.atom_node_list:
            print(node.child)
            if len(node.child) != 0:
                new_child = []
                for node_name in node.child:
                    if node_name in self.__operators:
                        connector_node = ConnectorNode(Operator(node_name))
                        new_child.append(connector_node)
                        continue
                    new_child.append(node_store.get_node(node_name))
                node_store.set_child(node.name, new_child)
        # initialized_child = []
        # if len(child) != 0:
        #     for node_name in child:
        #         if node_name in self.__operators:
        #             connector_node = ConnectorNode(Operator(node_name))
        #             initialized_child.append(connector_node)
        #             continue
        #         initialized_child.append(node_store.get_node(node_name))

    '''private
        @input: rules list 2d array
                node store object
        @void: intiialize child in child list of node store
    '''

    def __set_child_of_atom_nodes(self, rules_list, node_store):
        for rule in rules_list:
            splitted = rule.split("=>")
            rhs, lhs = splitted[0].split(), splitted[1].split()
            if len(lhs) == 1:
                node_store.set_child(lhs[0], rhs)
            # TODO: ADD CHILD FOR COMPLEX LHS (A + B, etc)

    '''private
        @input: rules list (2d array)
        @output: unique atom node names from 2d array
    '''

    def __search_unique_atom_nodes(self, rules_list):
        unique_node = []
        pattern = re.compile("[A-Z]")
        pattern_with_not = re.compile("[A-Z!]")

        for rule in rules_list:
            splited_rule = rule.split()
            for node in splited_rule:
                if node not in self.__operators:
                    if pattern.match(node):
                        unique_node.append(node)
                        continue
                    if pattern_with_not.match(node):
                        unique_node.append(node[1])

        return unique_node

    '''private 
        @input: unique node list, 
               facts (node name which state is true)
        @output: initialized unique atom node array 
    '''

    def __initialize_atom_nodes(self, unique_node_list, facts):
        initialized_node_list = []
        for node in unique_node_list:
            initialized_node = AtomNode(node, None)
            if node in facts:
                initialized_node.state = True
            initialized_node_list.append(initialized_node)
        return initialized_node_list
