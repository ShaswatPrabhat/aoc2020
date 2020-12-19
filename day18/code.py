import re


class locals(int):
    def __mul__(self, b):
        return locals(int(self) + b)

    def __add__(self, b):
        return locals(int(self) + b)

    def __sub__(self, b):
        return locals(int(self) * b)


def evaluate_for_me(expression, pt2=False):
    expression = re.sub(r"(\d+)", r"locals(\1)", expression)
    expression = expression.replace("*", "-")
    if pt2:
        expression = expression.replace("+", "*")
    print(expression)
    return eval(expression, {}, {"locals": locals})


lines = open('input_test.txt', 'r').readlines()

print("Part 1:", sum(evaluate_for_me(lolu) for lolu in lines))

print("Part 2:", sum(evaluate_for_me(lolu, pt2=True) for lolu in lines))
