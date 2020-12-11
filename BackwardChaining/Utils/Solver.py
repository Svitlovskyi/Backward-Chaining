class Solver:
    __operators = ["+", "=>", "|", "^"]

    '''@input: rule part
       @return: solved rule
    '''

    def solve_rule(self, rule):
        solved_rule = rule
        if len(rule) != 0:
            while len(rule) != 1:
                solved_rule = self.get_first_logical_operation(solved_rule)
            return solved_rule

    '''@input: rule 
       @return: get first logical operation and solve it
    '''

    def get_first_logical_operation(self, rule):
        rule = self.solve_all_not(rule)
        for index, node in enumerate(rule):
            if node in self.__operators:
                rule[index] = self.solve(node, rule[index - 1], rule[index + 1])
                rule.pop(index + 1)
                rule.pop(index - 1)
                return rule
    '''@input: rule
       @return: rule with solved not operator
    '''
    def solve_all_not(self, rule):
        for index, node in enumerate(rule):
            if node == "!":
                rule[index] = self.solve_not(rule[index + 1])
                rule.pop(index + 1)
        return rule

    '''@input: operator, lhs, rhs
       @return: solved operation
    '''

    def solve(self, operator, lhs, rhs=None):
        if operator == "+":
            return self.solve_and(lhs, rhs)
        elif operator == "|":
            return self.solve_or(lhs, rhs)
        elif operator == "^":
            return self.solve_xor(lhs, rhs)
        else:
            raise Exception("Unknown logical operator")

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

    def solve_xor(self, lhs, rhs):
        if lhs == rhs:
            return False
        return True
