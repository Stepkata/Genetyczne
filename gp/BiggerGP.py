class BiggerGP:
    def __init__(self, p_size: int = 25000, depth: int = 5):
        self.MAX_LEN: int = 10000
        self.POP_SIZE: int = p_size
        self.DEPTH: int = depth
        self.GENERATIONS: int = 50
        self.MATCH_SIZE: int = 2

        self.fitness = []
        self.population = []

        self.buffer = []
        self.term_buffer = []

    def generate_random_individual(self):
        pass

    def populate_population(self):
        pass

    def fitness(self):
        pass

    def crossover(self):
        pass

    def mutation(self):
        pass

    def tournament(self):
        pass

    def to_string(self) -> str:
        pass

    def evolve(self):
        pass



