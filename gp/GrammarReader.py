import re
import random


class GrammarReader:
    def __init__(self):
        self.terminals = {}
        self.rules = {}


    def read_grammar(self, filename):
        with open(filename, "r") as f:
            data = f.read()
            data = re.sub(r'\n', '', data)
            data = re.sub(r'\*', '', data)
            data = re.sub(r' {4}', " ", data)
            lines = data.split(";")
            for line in lines:
                if ":" not in line:
                    continue
                (left, right) = line.split(":")
                if left.isupper():
                    self.terminals[left] = re.sub("([' ])", "", right)
                else:
                    rules = right.split("|")
                    buffer = []
                    for rule in rules:
                        rule = re.sub(r'[()]', '', rule)
                        rule = rule.strip()
                        buffer.append(rule)
                    self.rules[left] = buffer

            print("TERMINALS:", self.terminals)
            print("RULES:", self.rules)

    def get_start_rule(self) -> str:
        return list(self.rules.keys())[1]

    def get_fset(self) -> dict:
        fset = {}
        start = self.get_start_rule()
        pom_creat = 100
        pom_term = 200
        for rule in self.rules.keys():
            for term in self.rules[rule]:
                if start in term:
                    fset[rule] = pom_creat
                    pom_creat += 1
                    break
                else:
                    fset[rule] = pom_term
                    pom_term += 1
        return fset

    def generate_grammar(self, n, maxlen):
        fset = self.get_fset()
        start = self.get_start_rule()

        buffer = []
        for i in range(random.randint(1, maxlen)):
            buffer.append(self.get_start_rule())
        print(buffer)
        for i in range(n-1):
            pom = []
            for rule in buffer:
                if rule in self.rules.keys():
                    pom.append(random.choice(self.rules[rule]))
                else:
                    pom.append(rule)
            buffer = []
            for rule in pom:
                split = rule.split(" ")
                if start in split and len(buffer) < maxlen:
                    index = split.index(start)
                    for i in range(random.randint(1, maxlen - len(buffer))):
                        split.insert(index, start)
                buffer += split
            print(buffer)

        pom = []
        for rule in buffer:
            if rule in self.rules.keys():
                if rule == self.get_start_rule():
                    new_rule = random.choice(self.rules[rule])
                    while new_rule in self.rules.keys() and fset[new_rule] < 200:
                        new_rule = random.choice(self.rules[rule])
                    pom.append(new_rule)
                else:
                    pom.append(random.choice(self.rules[rule]))
            else:
                pom.append(rule)
        buffer = []
        for rule in pom:
            buffer += rule.split(" ")
        print(buffer)

        while any(rule.islower() for rule in buffer):
            pom = []
            for rule in buffer:
                if rule in self.rules.keys():
                    pom.append(random.choice(self.rules[rule]))
                else:
                    pom.append(rule)
            buffer = []
            for rule in pom:
                buffer += rule.split(" ")
            print(buffer)

        pom = []
        for term in buffer:
            if term in self.terminals.keys():
                pom.append(self.terminals[term])
            elif len(term) > 0:
                pom.append(term)
        print(pom)





if __name__ == "__main__":
    g = GrammarReader()
    g.read_grammar("C:\\Users\\keste\\PycharmProjects\\Genetyczne\\Expr.g4")
    print(g.get_start_rule())
    print(g.get_fset())
    print("\n\n")
    g.generate_grammar(5, 14)
