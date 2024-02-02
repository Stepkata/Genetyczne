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
            visitor = ExprVisitor(20, -9999, 9999)
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
    if any(["print" in x and "-" in x for x in split_program[1:]]):
        value += 200
        checks += 1
    value = value / checks

    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        num_readings = program.count("input()")
        for _ in range(4):
            visitor = ExprVisitor(20, -9999, 9999)
            output, program_input = visitor.visit(tree)
            # print("Output: ", output)
            if output[0] == program_input[0] - program_input[1] and num_readings == 2 and len(output) == 1:
                print("inputs:", program_input)
                print("Outputs: ", output)
                fitness += 0
            elif len(output) == 1:
                fitness += (value - len(program) / 10000)
            else:
                fitness += 2 * (value - len(program) / 10000)
        return fitness
    except Exception as e:
        # print(e)
        return 8 * (value - len(program) / 10000)


def fitness_function_9(program):
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
    if any(["print" in x and "*" in x for x in split_program[1:]]):
        value += 200
        checks += 1
    value = value / checks

    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        num_readings = program.count("input()")
        for _ in range(4):
            visitor = ExprVisitor(20, -9999, 9999)
            output, program_input = visitor.visit(tree)
            # print("Output: ", output)
            if output[0] == program_input[0] * program_input[1] and num_readings == 2 and len(output) == 1:
                print("inputs:", program_input)
                print("Outputs: ", output)
                fitness += 0
            elif len(output) == 1:
                fitness += (value - len(program) / 10000)
            else:
                fitness += 2 * (value - len(program) / 10000)
        return fitness
    except Exception as e:
        # print(e)
        return 8 * (value - len(program) / 10000)

def fitness_function_10(program):
    fitness = 0
    value = -1500
    checks = 1
    inputs_count = program.count("input()")
    if inputs_count == 2:
        value += 100
        checks += 1
    else:
        return -3000
    split_program = program.split(".")
    variables = [line[0] for line in split_program if "input()" in line]
    if len(variables) != 2:
        raise ValueError("wt")
    if "input()" in split_program[0] and "input()" in split_program[1]:
        value += 500
        checks += 1
    if any([("<" in x or ">" in x) and all([v in x for v in variables]) for x in split_program[1:]]):
        value += 100
        checks += 1
    if any([variables[0] in x and variables[1] in x and "=" in x and "while" not in x and "if" not in x for x in split_program[1:]]):
        value += 500
        checks += 1
    if any(["print" in x for x in split_program[1:]]):
        value += 100
        checks += 1
    if any(["print" in x and (variables[0] in x or variables[1] in x )for x in split_program[1:]]):
        value += 100
        checks += 1
    value = value / checks

    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        num_readings = program.count("input()")
        for _ in range(15):
            visitor = ExprVisitor(20, 0, 9)
            output, program_input = visitor.visit(tree)
            # print("Output: ", output)
            if output[0] == max(program_input[0], program_input[1]) and num_readings == 2 and len(output) == 1 and checks == 7:
                print("inputs:", program_input)
                print("Outputs: ", output)
                fitness += 0
            elif len(output) == 1:
                fitness += (value - len(program) / 10000)
            else:
                fitness += 2 * (value - len(program) / 10000)
        return fitness
    except Exception as e:
        # print(e)
        return 8 * (value - len(program) / 10000)


def fitness_function_11(program):
    fitness = 0
    value = -2500
    checks = 1
    inputs_count = program.count("input()")
    value += max(inputs_count*100, 1000)
    split_program = program.split(".")
    variables = [line[0] for line in split_program if "input()" in line]
    if all(["input()" in x for x in split_program[:10]]):
        value += 500
        checks += 1
    if any(["=" in x and "+" in x and all([v in x for v in variables]) and "while" not in x and "if" not in x for x in split_program[10:]]):
        value += 500
        checks += 1
    for line in split_program:
        value += line.count("+")
    if any(["print" in x for x in split_program[10:]]):
        value += 100
        checks += 1
    value = value / checks

    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        num_readings = program.count("input()")
        for _ in range(15):
            visitor = ExprVisitor(20, -99, 99)
            output, program_input = visitor.visit(tree)
            if output[0] == sum(program_input) and num_readings == 10 and len(output) == 1:
                print("inputs:", program_input)
                print("Outputs: ", output)
                fitness += 0
            elif len(output) == 1:
                fitness += (value - len(program) / 10000)
            else:
                fitness += 2 * (value - len(program) / 10000)
        return fitness
    except Exception as e:
        print(e)
        return 8 * (value - len(program) / 10000)


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
    fitness = 0
    value = -1500
    inputs_count = program.count("input()")
    if inputs_count == 3:
        value += 100
    split_program = program.split(".")
    variables = [line[0] for line in split_program if "input()" in line]
    if "input()" in split_program[0] and "input()" in split_program[1] and "input()" in split_program[2]:
        value += 600
    if any(["print" in x and "/" in x for x in split_program[2:]]):
        value += 100
    if any(["print" in x and "+" in x for x in split_program[2:]]):
        value += 100
    if any(["print" in x and "+" in x and "/" in x for x in split_program[2:]]):
        value += 200
    if any(all(v in x for v in variables) and "print" in x for x in split_program[2:]):
        value += 100
    index = 0
    for i in range(0, len(split_program)-1):
        if "print" in split_program[i]:
            index = i
            break
    value = value - index

    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        num_readings = program.count("input()")
        for _ in range(8):
            visitor = ExprVisitor(20, 1, 9)
            output, program_input = visitor.visit(tree)

            if output[0] == sum(program_input) and num_readings == 3 and len(output) == 1:
                print("inputs:", program_input)
                print("Outputs: ", output)
                fitness += 0
            elif len(output) == 1:
                fitness += (value - len(program) / 10000)
            else:
                fitness += 2 * (value - len(program) / 10000)
        return fitness
    except Exception as e:
        # print(e)
        return 8 * (value - len(program) / 10000)

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
    fitness = 0
    value = -1500
    checks = 1
    inputs_count = program.count("input()")
    if inputs_count == 1:
        value += 100
        checks += 1
    else:
        return -1500
    split_program = program.split(".")
    variables = [line[0] for line in split_program if "input()" in line]
    if "input()" in split_program[0] and "= 0" in split_program[1]:
        value += 400
        checks += 1
    if any(["while" in x for x in split_program[2:]]):
        value += 100
        checks += 1
    if any(["print" in x for x in split_program[2:]]):
        value += 100
        checks += 1
    if any(["input()" in x for x in split_program[2:]]):
        value += 100
        checks += 1
    if any([any([v in x for v in variables]) and "=" in x and "+ 1" in x for x in split_program[2:]]):
        value += 100
        checks += 1
    value = value / checks

    try:
        lexer = ExprLexer(InputStream(program))
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        num_readings = program.count("input()")
        for _ in range(4):
            visitor = ExprVisitor(20, 1, 9)
            output, program_input = visitor.visit(tree)

            if output == [x*x for x in range(1, program_input[0]+1)] and num_readings == 1 and len(
                    output) == program_input[0]:
                print("inputs:", program_input)
                print("Outputs: ", output)
                fitness += 0
            elif len(output) == 1:
                fitness += (value - len(program) / 10000)
            else:
                fitness += 2 * (value - len(program) / 10000)
        return fitness
    except Exception as e:
        # print(e)
        return 8 * (value - len(program) / 10000)


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
    #test(fitness_function_7, "Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu "
    #                        "(jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9]",
    #    "1.2.A")
    #test(fitness_function_7, "Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu "
    #                        "(jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby w zakresie [-9,9]", "1.2.B")
    #test(fitness_function_7, "Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu "
    #                         "(jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby w zakresie [-9999,9999]",
    #     "1.2.C")
    #test(fitness_function_8, "Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu "
    #                        "(jedynie) ich różnicę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]",
    #    "1.2.D")
    #test(fitness_function_9, "Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu "
    #                         "(jedynie) ich iloczyn. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]",
    #     "1.2.E")
    test(fitness_function_10, "Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie)"
                             " większą z nich. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9]",
         "1.3.A")
    #test(fitness_function_10, "Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie)"
    #                          " większą z nich. Na wejściu mogą być tylko całkowite liczby w zakresie [-9999,9999]",
    #     "1.3.B")
    #test(fitness_function_11, "Program powinien odczytać dziesięć pierwszych liczy z wejścia i zwrócić na wyjściu ("
    #                          "jedynie) ich średnią arytmetyczną (zaokrągloną do pełnej liczby całkowitej). Na "
    #                          "wejściu mogą być tylko całkowite liczby w zakresie [-99,99]",
    #     "1.4.A")
    # test(benchmark1, "Given an integer and a float, print their sum", "B.1")
    # test(benchmark3, "Given 4 integers, print smallest of them", "28/ C.3")
    #test(benchmark2, "Given the integer n, return the sum of squaring each integer in range[1, n]", "B.3_17")
    # test(benchmark3, "Given the integer n, return the vector of squaring each integer in range[1, n]", "B.O_1")

    #print(fitness_function_11("A = input(). \n B = input(). \n C = input(). \n P = input(). \n D = input(). \n F = "
    #                          "input(). \n G = input(). \n Z = input() .\n J = input(). \n I = input(). \n a = A + B + "
    #                          "C + D + F + G + Z + P + J + I. \n print(a). \n"))
    pass
