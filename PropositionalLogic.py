import itertools

def evaluate_expression(expression, assignment):
    expression = expression.replace('P', str(assignment[0]))
    expression = expression.replace('Q', str(assignment[1]))
    expression = expression.replace('R', str(assignment[2]))
    expression = expression.replace('and', 'and').replace('or', 'or').replace('not', 'not').replace('implies', '<=')
    return eval(expression)

def generate_truth_table(expression):
    variables = ['P', 'Q', 'R']
    all_assignments = list(itertools.product([False, True], repeat=len(variables)))

    print(f"Truth Table for: {expression}")
    print("P\tQ\tR\tResult")
    for assignment in all_assignments:
        result = evaluate_expression(expression, assignment)
        print(f"{assignment[0]}\t{assignment[1]}\t{assignment[2]}\t{result}")

expression = "(P and (Q or not R)) or (not P implies Q)"
generate_truth_table(expression)
