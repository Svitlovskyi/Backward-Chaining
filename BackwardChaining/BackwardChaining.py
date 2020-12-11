from BackwardChaining.Utils.RulesUtils import RulesUtils
from BackwardChaining.Utils.Solver import Solver


class Backward_Chaining:
    def __init__(self, node_store, goals):
        self.node_store = node_store
        self.goals = goals


    def backward_chaining(self, goal):
        for node in self.node_store.atom_node_list:
            if node.name == goal:
                while True:
                    child = node.child
                    if node.name in child:
                        raise Exception("Prerequisite can't be a consequence at the same time")

                    
                    rule_utils = RulesUtils()
                    is_all_node_know, unknown_nodes = rule_utils.check_is_all_node_is_known(child, self.node_store)

                    if node.state != None:
                        return node.state
                    if is_all_node_know:
                        solver = Solver()
                        logical_operation = rule_utils.transform_child_to_logical_operation(child, self.node_store)
                        i = solver.solve_rule(logical_operation)
                        return i
                    elif all([unknown_node.child == [] for unknown_node in unknown_nodes]) and unknown_nodes != None:
                        for unknown_node in unknown_nodes:
                            if unknown_node.child == []:
                                self.node_store.set_state(unknown_node.name, False)
                    else:
                        for unknown_node in unknown_nodes:
                            searched_subgoal_value = self.backward_chaining(unknown_node.name)
                            self.node_store.set_state(unknown_node.name, searched_subgoal_value)
