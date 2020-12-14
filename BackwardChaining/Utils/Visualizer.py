class Visualizer():
    def __init__(self, data):
        self.data = data
        self.used_symbols = []
        self.temp_symbol_1 = None
        self.temp_symbol_2 = None
        self.temp_symbol_3 = None
        self.temp_symbol_4 = None
    def print_tree(self):
        print("|")
        for dic in self.data.keys():
            self.temp_symbol_1 = None
            self.temp_symbol_2 = None
            self.temp_symbol_3 = None
            self.temp_symbol_4 = None
            if(dic not in self.used_symbols):
                print("|_{0}".format(dic))
                for fact in self.data[dic]:
                    self.used_symbols.append(fact)
                    if(self.__check_symbol(fact)):
                        if(self.temp_symbol_1 == "!"):
                            print("| |_not {0}".format(fact))
                        elif(self.temp_symbol_1 == "|"):
                            print("| or")
                            print("| |_{0}".format(fact))
                        elif(self.temp_symbol_1 == "^"):
                            print("| xor")
                            print("| |_{0}".format(fact))
                        else:
                            print("| |_{0}".format(fact))
                    else:
                        self.temp_symbol_1 = fact
                    
                    for dic_as_fact in self.data.keys():
                        if fact == dic_as_fact:
                            for fact2 in self.data[fact]:
                                if(self.__check_symbol(fact2)):
                                    if(self.temp_symbol_2 == "!"):
                                        print("| | |_not {0}".format(fact2))
                                    elif(self.temp_symbol_2 == "|"):
                                        print("| | or")
                                        print("| | |_{0}".format(fact2))
                                    elif(self.temp_symbol_2 == "^"):
                                        print("| | xor")
                                        print("| | |_{0}".format(fact2))
                                    else:
                                        print("| | |_{0}".format(fact2))
                                else:
                                    self.temp_symbol_2 = fact2
                                
                                for dic_as_fact2 in self.data.keys():
                                    if fact2 == dic_as_fact2:
                                        for fact3 in self.data[fact2]:
                                            if(self.__check_symbol(fact3)):
                                                if(self.temp_symbol_3 == "!"):
                                                    print("| | | |_not {0}".format(fact3))
                                                elif(self.temp_symbol_3 == "|"):
                                                    print("| | | or")
                                                    print("| | | |_{0}".format(fact3))
                                                elif(self.temp_symbol_3 == "^"):
                                                    print("| | | xor")
                                                    print("| | | |_{0}".format(fact3))
                                                else:
                                                    print("| | | |_{0}".format(fact3))
                                            else:
                                                self.temp_symbol_3 = fact3

                                            for dic_as_fact3 in self.data.keys():
                                                if fact3 == dic_as_fact3:
                                                    for fact4 in self.data[fact3]:
                                                        if(self.__check_symbol(fact4)):
                                                            if(self.temp_symbol_4 == "!"):
                                                                print("| | | | |_not {0}".format(fact4))
                                                            elif(self.temp_symbol_3 == "|"):
                                                                print("| | | | or")
                                                                print("| | | | |_{0}".format(fact4))
                                                            elif(self.temp_symbol_4 == "^"):
                                                                print("| | | | xor")
                                                                print("| | | | |_{0}".format(fact4))
                                                            else:
                                                                print("| | | | |_{0}".format(fact4))
                                                        else:
                                                            self.temp_symbol_4 = fact4
                                                        self.used_symbols.append(fact4)
                                            self.used_symbols.append(fact3)
                                self.used_symbols.append(fact2)
                    
                print("|")
                self.used_symbols.append(dic)
    
    def __check_symbol(self, symb):
        if(symb == "+" or symb == "(" or symb == ")" or symb == "!" or symb == "|" or symb == "^"): 
            return False
        else:
            return True
