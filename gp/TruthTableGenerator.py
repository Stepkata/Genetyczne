class TruthTableGenerator:
    def __init__(self):
        pass

    def and_truth_table(self, num_variables: int) -> list:
        if num_variables <= 0:
            raise ValueError("Number of variables should be greater than 0")

        truth_table = []
        for i in range(2 ** num_variables):
            binary_representation = bin(i)[2:].zfill(num_variables)
            row = [int(bit) for bit in binary_representation]
            result = all(row)
            truth_table.append(row + [int(result)])

        return truth_table

    def or_truth_table(self, num_variables: int) -> list:
        if num_variables <= 0:
            raise ValueError("Number of variables should be greater than 0")

        truth_table = []
        for i in range(2 ** num_variables):
            binary_representation = bin(i)[2:].zfill(num_variables)
            row = [int(bit) for bit in binary_representation]
            result = any(row)
            truth_table.append(row + [int(result)])

        return truth_table

    def xor_truth_table(self, num_variables: int) -> list:
        if num_variables <= 0:
            raise ValueError("Number of variables should be greater than 0")

        truth_table = []
        for i in range(2 ** num_variables):
            binary_representation = bin(i)[2:].zfill(num_variables)
            row = [int(bit) for bit in binary_representation]
            result = sum(row) % 2 == 1
            truth_table.append(row + [int(result)])

        return truth_table

if __name__ == "__main__":
    # Example usage:
    num_variables = 4
    t = TruthTableGenerator()
    result = t.or_truth_table(num_variables)
    print(f"Truth table for AND operation with {num_variables} variables:")
    for row in result:
        print(row)