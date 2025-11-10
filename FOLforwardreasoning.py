# Forward Reasoning (FOL-style) using IF–THEN rules (case-insensitive)

def is_variable(x):
    return x.lower() in ['x', 'y', 'z'] or x.isupper()

def match(pattern, fact):
    p_pred, p_arg = pattern.split("(")[0].strip(), pattern.split("(")[1][:-1].strip()
    f_pred, f_arg = fact.split("(")[0].strip(), fact.split("(")[1][:-1].strip()
    if p_pred.lower() != f_pred.lower(): 
        return None
    if is_variable(p_arg): 
        return {p_arg: f_arg}
    return {} if p_arg == f_arg else None

def substitute(expr, subst):
    pred, arg = expr.split("(")[0].strip(), expr.split("(")[1][:-1].strip()
    if arg in subst: 
        arg = subst[arg]
    return f"{pred}({arg})"

def forward_reasoning(facts, rules, query):
    derived = set(facts)
    added = True
    while added:
        added = False
        for cond, concl in rules:
            for f in list(derived):
                subst = match(cond, f)
                if subst:
                    new_fact = substitute(concl, subst)
                    if new_fact not in derived:
                        print("Derived:", new_fact)
                        derived.add(new_fact)
                        added = True
    print("\nAll facts:", derived)
    if query in derived:
        print(f" Query '{query}' is proved true!")
    else:
        print(f" Query '{query}' cannot be proved.")

# --- Input section ---
facts = []
n = int(input("Enter number of facts: "))
for i in range(n):
    facts.append(input(f"Fact {i+1}: ").strip())

rules = []
m = int(input("\nEnter number of rules: "))
for i in range(m):
    print(f"Rule {i+1} format: IF condition THEN conclusion")
    rule = input(f"Rule {i+1}: ").strip()
    rule = rule.replace("if", "IF").replace("then", "THEN")
    cond = rule.split("IF")[1].split("THEN")[0].strip()
    concl = rule.split("THEN")[1].strip()
    rules.append((cond, concl))

query = input("\nEnter query: ").strip()

# --- Run reasoning ---
forward_reasoning(facts, rules, query)
