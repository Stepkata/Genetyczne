import copy
import random
import string


class BiggerGP:
    def __init__(self, p_size: int = 25000, depth: int = 3):
        self.MAX_LEN: int = 5
        self.POP_SIZE: int = p_size
        self.DEPTH: int = depth
        self.GENERATIONS: int = 50
        self.MATCH_SIZE: int = 2

        self.pop_fitness = []
        self.population = []

        self.terminal_table = {
            100: '+',
            200: '-',
            300: '*',
            400: '/',
            500: '%',
            600: '=',
            700: '(',
            800: ')',
            900: '{',
            1000: '}',
            1100: '<',
            1200: '>',
            1300: '==',
            1400: '!=',
            1500: '&&',
            1600: '||',
            1700: 'if',
            1800: 'while',
            1900: '\n',
            2000: 'print',
            2100: 'IDENTIFIER',
            2200: 'INTLITERAL',
            2300: 'input()',
            2400: '.'}

        self.grammar = {
            0: [[1, 1900]],  # 'prog': ['expr NEWLINE'],
            1: [[3, 2400, 1900], [8, 2400, 1900], [2, 2400, 1900], [10, 2400, 1900], [1900]],
            # 'expr': ['print COLON NEWLINE', 'if_statement COLON NEWLINE', 'variable_assign COLON NEWLINE', 'while COLON NEWLINE', 'NEWLINE'],
            2: [[2100, 600, 6], [2100, 600, 2300]],
            # 'variable_assign': ['IDENTIFIER EQ literals', 'IDENTIFIER EQ INPUT'],
            3: [[2000, 700, 6, 800]],  # 'print': ['PRINT LPAREN literals RPAREN'],
            4: [[300], [400], [100], [500], [200]],  # 'operators': ['MULTIPLY', 'DIVIDE', 'ADD', 'MOD', 'SUBSTRACT'],
            5: [[1500], [1600]],  # 'logic_operators': ['AND', 'OR'],
            6: [[2100], [2200], [6, 4, 6]],  # 'literals': ['IDENTIFIER', 'INTLITERAL', 'literals operators literals'],
            7: [[1300], [1200], [1100], [1400]],  # 'comparisson_type': ['EQEQ', 'GTHAN', 'LTHAN', 'NOTEQ'],
            8: [[1700, 700, 9, 800, 900, 1900, 1, 1900, 1000]],
            # 'if_statement': ['IF LPAREN condition RPAREN LCURL NEWLINE expr NEWLINE RCURL'],
            9: [[6, 7, 6], [9, 5, 9]],
            # 'condition': ['literals comparisson_type literals', 'condition logic_operators condition'],
            10: [[1800, 700, 9, 800, 900, 1900, 1, 1900, 1000]]
            # 'while': ['WHILE LPAREN  condition RPAREN LCURL NEWLINE  expr NEWLINE  RCURL']
        }

        self.start: int = 1  # expr
        self.node_end = 2400  # dot
        self.variables = {}
        self.intliterals = {}
        self.variables_buffer = []

    def traverse(self, buffer):
        pom = []
        for rule in buffer:
            if rule in self.grammar.keys():
                new_rule = copy.deepcopy(random.choice(self.grammar[rule]))
                new_rule = self.check_new_rule(buffer, new_rule, rule)
                pom.append(new_rule)
            else:
                pom.append(rule)
        buffer = []
        for rule in pom:
            if isinstance(rule, list):
                if self.start in rule and len(buffer) < self.MAX_LEN:
                    index = rule.index(self.start)
                    for _ in range(random.randint(1, self.MAX_LEN - len(buffer))):
                        rule.insert(index, self.start)
                buffer += rule
            else:
                buffer.append(rule)
        print(buffer)
        return buffer

    def check_new_rule(self, buffer, new_rule, rule):
        if new_rule == [2100]:  # we cannot use variables we didn't declare
            variables_pom = []
            for var in self.variables_buffer:
                if var in buffer and buffer.index(var) < buffer.index(rule):
                    variables_pom.append(var)
            if len(variables_pom) == 0:
                new_rule = 2200
            else:
                new_rule = random.choice(variables_pom)
        if rule == 2:
            print("New_rule:", new_rule)
            print("Rules:", self.grammar[rule])
            index = len(self.variables) + 10000
            self.variables[index] = random.choice(
                string.ascii_letters)  # if we are creating variable, add its name to register
            self.variables_buffer.append(index)
            new_rule[new_rule.index(2100)] = index
        return new_rule

    def generate_random_individual(self):
        self.variables_buffer = []

        buffer = []
        for i in range(random.randint(1, self.MAX_LEN)):  # create the base length of program
            buffer.append(self.start)

        print(buffer)
        for i in range(self.DEPTH - 1):  # grow the tree
            buffer = self.traverse(buffer)

        pom = []  # make sure we do not create any more nodes
        for rule in buffer:
            if rule in self.grammar.keys():
                new_rule = copy.deepcopy(random.choice(self.grammar[rule]))
                while self.start in new_rule:
                    new_rule = random.choice(self.grammar[rule])
                new_rule = self.check_new_rule(buffer, new_rule, rule)
                pom.append(new_rule)
            else:
                pom.append(rule)
        buffer = []
        for rule in pom:
            if isinstance(rule, list):
                buffer += rule
            else:
                buffer.append(rule)
        print(buffer)

        while any(number < 100 for number in buffer):  # reach terminals
            buffer = self.traverse(buffer)

        for i in range(len(buffer)):  # choose some ints
            if buffer[i] == 2200:
                index = len(self.intliterals) + 100000
                self.intliterals[index] = random.randint(0, 100)  # can be changed
                buffer[i] = index

        print(buffer)
        self.to_string(buffer)
        return buffer

    def populate_population(self):
        for _ in range(self.POP_SIZE):
            self.population.append(self.generate_random_individual())

    def fitness(self, fitness_f):
        for specimen in self.population:
            self.pop_fitness.append(fitness_f(specimen))

    def crossover(self, specimen1, specimen2):
        new_specimen = []
        indexes1 = [index for index, value in enumerate(specimen1) if value == self.node_end]
        indexes2 = [index for index, value in enumerate(specimen2) if value == self.node_end]
        index1 = random.choice(indexes1)
        index2 = random.choice(indexes2)
        if len(specimen2) - 1 == index2:
            new_specimen = specimen1[:index1] + specimen2
        elif index1 == 0:
            new_specimen = specimen1 + specimen2[index2:]
        else:
            new_specimen = specimen1[:index1] + specimen2[index2:]
        return new_specimen

    def mutation(self, specimen):
        return self.crossover(specimen, self.generate_random_individual())

    def tournament(self):
        best_index = self.pop_fitness.index(max(self.pop_fitness))
        return self.population[best_index]

    def negative_tournament(self):
        pass

    def to_string(self, buffer) -> str:
        pom = []
        for term in buffer:  # translate terminals
            if term in self.terminal_table.keys():
                pom.append(self.terminal_table[term])
            elif term in self.intliterals.keys():
                pom.append(str(self.intliterals[term]))
            elif term in self.variables.keys():
                pom.append(self.variables[term])
            else:
                pom.append(str(term))
        print(' '.join(pom))
        return ' '.join(pom)

    def evolve(self):
        pass


if __name__ == "__main__":
    b = BiggerGP()
    b.generate_random_individual()
