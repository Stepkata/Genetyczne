import re


class GrammarReader:
    def __init__(self):
        self.terminals = {}
        self.rules = {}

    def read_grammar(self, filename):
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
                    self.terminals[left] = re.sub("'", "", right)
                else:
                    self.rules[left] = right.split("|")

            print("TERMINALS:", self.terminals)
            print("RULES:", self.rules)

    def get_start_rule(self) -> str:
        return list(self.rules.keys())[1]


if __name__ == "__main__":
    g = GrammarReader()
    g.read_grammar("C:\\Users\\keste\\PycharmProjects\\Genetyczne\\Expr.g4")
    print(g.get_start_rule())
