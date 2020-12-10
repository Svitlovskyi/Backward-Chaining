class Solver:
    def solve_and(self, rhs, lhs):
        if rhs and lhs:
            return True
        return False

    def solve_or(self, rhs, lhs):
        if rhs or lhs:
            return True
        return False

    def solve_not(self, value):
        return not value

    def solve_inference(self, rhs):
        return rhs