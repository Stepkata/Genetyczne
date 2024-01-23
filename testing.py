from antlr4 import *
from gen.ExprLexer import ExprLexer
from gen.ExprParser import ExprParser
from gen.ExprVisitor import ExprVisitor
from gp.BiggerGP import BiggerGP
import matplotlib.pyplot as plt


def fitness_function_1(program):
    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        visitor = ExprVisitor()
        output = visitor.visit(tree)
        # print("Output: ", output)
        if 1 in output:
            return 0
        else:
            return -10 * (abs(min(output)) + 1)
    except Exception as e:
        # print(e)
        return -1000


def fitness_function_2(program):
    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        visitor = ExprVisitor()
        output = visitor.visit(tree)
        # print("Output: ", output)
        if 789 in output:
            return 0
        else:
            if len(output) == 0:
                return -10000
            else:
                return -10 * (sum([abs(x-789) for x in output])/10 + 1)
    except Exception as e:
        # print(e)
        return -1000


def fitness_function_3(program):
    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        visitor = ExprVisitor()
        output = visitor.visit(tree)
        # print("Output: ", output)
        if 31415 in output:
            return 0
        else:
            return -10 * (1 / abs(max(output)) + 1)
    except Exception as e:
        # print(e)
        return -1000


def fitness_function_4(program):
    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        visitor = ExprVisitor()
        output = visitor.visit(tree)
        # print("Output: ", output)
        if output[0] == 1:
            return 0
        else:
            return -10 * (abs(min(output)) + 1)
    except Exception as e:
        # print(e)
        return -1000

def fitness_function_5(program):
    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        visitor = ExprVisitor()
        output = visitor.visit(tree)
        # print("Output: ", output)
        if output[0] == 789:
            return 0
        else:
            return -10 * (abs(min(output)) + 1)
    except Exception as e:
        # print(e)
        return -1000

def fitness_function_6(program):
    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        visitor = ExprVisitor()
        output = visitor.visit(tree)
        # print("Output: ", output)
        if output[0] == 1 and len(output) == 1:
            return 0
        elif len(output) == 1:
            return -10 * (abs(min(output)) + 1)
        else:
            return -100 * (abs(min(output)) + 1)
    except Exception as e:
        # print(e)
        return -1000


def visualize_fitness(generations, avg_fitness, best_fitness, stats, ex="", success=True,
                      save_path='gp/output/fitness_visualization.png'):
    plt.figure(figsize=(8, 6))

    paragraph = ex + "\n" + stats

    plt.figtext(0.5, 0.95, paragraph, wrap=True, horizontalalignment='center', fontsize=10)

    plt.scatter(generations, avg_fitness, color='blue', label='Average Fitness', marker='.')
    plt.scatter(generations, best_fitness, color='orange', label='Best Fitness', marker='.')

    plt.title("Solved" if success else "Not Solved")
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.legend()

    plt.savefig(save_path, bbox_inches='tight')
    plt.show()


def test(function, ex: str, filename):
    gp = BiggerGP()
    stats = gp.evolve(function)
    gen = [stat.generation for stat in stats]
    best_fit = [stat.best_fitness for stat in stats]
    avg_fit = [stat.avg_fitness for stat in stats]
    visualize_fitness(gen, avg_fit, best_fit, stats[-1].to_string(), ex, stats[-1].solved, 'gp/output/'+filename+'.png')


if __name__ == '__main__':
    #test(fitness_function_1, "Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) "
    #                       "liczbę 1. Poza liczbą 1 może też zwrócić inne liczby.", "1.1.A")
    test(fitness_function_2, "Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) "
                             "liczbę 789. Poza liczbą 789 może też zwrócić inne liczby.", "1.1.B")
    #test(fitness_function_3, "Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) "
    #                         "liczbę 31415. Poza liczbą 31415 może też zwrócić inne liczby.", "1.1.C")
    #test(fitness_function_4, "Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 1. "
    #                         "Poza liczbą 1 może też zwrócić inne liczby.", "1.1.D")
    #test(fitness_function_5, "Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 789. "
    #                         "Poza liczbą 789 może też zwrócić inne liczby.", "1.1.E")
    #test(fitness_function_6, "Program powinien wygenerować na wyjściu liczbę jako jedyną liczbę 1. "
    #                         "Poza liczbą 1 NIE powinien nic więcej wygenerować.", "1.1.F")