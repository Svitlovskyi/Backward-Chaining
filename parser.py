class Parser:
    def __init__(self, file_name):
        self.file_name = file_name

    # return rules, facts and goals lines
    def parse_file(self):
        fileObject = open(self.file_name, mode='r')
        lines = fileObject.readlines()

        rules = []
        facts = ""
        goals = ""

        for line in lines:
            line = line.rstrip()
            if len(line) == 0:
                continue
            if line[0] == "#":
                continue
            if line[0] == " ":
                continue
            if line[0] == "=":
                facts = line
                continue
            if line[0] == "?":
                goals = line
                continue
            rules.append(line)

        return rules, facts, goals
