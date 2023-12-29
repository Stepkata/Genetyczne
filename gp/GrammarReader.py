import re
import random


class GrammarReader:
    def __init__(self):
        self.terminals = {}
        self.rules = {}

        self.TERMINAL_NUMBERS = {}
        self.RULE_NUMBERS = {}
        self.GRAMMAR = {}

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
            self.TERMINAL_NUMBERS = {terminal: i*100 for i, terminal in enumerate(self.terminals.keys())}
            self.RULE_NUMBERS = {rule : i for i, rule in enumerate(self.rules.keys())}

    def get_start_rule(self) -> str:
        return list(self.rules.keys())[1]

    def check(self):
        pass
    def process(self):
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
        for i in range(random.randint(1, maxlen)):  # create the base length of program
            buffer.append(self.get_start_rule())
        print(buffer)

        for i in range(n - 1):  # grow the tree
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
        for rule in buffer:  # make sure all the nodes of the tree can be transformed into literals next iteration
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

        while any(rule.islower() for rule in buffer):  # reach all terminals
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
        for term in buffer:  # translate terminals
            if term in self.terminals.keys():
                pom.append(self.terminals[term])
            elif len(term) > 0:
                pom.append(term)
        print(pom)

        return buffer

    def crossover(self):
        obj1 = self.generate_grammar(3, 3)
        obj2 = self.generate_grammar(3, 3)
        print("\n\n")
        print(obj1)
        print(obj2)
        print("\n\n")
        indexes1 = [index for index, value in enumerate(obj1) if value == 'COLON']
        indexes2 = [index for index, value in enumerate(obj2) if value == 'COLON']
        index1 = random.choice(indexes1)
        index2 = random.choice(indexes2)
        if len(obj2) - 1 == index2:
            print(obj1[:index1] + obj2)
        elif index1 == 0:
            print(obj1 + obj2[index2:])
        else:
            print(obj1[:index1] + obj2[index2:])


if __name__ == "__main__":
    g = GrammarReader()
    g.read_grammar("C:\\Users\\keste\\PycharmProjects\\Genetyczne\\Expr.g4")
    #print(g.get_start_rule())
    #print(g.get_fset())
    print("\n\n")
    print(g.TERMINAL_NUMBERS)
    print(g.RULE_NUMBERS)
    #g.generate_grammar(3, 5)
    print("\n\n")
    g.process()
    #g.crossover()
