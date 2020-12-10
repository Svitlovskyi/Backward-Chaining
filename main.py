from Parser.Parser import *
from BackwardChaining.Utils.NodesUtils import Node_Store_Utils
from BackwardChaining.BackwardChaining import Backward_Chaining

if __name__ == '__main__':
    #Parse
    parser = Parser("Tests/Test")
    rules, facts, goals = parser.parse_file()
    #Initialize Nodes
    utils = Node_Store_Utils()
    node_store = utils.initialize_atom_nodes_store_from_rules(rules, facts)
    #Solve
    backward_chaining = Backward_Chaining(node_store, goals)
    for i in goals:
        result = backward_chaining.backward_chaining(i)
        print(result)




