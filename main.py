from Parser.Parser import *
from BackwardChaining.Utils.NodesUtils import Node_Store_Utils
from BackwardChaining.BackwardChaining import Backward_Chaining
import sys


def main_func(text_name):
    sys.setrecursionlimit(10000)
    # Parse
    parser = Parser("Tests/{}".format(text_name))
    rules, facts, goals = parser.parse_file()
    # Initialize Nodes
    utils = Node_Store_Utils()
    node_store = utils.initialize_atom_nodes_store_from_rules(rules, facts)
    # Solve
    backward_chaining = Backward_Chaining(node_store, goals)
    for i in goals:
        result, vis = backward_chaining.backward_chaining(i)
        return result, vis

if __name__ == '__main__':
    test = {
            "andTest": True,
            "bracketsTest": True,
            "notTest": True,
            "orTest": True,
            "xorTest": True,
            "complexTest": False
    }
    result = []
    vis = []
    for key in test:
        test_result, vis = main_func(key)
        is_completed = (test_result == test[key])
        print("test name: {}, completed: {}".format(key, is_completed))



