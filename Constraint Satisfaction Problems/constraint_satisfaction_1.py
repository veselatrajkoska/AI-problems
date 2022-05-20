from constraint import *

if __name__ == '__main__':
    problem = Problem()
    n = int(input())
    queens = []
    domain = []
    for i in range(0, n):
        queens.append(i+1)
        for j in range(0, n):
            domain.append((i, j))

    problem.addVariables(queens, domain)

    for queen1 in queens:
        for queen2 in queens:
            if queen1 < queen2:
                problem.addConstraint(lambda q1, q2: q1[0] != q2[0] and q1[1] != q2[1] and abs(q1[0] - q2[0])
                                                     != abs(q1[1] - q2[1]), (queen1, queen2))

    if n <= 6:
        solutions = problem.getSolutions()
        print(len(solutions))
    else:
        print(problem.getSolution())
