import copy
import random
import string


class BiggerGP:
    ''' Class executing genetic algorithm using simple custom programming language'''
    def __init__(self, p_size: int = 25000, depth: int = 3):
        self.MAX_LEN: int = 2
        self.MAX_LOGIC_LEN: int = 5
        self.POP_SIZE: int = p_size
        self.DEPTH: int = depth
        self.GENERATIONS: int = 50
        self.MATCH_SIZE: int = 2
        self.MUTATION_RATE: int = 5

        self.pop_fitness: list = []
        self.population: list = []

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
            1: [[3, 2400, 1900], [8, 2400, 1900], [2, 2400, 1900], [10, 2400, 1900]], # 'expr': ['print COLON NEWLINE', 'if_statement COLON NEWLINE', 'variable_assign COLON NEWLINE', 'while COLON NEWLINE'],
            2: [[2100, 600, 6], [2100, 600, 2300]], # 'variable_assign': ['IDENTIFIER EQ literals', 'IDENTIFIER EQ INPUT'],
            3: [[2000, 700, 6, 800]],  # 'print': ['PRINT LPAREN literals RPAREN'],
            4: [[300], [400], [100], [500], [200]],  # 'operators': ['MULTIPLY', 'DIVIDE', 'ADD', 'MOD', 'SUBSTRACT'],
            5: [[1500], [1600]],  # 'logic_operators': ['AND', 'OR'],
            6: [[2100], [2200], [6, 4, 6]],  # 'literals': ['IDENTIFIER', 'INTLITERAL', 'literals operators literals'],
            7: [[1300], [1200], [1100], [1400]],  # 'comparisson_type': ['EQEQ', 'GTHAN', 'LTHAN', 'NOTEQ'],
            8: [[1700, 700, 9, 800, 900, 1900, 1, 1900, 1000]], # 'if_statement': ['IF LPAREN condition RPAREN LCURL NEWLINE expr NEWLINE RCURL'],
            9: [[6, 7, 6], [9, 5, 9]], # 'condition': ['literals comparisson_type literals', 'condition logic_operators condition'],
            10: [[1800, 700, 9, 800, 900, 1900, 1, 1900, 1000]] # 'while': ['WHILE LPAREN  condition RPAREN LCURL NEWLINE  expr NEWLINE  RCURL']
        }

        self.node_starts = [1700, 2000, 1800]
        self.start: int = 1  # expr
        self.node_end: int = 2400  # dot
        self.variables: dict = {}
        self.intliterals: dict = {}
        self.variables_buffer: list = []

    def traverse(self, buffer) -> list:
        pom = []
        for index, rule in enumerate(buffer):
            if rule in self.grammar.keys():
                new_rule = copy.deepcopy(random.choice(self.grammar[rule]))
                new_rule = self.check_new_rule(buffer, new_rule, rule, index)
                pom.append(new_rule)
            else:
                pom.append(rule)
        buffer = []
        for rule in pom:
            if isinstance(rule, list):
                children = buffer.count(2400)
                if self.start in rule and children < self.MAX_LEN:
                    index = rule.index(self.start)
                    for _ in range(random.randint(1, self.MAX_LEN - children)):
                        rule.insert(index, self.start)
                buffer += rule
            else:
                buffer.append(rule)
        return buffer

    def check_new_rule(self, buffer, new_rule, rule, index) -> list:
        if new_rule == [2100]:  # we cannot use variables we didn't declare
            variables_pom = []
            for var in self.variables_buffer:
                if var in buffer and buffer.index(var) < index:
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
        if rule == 9:
            ind1 = 0
            ind2 = len(buffer)-1
            for i in range(0, index -1):
                if buffer[i] == 700:
                    ind1 = i
                    break
            for i in range(index,len(buffer)-1):
                if buffer[i] == 800:
                    ind2 = i
                    break
            neighbors = buffer[ind1:ind2]
            num_logic = neighbors.count(1500) + neighbors.count(1600) + neighbors.count(5)
            if num_logic >= self.MAX_LOGIC_LEN:
                new_rule = [6, 7, 6]

        return new_rule

    def grow(self, buffer: []):
        pom = []  # make sure we do not create any more nodes
        for index, rule in enumerate(buffer):
            if rule in self.grammar.keys():
                rules = [rule for rule in copy.deepcopy(self.grammar[rule]) if self.start not in rule]
                if len(rules) == 0:
                    rules.append([1900]) #for safety
                new_rule = random.choice(rules)
                new_rule = self.check_new_rule(buffer, new_rule, rule, index)
                pom.append(new_rule)
            else:
                pom.append(rule)
        buffer = []
        for rule in pom:
            if isinstance(rule, list):
                buffer += rule
            else:
                buffer.append(rule)

        while any(number < 100 for number in buffer):  # reach terminals
            buffer = self.traverse(buffer)

        for i in range(len(buffer)):  # choose some ints
            if buffer[i] == 2200:
                index = len(self.intliterals) + 100000
                self.intliterals[index] = random.randint(0, 100)  # can be changed
                buffer[i] = index

        self.to_string(buffer)
        return buffer



    def generate_random_individual(self) -> list:
        self.variables_buffer = []
        buffer = []
        for _ in range(random.randint(1, self.MAX_LEN)):
            buffer.append(self.start)
        print(buffer)
        return self.grow(buffer)
    

    def populate_population(self) -> None:
        for _ in range(self.POP_SIZE):
            self.population.append(self.generate_random_individual())

    def fitness_pop(self, fitness_f) -> None:
    
        for specimen in self.population:
            self.pop_fitness.append(fitness_f(specimen))

    def fitness(self, specimen, fitness_f) -> float:
        return fitness_f(specimen)

    def get_best_fitness(self) -> float:
        return max(self.pop_fitness)

    def crossover(self, specimen1, specimen2) -> list:
        new_specimen = []
        indexes1 = []
        indexes2 = []
        indexes1 = [index for index, item in enumerate(specimen1) if item in self.node_starts]
        indexes2 = [index for index, item in enumerate(specimen2) if item in self.node_starts]
        for i in range(len(specimen1)-2):
            if specimen1[i] >= 10000 and specimen1[i+1] == 600:
                indexes1.append(i)
        for i in range(len(specimen2)-2):
            if specimen2[i] >= 10000 and specimen2[i+1] == 600:
                indexes2.append(i)
        if (len(indexes1) == 0):
            return specimen2
        if (len(indexes2) == 0):
            return specimen1
        index1 = random.choice(indexes1)
        index2 = random.choice(indexes2)
        if len(specimen2) - 1 == index2:
            new_specimen = specimen1[:index1] + specimen2
        elif index1 == 0:
            new_specimen = specimen1 + specimen2[index2:]
        else:
            new_specimen = specimen1[:index1] + specimen2[index2:]
        print("parent1", self.to_string(specimen1))
        print("parent2", self.to_string(specimen2))
        print("child", self.to_string(new_specimen))
        return new_specimen

    def mutation(self, specimen) -> list:
        print("Old", self.to_string(specimen))
        print("-------")
        type = random.randint(0,2)
        print(type)
        if type == 0:
            for i in range(len(specimen)):
                if specimen[i] in self.variables:
                    specimen[i] = random.choice(list(self.variables.keys()))
            print(self.to_string(specimen))
            return specimen
        if type == 1:
            indexes = [index for index, x in enumerate(specimen) if x == self.node_end ]
            new_branch = self.grow(random.choice(self.grammar[self.start]))
            index = random.choice(indexes)
            new_speciman = specimen[:index+1] + new_branch
            print(self.to_string(new_speciman))
            return new_speciman
        if type == 2:
            new_speciman = []
            index1 = len(specimen)-1
            index2 = len(specimen)-1
            for i in range(len(specimen)):
                if specimen[i] == 700:
                    index1 = i
                if specimen[i] == 800:
                    index2 = i
                    break
            if index1 == index2:
                print(self.to_string(specimen))
                return specimen
            if any([x >= 1100 and x <= 1600 for x in specimen[index1:index2]]):
                new_logic = self.grow([9])
            else:
                new_logic = self.grow([6])
            new_speciman = specimen[:index1+1] + new_logic + specimen[index2:]
            print(self.to_string(new_speciman))
            return new_speciman

    def tournament(self, tournament_size: int):
        best = random.randint(0, len(self.population))
        best_fit = -1.0e34
        for i in range(tournament_size):
            competitor = random.randint(0, len(self.population))
            if self.pop_fitness[competitor] > best_fit:
                best = competitor
                best_fit = self.pop_fitness[competitor]

        return self.population[best]

    def negative_tournament(self, tournament_size:int):
        worst = random.randint(0, len(self.population))
        worst_fit = -1.0e34
        for i in range(tournament_size):
            competitor = random.randint(0, len(self.population))
            if self.pop_fitness[competitor] < worst_fit:
                worst = competitor
                worst_fit = self.pop_fitness[competitor]

        return worst

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
        return ' '.join(pom)

    def evolve(self, fitness_f):
        new_individual = []
        for _ in range(self.GENERATIONS):
            if self.get_best_fitness() > -1e-5:
                print("Problem solved")
            else:
                for i in range(self.POP_SIZE):
                    if random.randint(0, 100) <= self.MUTATION_RATE:
                        parent = self.tournament(self.MATCH_SIZE)
                        new_individual = self.mutation(parent)
                    else:
                        parent1 = self.tournament(self.MATCH_SIZE)
                        parent2 = self.tournament(self.MATCH_SIZE)
                        new_individual = self.crossover(parent1, parent2)
                    new_fitness = self.fitness(new_individual, fitness_f)
                    offspring = self.negative_tournament(self.MATCH_SIZE)
                    self.population[offspring] = new_individual
                    self.fitness[offspring] = new_fitness
        print("Problem NOT solved")




if __name__ == "__main__":
    b = BiggerGP()
    specimen1 = b.generate_random_individual()
    print(b.to_string(specimen1))
    #specimen2 =  b.generate_random_individual()
    #specimen3 =  b.generate_random_individual()
    #specimen4 =  b.generate_random_individual()
    #specimen5 =  b.generate_random_individual()
    #b.crossover(specimen1, specimen2)
    #b.mutation(specimen1)
