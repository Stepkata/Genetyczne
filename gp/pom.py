if __name__ == '__main__':
    expected_rules = {
        'prog': ['expr NEWLINE'],
        'expr': ['print COLON', 'if_statement COLON', 'variable_assign COLON', 'while COLON', 'NEWLINE'],
        'variable_assign': ['IDENTIFIER EQ literals', 'IDENTIFIER EQ INPUT'],
        'print': ['PRINT LPAREN literals RPAREN'],
        'operators': ['MULTIPLY', 'DIVIDE', 'ADD', 'MOD', 'SUBSTRACT'],
        'logic_operators': ['AND', 'OR'],
        'literals': ['IDENTIFIER', 'INTLITERAL', 'literals operators literals'],
        'comparisson_type': ['EQEQ', 'GTHAN', 'LTHAN', 'NOTEQ'],
        'if_statement': ['IF LPAREN condition RPAREN LCURL NEWLINE expr NEWLINE RCURL'],
        'condition': ['literals comparisson_type literals', 'condition logic_operators condition'],
        'while': ['WHILE LPAREN  condition RPAREN LCURL NEWLINE  expr NEWLINE  RCURL']
    }

    your_rules = {
        0: [[1, 1900]],
        1: [[3, 2400], [8, 2400], [2, 2400], [10, 2400], [1900]],
        2: [[2100, 600, 6], [2100, 600, 2300]],
        3: [[2000, 700, 6, 800]],
        4: [[300], [400], [100], [500], [200]],
        5: [[1500], [1600]],
        6: [[2100], [2200], [6, 4, 6]],
        7: [[1300], [1200], [1100], [1400]],
        8: [[1700, 700, 9, 800, 900, 1900, 1, 1900, 1000]],
        9: [[6, 7, 6], [9, 5, 9]],
        10: [[1800, 700, 9, 800, 900, 1900, 1, 1900, 1000]]
    }

    terms = {'WS': 0,
             'ADD': 100,
             'SUBSTRACT': 200,
             'MULTIPLY': 300,
             'DIVIDE': 400,
             'MOD': 500,
             'EQ': 600,
             'LPAREN': 700,
             'RPAREN': 800,
             'LCURL': 900,
             'RCURL': 1000,
             'LTHAN': 1100,
             'GTHAN': 1200,
             'EQEQ': 1300,
             'NOTEQ': 1400,
             'AND': 1500,
             'OR': 1600,
             'IF': 1700,
             'WHILE': 1800,
             'NEWLINE': 1900,
             'PRINT': 2000,
             'IDENTIFIER': 2100,
             'INTLITERAL': 2200,
             'INPUT': 2300,
             'COLON': 2400}
    rules = {'prog': 0,
             'expr': 1,
             'variable_assign': 2,
             'print': 3,
             'operators': 4,
             'logic_operators': 5,
             'literals': 6,
             'comparisson_type': 7,
             'if_statement': 8,
             'condition': 9,
             'while': 10}

    reversed_terms = {v: k for k, v in terms.items()}
    reversed_rules = {v: k for k, v in rules.items()}

    # Print reversed dictionaries
    print("Reversed Terms:")
    print(reversed_terms)

    print("\nReversed Rules:")
    print(reversed_rules)

    buffer = {}
    for r, t in your_rules.items():
        pom = []
        for item in t:
            help = []
            for i in item:
                if i in reversed_rules.keys():
                    help.append(reversed_rules[i])
                else:
                    help.append(reversed_terms[i])
            pom.append(help)
        buffer[reversed_rules[r]] = help

    print("Result:")
    print(buffer)