import sys
import Parser

if len(sys.argv) >= 2:
    filename = sys.argv[1]
    file = open(filename, 'r')
    content = file.read()
    problem = Parser.parse(content)
    problem.solve()
    print(problem.describe())
