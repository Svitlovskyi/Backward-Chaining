import re
from BackwardChaining.Models.Nodes import *
from BackwardChaining.Models.NodeStore import *


class Node_Store_Utils:
    # operator symbols
    __operators = ["+", "=>", "|", "^", "!", ")", "("]

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



    # def __initialize_child(self, node_store):
    #     for node in node_store.atom_node_list:
    #         print(node.child)
    #         if len(node.child) != 0:
    #             new_child = []
    #             for node_name in node.child:
    #                 if node_name in self.__operators:
    #                     connector_node = ConnectorNode(Operator(node_name))
    #                     new_child.append(connector_node)
    #                     continue
    #                 new_child.append(node_store.get_node(node_name))
    #             node_store.set_child(node.name, new_child)

    '''private
        @input: rules list 2d array
                node store object
        @void: intiialize child in child list of node store
    '''

    def __set_child_of_atom_nodes(self, rules_list, node_store):
        for rule in rules_list:
            splitted = rule.split("=>")
            lhs, rhs = splitted[0].split(), splitted[1].split()

            if len(rhs) == 1:
                node_store.set_child(rhs[0], lhs)
            else:
                for node in rhs:
                    if node in ["=>", "|", "^", "!", ")", "("]:
                        raise Exception("Not valid rules")
                for node in rhs:
                    if node != "+":
                        node_store.set_child(node, lhs)


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
                if node not in self.__operators and node not in unique_node:
                    if pattern.match(node):
                        unique_node.append(node)
                        continue


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
