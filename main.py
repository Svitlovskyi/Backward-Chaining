from parser import *


if __name__ == '__main__':
    parser = Parser("Test")
    rules, facts, goals = parser.parse_file()
    print(rules)
    print(facts)
    print(goals)
