def arithmetic_arranger(problems, print_ans=False):
    # define empty lists to store data
    operands_1 = []
    operands_2 = []
    operators = []

    # separate data to operands and operators
    for problem in problems:
        problem = problem.split()
        operands_1.append(problem[0])
        operators.append(problem[1])
        operands_2.append(problem[2])

    # get the maximum length of each operand
    max_lengths = [max(len(operand_1), len(operand_2)) for operand_1, operand_2 in zip(operands_1, operands_2)]
    # number of operations
    num_op = len(problems)

    # check for errors
    if num_op > 5:
        return "Error: Too many problems."

    if '*' in operators or '/' in operators:
        return "Error: Operator must be '+' or '-'."

    for operand_1, operand_2 in zip(operands_1, operands_2):
        if not operand_1.isdigit() or not operand_2.isdigit():
            return 'Error: Numbers must only contain digits.'
        elif len(operand_1) > 4 or len(operand_2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    # vertically arrange the problems
    arranged_problems = ''
    # first row
    for i in range(num_op):
        arranged_problems += operands_1[i].rjust(max_lengths[i] + 2)
        if i != num_op - 1:
            arranged_problems += '    '
    arranged_problems += '\n'
    # second row
    for i in range(num_op):
        arranged_problems += operators[i]
        arranged_problems += operands_2[i].rjust(max_lengths[i] + 1)
        if i != num_op - 1:
            arranged_problems += '    '
    arranged_problems += '\n'

    # third row
    for i in range(num_op):
        arranged_problems += ''.rjust(max_lengths[i] + 2, '-')
        if i != num_op - 1:
            arranged_problems += '    '

    # fourth row
    if print_ans:
        arranged_problems += '\n'
        for i in range(num_op):
            arranged_problems += str(eval(problems[i])).rjust(max_lengths[i] + 2)
            if i != num_op - 1:
                arranged_problems += '    '

    return arranged_problems