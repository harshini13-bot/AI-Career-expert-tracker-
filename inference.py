from rules import rules

def forward_chaining(facts):

    inferred = set(facts)

    reasoning_steps = []

    changed = True

    while changed:

        changed = False

        for rule in rules:

            conditions = set(rule["conditions"])

            conclusion = rule["conclusion"]

            if conditions.issubset(inferred):

                if conclusion not in inferred:

                    inferred.add(conclusion)

                    reasoning_steps.append(
                        f"IF {', '.join(rule['conditions'])} THEN {conclusion}"
                    )

                    changed = True

    return inferred, reasoning_steps