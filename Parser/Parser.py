import re


class Parser:
    def __init__(self, file_name):
        self.file_name = file_name

    '''return: rules, facts and goals lines '''
    def parse_file(self):
        fileObject = open(self.file_name, mode='r')
        lines = fileObject.readlines()

        parsed_line = []

        for line in lines:
            line = line.rstrip()
            if len(line) == 0:
                continue
            if line[0] == "#":
                continue
            if line[0] == " ":
                continue
            parsed_line.append(line)

        rules = self.__get_rules_lines(parsed_line)
        facts = self.__get_facts_lines(parsed_line)
        goals = self.__get_goals_lines(parsed_line)

        return rules, facts, goals

    ''' private method 
        @return: rules
        @input: filelines
    '''
    def __get_rules_lines(self, lines):
        rules = []
        pattern = re.compile("[A-Za-z!]")
        for line in lines:
            if pattern.match(line[0]):
                rules.append(line)

        if len(rules) == 0:
            raise Exception("No rules found")
        return rules

    ''' private method 
        @return: goals
        @input: filelines
    '''
    def __get_goals_lines(self, lines):
        for line in lines:
            if line[0] == "?":
                return list(line.replace("?",""))
        raise Exception("No goals found")

    ''' private method 
        @return: facts
        @input: filelines
    '''
    def __get_facts_lines(self, lines):
        for line in lines:
            if line[0] == "=":
                return list(line.replace("=", ""))
        raise Exception("No facts found")
