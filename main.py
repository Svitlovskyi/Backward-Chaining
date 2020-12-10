from Parser import *
from NodesUtils import Node_Store_Utils
from RulesUtils import RulesUtils
from Solver import Solver

class Backward_Chaining:
    def __init__(self, node_store, goals):
        self.node_store = node_store
        self.goals = goals[0]


    def search_goal(self, goal):
        for node in node_store.atom_node_list:
            if node.name == goal:
                while True:
                    child = node.child
                    rule_utils = RulesUtils()
                    is_all_node_know, unknown_node = rule_utils.check_is_all_node_is_known(child, self.node_store)
                    if is_all_node_know:
                        solver = Solver()
                        logical_operation = rule_utils.transform_child_to_logical_operation(child, self.node_store)
                        i = solver.solve_rule(logical_operation)
                        return i
                    elif unknown_node.child == []:
                        raise Exception("Not enough data")
                    else:
                        searched_subgoal_value = self.search_goal(unknown_node.name)
                        print(searched_subgoal_value)

                        self.node_store.set_state(unknown_node.name, searched_subgoal_value)
                # TODO: SOLVE


if __name__ == '__main__':
    parser = Parser("Test")
    rules, facts, goals = parser.parse_file()
    utils = Node_Store_Utils()
    node_store = utils.initialize_atom_nodes_store_from_rules(rules, facts)
    backward_chaining = Backward_Chaining(node_store, goals)
    result = backward_chaining.search_goal(backward_chaining.goals[0])
    print(result)




