import copy
import random
import string
from gp.Stats import Stats


class BiggerGP:
    """ Class executing genetic algorithm using simple custom programming language"""

    def __init__(self, p_size: int = 500, depth: int = 4):
        self.MAX_LEN: int = 4
        self.MAX_LOGIC_LEN: int = 5
        self.POP_SIZE: int = p_size
        self.DEPTH: int = depth
        self.GENERATIONS: int = 50
        self.MATCH_SIZE: int = 2
        self.MUTATION_RATE: int = 10

        self.pop_fitness: list = []
        self.population: list = []

        self.terminal_table: dict = {
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
            2400: '.',
            2500: '!'}

        self.grammar: dict = {
            0: [[1, 1900]],  # 'prog': ['expr NEWLINE'],
            1: [[3, 2400, 1900], [8, 2400, 1900], [2, 2400, 1900], [10, 2400, 1900]],
            # 'expr': ['print COLON NEWLINE', 'if_statement COLON NEWLINE', 'variable_assign COLON NEWLINE', 'while COLON NEWLINE'],
            2: [[2100, 600, 6], [2100, 600, 2300]],
            # 'variable_assign': ['IDENTIFIER EQ literals', 'IDENTIFIER EQ INPUT'],
            3: [[2000, 700, 6, 800]],  # 'print': ['PRINT LPAREN literals RPAREN'],
            4: [[300], [400], [100], [500], [200]],  # 'operators': ['MULTIPLY', 'DIVIDE', 'ADD', 'MOD', 'SUBSTRACT'],
            5: [[1500], [1600]],  # 'logic_operators': ['AND', 'OR'],
            6: [[2100], [2200], [6, 4, 6]],  # 'literals': ['IDENTIFIER', 'INTLITERAL', 'literals operators literals'],
            7: [[1300], [1200], [1100], [1400]],  # 'comparisson_type': ['EQEQ', 'GTHAN', 'LTHAN', 'NOTEQ'],
            8: [[1700, 700, 9, 800, 900, 1900, 1, 1900, 1000], [1700, 2500, 700, 9, 800, 900, 1900, 1, 1900, 1000]],
            # 'if_statement': ['IF LPAREN condition RPAREN LCURL NEWLINE expr NEWLINE RCURL'],['IF NOT LPAREN condition RPAREN LCURL NEWLINE expr NEWLINE RCURL']
            9: [[6, 7, 6], [9, 5, 9]],
            # 'condition': ['literals comparisson_type literals', 'condition logic_operators condition'],
            10: [[1800, 700, 9, 800, 900, 1900, 1, 1900, 1000], [1800, 2500, 700, 9, 800, 900, 1900, 1, 1900, 1000]]
            # 'while': ['WHILE LPAREN  condition RPAREN LCURL NEWLINE  expr NEWLINE  RCURL'], ['WHILE NOT LPAREN  condition RPAREN LCURL NEWLINE  expr NEWLINE  RCURL']
        }

        self.node_starts: list = [1700, 2000, 1800]
        self.start: int = 1  # expr
        self.node_end: int = 2400  # dot
        self.variables: dict = {}
        self.int_literals: dict = {}
        self.variables_buffer: list = []
        self.stats: list = []

    """grows the buffer. An iteration of self.grow"""

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
                buffer += rule
            else:
                buffer.append(rule)
        return buffer

    """Checks for special cases when creating rules:
        - if the new_rule demands the use of a variable, it checks if there are any declared by the individual. 
            if not the variable is swapped for an integer
        - if the rule will create a variable, we add it to the declared variables (self.variables and variables_buffer)
            and immediately place it in the new_rule
        - if the rule is a condition we check the neighbourhood to count how long is the logical statement already.
            If it is longer than self.MAX_LOGIC_LEN, we do not allow it to make more conditions in new_rule"""

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
            index = len(self.variables) + 10000
            self.variables[index] = random.choice(
                string.ascii_letters)  # if we are creating variable, add its name to register
            self.variables_buffer.append(index)
            new_rule[new_rule.index(2100)] = index
        if rule == 9:
            ind1 = 0
            ind2 = len(buffer) - 1
            for i in range(0, index - 1):
                if buffer[i] == 700:
                    ind1 = i
                    break
            for i in range(index, len(buffer) - 1):
                if buffer[i] == 800:
                    ind2 = i
                    break
            neighbors = buffer[ind1:ind2]
            num_logic = neighbors.count(1500) + neighbors.count(1600) + neighbors.count(5)
            if num_logic >= self.MAX_LOGIC_LEN:
                new_rule = [6, 7, 6]

        return new_rule

    """Grows the syntax tree from the starting rule in the buffer.
     Makes sure no start rule is left at the maximum depth"""

    def grow(self, buffer: []):
        pom = []  # make sure we do not create any more nodes
        for index, rule in enumerate(buffer):
            if rule in self.grammar.keys():
                rules = [rule for rule in copy.deepcopy(self.grammar[rule]) if self.start not in rule]
                if len(rules) == 0:
                    rules.append([1900])
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
                index = len(self.int_literals) + 100000
                self.int_literals[index] = random.randint(0, 10000)  # can be changed
                buffer[i] = index

        self.to_string(buffer)
        return buffer

    def generate_random_individual(self) -> list:
        self.variables_buffer = []
        buffer = []
        for _ in range(random.randint(1, self.MAX_LEN)):
            buffer.append(self.start)
        return self.grow(buffer)

    def populate_population(self) -> None:
        for _ in range(self.POP_SIZE):
            self.population.append(self.generate_random_individual())

    def calculate_pop_fitness(self, fitness_f) -> None:
        self.pop_fitness = []
        for specimen in self.population:
            self.pop_fitness.append(self.fitness(specimen, fitness_f))

    def fitness(self, specimen: [], fitness_f) -> float:
        return fitness_f(self.to_string(specimen))

    def get_best_fitness(self) -> float:
        if len(self.pop_fitness) > 0:
            return max(self.pop_fitness)
        else:
            return -1000

    def get_average_fitness(self) -> float:
        return sum(self.pop_fitness) / len(self.pop_fitness)

    def get_best_individual(self) -> list:
        if len(self.pop_fitness) != len(self.population):
            raise Exception("Population does not equal fitness")
        max_fitness = max(self.pop_fitness, default=None)
        if max_fitness is None:
            index = 0
        else:
            index = self.pop_fitness.index(max_fitness)
        return self.population[index]

    """Swaps branches between parent1 and parent1"""

    def crossover(self, parent1: [], parent2: []) -> list:
        new_specimen = []
        (index1_start, index1_end) = self.find_index(parent1)
        (index2_start, index2_end) = self.find_index(parent2)
        new_specimen = parent1[:index1_start] + parent2[index2_start:index2_end] + parent1[index1_end:]
        '''print("parent1", self.to_string(parent1))
        print("----------------------------------")
        print("parent2", self.to_string(parent2))
        print("start: ", parent1[index1_start], "end: ", parent1[index1_end])
        print("----------------------------------")
        print("child", self.to_string(new_specimen))'''''
        return new_specimen

    """Finds the beginning and end of the statement (branch) that will be swapped"""

    def clean_individual(self, buffer):
        result = copy.deepcopy(buffer)
        for i in range(len(buffer)-2):
            if buffer[i] == 1900 and buffer[i+1] == 1900:
                result = result[:i] + result[i+1:]
            elif buffer[i] == 1900 and buffer[i+1] != 2400:
                result = result[:i] + [2400] + result[i:]
        return result
    def find_index(self, specimen: []) -> tuple:
        indexes = [index for index, item in enumerate(specimen) if item in self.node_starts]
        for i in range(len(specimen) - 2):
            if specimen[i] >= 10000 and specimen[i + 1] == 600:
                indexes.append(i)
        if len(indexes) == 0:
            return 0, 0
        index1 = random.choice(indexes)
        if specimen[index1] in [1700, 1800]:
            index_end = self.find_closing_parentheses(index1, specimen)
        else:
            index_end = self.find_closing_dot(index1, specimen)
        return index1, index_end

    def find_closing_dot(self, index: int, buffer: []) -> int:
        for i in range(index, len(buffer) - 1):
            if buffer[i] == 2400:
                return i
        return len(buffer) - 1

    def find_closing_parentheses(self, index: int, buffer: []) -> int:
        num_begin = 0
        num_end = 0
        for i in range(index, len(buffer) - 2):
            if buffer[i] == 900:
                num_begin += 1
            if buffer[i] == 1000:
                num_end += 1
            if num_end != 0 and num_end == num_begin:
                return i + 1
        return len(buffer) - 1

    """Mutates a random individual. There are following ways the individual is mutated:
        0. The variables used in the equations are shuffled
        1. One of its statements (branches) is replaced
        2. The first condition or print statement is changed"""

    def mutation(self, specimen) -> list:
        # print("Old", self.to_string(specimen))
        # print("-------")
        mutation_type = random.randint(0, 2)
        # print(mutation_type)
        if mutation_type == 0:
            for i in range(len(specimen)):
                if specimen[i] in self.variables:
                    specimen[i] = random.choice(list(self.variables.keys()))
            # print(self.to_string(specimen))
            return specimen
        if mutation_type == 1:
            (index1_start, index1_end) = self.find_index(specimen)
            new_branch = self.grow(random.choice(self.grammar[self.start]))
            new_specimen = specimen[:index1_start] + new_branch + specimen[index1_end + 1:]
            # print(self.to_string(new_specimen))
            return new_specimen
        if mutation_type == 2:
            index1 = len(specimen) - 1
            index2 = len(specimen) - 1
            for i in range(len(specimen)):
                if specimen[i] == 700:
                    index1 = i
                if specimen[i] == 800:
                    index2 = i
                    break
            if index1 == index2:
                # print(self.to_string(specimen))
                return specimen
            if any([1100 <= x <= 1600 for x in specimen[index1:index2]]):
                new_logic = self.grow([9])
            else:
                new_logic = self.grow([6])
            new_specimen = specimen[:index1 + 1] + new_logic + specimen[index2:]
            # print(self.to_string(new_specimen))
            return new_specimen

    """Finds the most fit individual """

    def tournament(self, tournament_size: int):
        best = random.randint(0, len(self.population)-1)
        best_fit = -1.0e34
        for i in range(tournament_size):
            competitor = random.randint(0, len(self.population) - 1)
            if self.pop_fitness[competitor] > best_fit:
                best = competitor
                best_fit = self.pop_fitness[competitor]

        return self.population[best]

    """Chooses a random individual to be replaced from a group of tournament_size individuals"""

    def negative_tournament(self, tournament_size: int):
        worst = random.randint(0, len(self.population)-1)
        worst_fit = -1.0e34
        for i in range(tournament_size):
            competitor = random.randint(0, len(self.population) - 1)
            if self.pop_fitness[competitor] < worst_fit:
                worst = competitor
                worst_fit = self.pop_fitness[competitor]

        return worst

    """Translates the individual to readable string using the terminals_table lookup table"""

    def to_string(self, buffer) -> str:
        pom = []
        for term in buffer:  # translate terminals
            if term in self.terminal_table.keys():
                pom.append(self.terminal_table[term])
            elif term in self.int_literals.keys():
                pom.append(str(self.int_literals[term]))
            elif term in self.variables.keys():
                pom.append(self.variables[term])
            else:
                pom.append(str(term))
        return ' '.join(pom)

    """Gather current generation stats"""
    def get_stats(self, solved, generation):
        best_indiv = self.get_best_individual()
        best_fit = self.get_best_fitness()
        avg_fit = self.get_average_fitness()
        return Stats(solved, generation, best_fit, self.to_string(best_indiv), avg_fit, self.POP_SIZE, self.DEPTH)

    def evolve(self, fitness_f):
        self.populate_population()
        for g in range(self.GENERATIONS):
            print("GENERATION ", g)
            self.calculate_pop_fitness(fitness_f)
            if self.get_best_fitness() > -1e-5:
                print("Problem solved")
                stats = self.get_stats(True, g)
                self.stats.append(stats)
                print(stats.to_string())
                return self.stats
            else:
                stats = self.get_stats(False, g)
                self.stats.append(stats)
                print(stats.to_string())
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
                    self.pop_fitness[offspring] = new_fitness
        print("Problem NOT solved")
        return self.stats


if __name__ == "__main__":
    b = BiggerGP()
    specimen1 = b.generate_random_individual()
    print(b.to_string(specimen1))
    #specimen2 = b.generate_random_individual()
    # specimen3 =  b.generate_random_individual()
    # specimen4 =  b.generate_random_individual()
    # specimen5 =  b.generate_random_individual()
    # b.crossover(specimen1, specimen2)
    #b.mutation(specimen1)
