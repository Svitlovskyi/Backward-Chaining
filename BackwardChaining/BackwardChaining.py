from RulesUtils import RulesUtils
from Solver import Solver
from Nodes import NodeStore

class Backward_Chaining:
    def __init__(self, node_store, goals):
        self.node_store = node_store
        self.goals = goals


    def backward_chaining(self, goal):
        for node in self.node_store.atom_node_list:
            if node.name == goal:
                while True:
                    child = node.child
                    rule_utils = RulesUtils()
                    is_all_node_know, unknown_node = rule_utils.check_is_all_node_is_known(child, self.node_store)

                    if node.state == True or node.state == False:
                        return node.state
                    if is_all_node_know:
                        solver = Solver()
                        logical_operation = rule_utils.transform_child_to_logical_operation(child, self.node_store)
                        i = solver.solve_rule(logical_operation)
                        return i
                    elif unknown_node.child == []:
                        raise Exception("Not enough data")
                    else:
                        searched_subgoal_value = self.backward_chaining(unknown_node.name)
                        self.node_store.set_state(unknown_node.name, searched_subgoal_value)

