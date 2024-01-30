import time

from antlr4 import *
from gen.ExprLexer import ExprLexer
from gen.ExprParser import ExprParser
from gen.ExprVisitor import ExprVisitor
from gp.BiggerGP import BiggerGP
import matplotlib.pyplot as plt
import re


def fitness_function_1(program):
    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        visitor = ExprVisitor()
        output, _ = visitor.visit(tree)
        # print("Output: ", output)
        if 1 in output:
            return 0
        else:
            return -10 * (abs(min(output)) + 1)
    except Exception as e:
        print("------------------------------------------")
        print(e)
        print(program)
        print("------------------------------------------")
        return -1000


def fitness_function_2(program):
    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        visitor = ExprVisitor()
        output, _ = visitor.visit(tree)
        # print("Output: ", output)
        if 789 in output:
            return 0
        else:
            if len(output) == 0:
                return -10000
            else:
                return -10 * (sum([abs(x - 789) for x in output]) / 10 + 1)
    except TypeError as e:
        return -1000


def fitness_function_3(program):
    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        visitor = ExprVisitor()
        output, _ = visitor.visit(tree)
        # print("Output: ", output)
        if 31415 in output:
            return 0
        else:
            if len(output) == 0:
                return -1000
            else:
                return min(-10 * (min([abs(abs(x) - 31415) for x in output]) + 1), -1000)
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
        output, _ = visitor.visit(tree)
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
        output, _ = visitor.visit(tree)
        # print("Output: ", output)
        if output[0] == 789:
            return 0
        else:
            if len(output) == 0:
                return -10000
            else:
                return -10 * (abs(output[0] - 789) / 100 + 1)
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
        output, _ = visitor.visit(tree)
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


def fitness_function_7(program):
    fitness = 0
    value = -1000
    checks = 1
    inputs_count = program.count("input()")
    if inputs_count == 2:
         value += 100
         checks += 1
    else:
        return -1000
    split_program = program.split(".")
    if "input()" in split_program[0] and "input()" in split_program[1]:
        value += 500
        checks += 1
    if any(["print" in x and "+" in x for x in split_program[1:]]):
        value += 200
        checks += 1
    value = value/checks

    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        num_readings = program.count("input()")
        for _ in range(4):
            visitor = ExprVisitor(20, -9, 9)
            output, program_input = visitor.visit(tree)
            # print("Output: ", output)
            if output[0] == program_input[0] + program_input[1] and num_readings == 2 and len(output) == 1:
                print("inputs:", program_input)
                print("Outputs: ", output )
                fitness += 0
            elif len(output) == 1:
                fitness += (value - len(program)/10000)
            else:
                fitness += 2*(value - len(program)/10000)
        return fitness
    except Exception as e:
        # print(e)
        return 8*(value - len(program)/10000)


def fitness_function_8(program):
    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        visitor = ExprVisitor()
        output, input = visitor.visit(tree)
        num_readings = program.count("input()")

        # print("Output: ", output)
        if output[0] == input[0] - input[1] and num_readings == 2 and len(output) == 1:
            return 0
        elif len(output) == 1:
            return max(-10 * (num_readings + abs(abs(output[0]) - (input[0] - input[1])) + 1), -100)
        else:
            return -1000
    except Exception as e:
        # print(e)
        return -1000


def fitness_function_9(program):
    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        visitor = ExprVisitor()
        output, input = visitor.visit(tree)
        num_readings = program.count("input()")

        # print("Output: ", output)
        if output[0] == max(input[0], input[1]) and num_readings == 2 and len(output) == 1:
            return 0
        elif len(output) == 1:
            return max(-10 * (num_readings * abs(abs(output[0]) - max(input[0], input[1])) + 1), -100)
        else:
            return -1000
    except Exception as e:
        # print(e)
        return -1000


def check_for_variables(program):
    pattern = re.compile(r'print\(([^)]+)\)')

    # Find all matches in the input string
    matches = pattern.findall(program)

    # Check if there are any letters in <something> for each match
    for match in matches:
        if any(c.isalpha() for c in match):
            return 0

    return 20


def benchmark1(program):
    try:
        #print(program)
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        visitor = ExprVisitor()
        fitness = 0
        for _ in range(3):
            output, program_input = visitor.visit(tree)
            num_readings = program.count("input()")

            # print("Output: ", output)
            if output[0] == program_input[0] + program_input[1] / program_input[2] and num_readings == 3 and len(
                    output) == 1:
                fitness += 0
            elif len(output) == 1 or num_readings == 3:
                fitness += max(-10 * (num_readings * abs(
                    abs(output[0]) - (program_input[0] + program_input[1] / program_input[2])) + 1
                                      + check_for_variables(program)), -100)
            else:
                fitness += -1000
        return fitness
    except Exception as e:
        # print(e)
        return -1000

def benchmark2(program):
    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        visitor = ExprVisitor()
        fitness = 0
        if program.count("while") == 0:
            return -10_000
        for _ in range(3):
            output, inputs = visitor.visit(tree)
            num_reading = program.count("input()")
            proper_value = 0
            for i in range(1, inputs[0] + 1):
                proper_value += i**2

            if num_reading == 1 and proper_value in output:
                print("Inputs: ", inputs)
                print("Outputs:", output)
                print("Proper val: ", proper_value)
                fitness += 0
            else:
                fitness += (-1 * abs(output[0] - proper_value) - 100)
        return fitness
    except Exception as e:
        # print(e)
        # print(program)
        return -10_000


def benchmark3(program):
    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        visitor = ExprVisitor()
        fitness = 0
        for _ in range(3):
            output, program_input = visitor.visit(tree)
            num_readings = program.count("input()")

            # print("Output: ", output)
            if output[0] == min(program_input) and num_readings == 4 and len(
                    output) == 1:
                fitness += 0
            elif len(output) == 1 or num_readings == 4:
                fitness += max(-10 * (num_readings * abs(
                    abs(output[0]) - min(program_input)) + 1 + check_for_variables(program)), -100)
            else:
                fitness += -1000
        return fitness
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
    visualize_fitness(gen, avg_fit, best_fit, stats[-1].to_string(), ex, stats[-1].solved,
                      'gp/output/' + filename + '.png')


if __name__ == '__main__':
    # test(fitness_function_1, "Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) "
    #                       "liczbę 1. Poza liczbą 1 może też zwrócić inne liczby.", "1.1.A")
    # test(fitness_function_2, "Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) "
    #                         "liczbę 789. Poza liczbą 789 może też zwrócić inne liczby.", "1.1.B")
    # test(fitness_function_3, "Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) "
    #                         "liczbę 31415. Poza liczbą 31415 może też zwrócić inne liczby.", "1.1.C")
    # test(fitness_function_4, "Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 1. "
    #                         "Poza liczbą 1 może też zwrócić inne liczby.", "1.1.D")
    # test(fitness_function_5, "Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 789. "
    #                         "Poza liczbą 789 może też zwrócić inne liczby.", "1.1.E")
    # test(fitness_function_6, "Program powinien wygenerować na wyjściu liczbę jako jedyną liczbę 1. "
    #                         "Poza liczbą 1 NIE powinien nic więcej wygenerować.", "1.1.F")
    test(fitness_function_7, "Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu "
                            "(jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9]",
        "1.2.A")
    #test(fitness_function_7, "Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu "
    #                        "(jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby w zakresie [-9,9]", "1.2.B")
    # test(fitness_function_7, "Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu "
    #                         "(jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]",
    #     "1.2.C")
    # test(fitness_function_8, "Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu "
    #                         "(jedynie) ich różnicę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]",
    #     "1.2.D")
    # test(fitness_function_8, "Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu "
    #                         "(jedynie) ich iloczyn. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]",
    #     "1.2.E")
    # test(fitness_function_9, "Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie)"
    #                         " większą z nich. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9]",
    #     "1.3.A")
    # test(benchmark1, "Given an integer and a float, print their sum", "B.1")
    # test(benchmark3, "Given 4 integers, print smallest of them", "28/ C.3")
    # test(benchmark2, "Given the integer n, return the sum of squaring each integer in range[1, n]", "B.3_17")

    #program = ("E = input() . \n" + "M = input() . \n" + "while ( M < E / E && M + M - M != E / M && M != M && M != E ) { \n "
    #           + "print ( 995 ) . \n" + "\n") + "} . \n" + "print ( M + E ) . \n"
    #print(fitness_function_7(program))
