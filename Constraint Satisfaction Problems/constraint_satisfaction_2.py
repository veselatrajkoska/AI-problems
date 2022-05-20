from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    domain = range(1, 10)
    variables = range(0, 81)
    problem.addVariables(variables, domain)

    for i in range(0, 81, 9):
        problem.addConstraint(AllDifferentConstraint(), range(i, i + 8))

    for i in range(0, 9):
        problem.addConstraint(AllDifferentConstraint(), range(i, i + 72, 9))

    for i in range(0, 9, 3):
        problem.addConstraint(AllDifferentConstraint(),
                              [i, i + 1, i + 2, i + 9, i + 10, i + 11, i + 18, i + 19, i + 20])

    for i in range(27, 36, 3):
        problem.addConstraint(AllDifferentConstraint(),
                              [i, i + 1, i + 2, i + 9, i + 10, i + 11, i + 18, i + 19, i + 20])

    for i in range(54, 63, 3):
        problem.addConstraint(AllDifferentConstraint(),
                              [i, i + 1, i + 2, i + 9, i + 10, i + 11, i + 18, i + 19, i + 20])

    print(problem.getSolution())
