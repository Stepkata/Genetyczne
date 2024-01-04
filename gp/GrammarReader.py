import re
import random


class GrammarReader:
    '''Class meant to read and process small grammars. It will recognise rules that create terminals (self.terminals)
      and separate them from grammar (self.rules). It will then assign int numbers to each rule (self.TERMINAL_NUMBERS, self.RULE_NUMBERS)
      and create grammar rules from them for space optimisation, as well as give look-up table with terminals to use in syntax creation'''
    def __init__(self):
        self.terminals = {}
        self.rules = {}

        self.TERMINAL_NUMBERS = {}
        self.RULE_NUMBERS = {}
        self.GRAMMAR = {}

    def read_grammar(self, filename) -> None:
        with open(filename, "r") as f:
            data = f.read()
            data = re.sub(r'\n', '', data)
            data = re.sub(r' {4}', " ", data)
            lines = data.split(";")
            for line in lines:
                if ":" not in line:
                    continue
                (left, right) = line.split(":")
                if left.isupper():
                    right = re.sub("([' ])", "", right)
                    if len(right) > 1:
                        right =  re.sub(r'\*', '', right)
                    self.terminals[left] = re.sub("([' ])", "", right)
                else:
                    right =  re.sub(r'\*', '', right)
                    rules = right.split("|")
                    buffer = []
                    for rule in rules:
                        rule = re.sub(r'[()]', '', rule)
                        rule = rule.strip()
                        buffer.append(rule)
                    self.rules[left] = buffer

            print("TERMINALS:", self.terminals)
            print("RULES:", self.rules)
            self.TERMINAL_NUMBERS = {terminal: i*100 for i, terminal in enumerate(self.terminals.keys())}
            self.RULE_NUMBERS = {rule : i for i, rule in enumerate(self.rules.keys())}

    def get_start_rule(self) -> str:
        ''' returns the beginning rule of the grammar. We ignore the prog: expr rule as it can be simplified'''
        first = list(self.rules.keys())[0]
        if len(self.rules[first]) == 1:
            return list(self.rules.keys())[1]
        else:
            return first

    def get_processed_grammar(self) -> dict:
        ''' returns grammar consisting only of int numbers, based on self.TERMINAL_NUMBERS and self.RULE_NUMBERS'''
        buff = {}
        for (rule, term) in self.rules.items():
            pom = []
            for item in term:
                help = []
                split = item.split(" ")
                for i in split:
                    if i in self.terminals.keys():
                        help.append(self.TERMINAL_NUMBERS[i])
                    elif i in self.rules.keys():
                        help.append(self.RULE_NUMBERS[i])
                pom.append(help)
            buff[self.RULE_NUMBERS[rule]] = pom
        print(buff)
        return buff
    
    def get_terminal_table(self) -> dict:
        ''' returns terminal lookup table for future parsing '''
        buff = {}
        for (key, item) in self.TERMINAL_NUMBERS.items():
            buff[item] = self.terminals[key]
        print(buff)
        return buff



if __name__ == "__main__":
    g = GrammarReader()
    g.read_grammar("C:\\Users\\keste\\Genetyczne\\Expr.g4")
    print("\n\n")
    print(g.TERMINAL_NUMBERS)
    print(g.RULE_NUMBERS)
    print("\n\n")
    g.get_processed_grammar()
    print("\n\n")
    g.get_terminal_table()
    print("\n\n")
    print(g.get_start_rule())
