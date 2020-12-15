from Parser.Parser import *
from BackwardChaining.Utils.NodesUtils import Node_Store_Utils
from BackwardChaining.BackwardChaining import Backward_Chaining
from BackwardChaining.Utils.Visualizer import Visualizer


def main_func(text_name):
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
            "andTest2": False,
            "bracketsTest": True,
            "bracketsTest2": False,
            "notTest": True,
            "notTest2": False,
            "orTest": True,
            "orTest2": True,
            "xorTest": True,
            "xorTest2": False,
            "complexTest": False
    }
    result = []
    vis = []
    for key in test:
        test_result, vis = main_func(key)
        is_completed = (test_result == test[key])
        print("test file name: {}, is test passed: {}".format(key, is_completed))
        # print(vis)
        # visual = Visualizer(vis)
        # visual.print_tree()

#TODO: Rules parser check

