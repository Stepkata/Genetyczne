class Stats:
    """Custom class to gather statistics for BiggerGP"""
    def __init__(self, solved, generation, best_fit, best_indiv, avg_fit, pops, d):
        self.solved: bool = solved
        self.generation: int = generation
        self.best_fitness: float = best_fit
        self.best_individual: str = best_indiv
        self.avg_fitness: float = avg_fit
        self.pop_size: int = pops
        self.depth: int = d

    def to_string(self):
        return (f"Generation: {self.generation} - Best Fitness: {self.best_fitness} - Average Fitness: {self.avg_fitness},"
                f"- Population: {self.pop_size} - Depth: {self.depth} \n Best Individual:\n {self.best_individual}")
