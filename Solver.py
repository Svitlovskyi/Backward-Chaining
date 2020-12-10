from Operator import *

class Solver:
    __operators = ["+", "=>", "|", "^", "!"]

    def solve_rule(self, rule):
        solved_rule = rule
        while len(rule) != 1:
            solved_rule = self.get_first_logical_operation(solved_rule)
        return solved_rule


    def get_first_logical_operation(self, rule):
        for index, node in enumerate(rule):
            if node in self.__operators:
                if node == "!":
                    rule[index] = self.solve(node, rule[index-1])
                    rule.pop(index+1)
                    return rule
                else:
                    rule[index] = self.solve(node, rule[index-1], rule[index+1])
                    rule.pop(index+1)
                    rule.pop(index-1)
                    return rule



    def solve(self, operator, lhs, rhs=None):
        if operator == "+":
            return self.solve_and(rhs, lhs)
        elif operator == "|":
            return self.solve_or(rhs, lhs)
        elif operator == "!":
            return self.solve_not(lhs)


    def solve_and(self, lhs, rhs):
        if rhs and lhs:
            return True
        return False

    def solve_or(self, lhs, rhs):
        if rhs or lhs:
            return True
        return False

    def solve_not(self, value):
        return not value

    # def solve_inference(self, rhs):
    #     return rhs