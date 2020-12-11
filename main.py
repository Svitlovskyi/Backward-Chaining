from Parser.Parser import *
from BackwardChaining.Utils.NodesUtils import Node_Store_Utils
from BackwardChaining.BackwardChaining import Backward_Chaining
import sys

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    #Parse
    parser = Parser("Tests/Test")
    rules, facts, goals = parser.parse_file()
    #Initialize Nodes
    utils = Node_Store_Utils()
    node_store = utils.initialize_atom_nodes_store_from_rules(rules, facts)
    #Solve
    backward_chaining = Backward_Chaining(node_store, goals)
    for i in goals:
        result, vis = backward_chaining.backward_chaining(i)
        print(result)
        print(vis)
    # test = ([], ["A"])
    # array = [x == [] and x=="A" for x in test]
    # print(all(array))



