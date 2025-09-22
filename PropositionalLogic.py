import itertools

def evaluate_expression(expression, assignment):
    expression = expression.replace('A', str(assignment[0]))
    expression = expression.replace('B', str(assignment[1]))
    expression = expression.replace('C', str(assignment[2]))
    expression = expression.replace('and', 'and').replace('or', 'or').replace('not', 'not')
    return eval(expression)

def check_entailment(alpha, kb):
    variables = ['A', 'B', 'C']
    all_assignments = list(itertools.product([False, True], repeat=len(variables)))

    print("Truth Table:")
    print("A\tB\tC\tKB\tα")
    for assignment in all_assignments:
        kb_result = evaluate_expression(kb, assignment)
        alpha_result = evaluate_expression(alpha, assignment)
        
        print(f"{assignment[0]}\t{assignment[1]}\t{assignment[2]}\t{kb_result}\t{alpha_result}")

        if kb_result and not alpha_result:
            return False 
    
    return True 

alpha = "A or B"
kb = "(A or C) and (B and not C)"

if check_entailment(alpha, kb):
    print("KB entails α")
else:
    print("KB does not entail α")
