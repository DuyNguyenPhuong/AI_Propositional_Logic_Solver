import SATSolver as SatSolver

"""
Call A is 1, B is 2, C is 3

A: Amy is truth-teller
B: Bob is truth-teller
C: Cal is truth-teller
"""

clauses = [[-1,3],[-2,-3],[2,3],[-1,2,-3],[-2,3],[1,3]]
# Check to see if a particular knowledge base is satisfiable.
print('Knowledge base is satisfiable:',SatSolver.testKb(clauses))

# Check to see Amy is a truth-teller
print('Is Amy a truth-teller?', end=' ')
result = SatSolver.testLiteral(1,clauses)
if result==True:
    print('Yes.')
elif result==False:
    print('No.')
else:
    print('Unknown.')


# Check to see Bob is a truth-teller
print('Is Bob a truth-teller?', end=' ')
result = SatSolver.testLiteral(2,clauses)
if result==True:
    print('Yes.')
elif result==False:
    print('No.')
else:
    print('Unknown.')

# Check to see Cal is a truth-teller
print('Is Cal a truth-teller?', end=' ')
result = SatSolver.testLiteral(3,clauses)
if result==True:
    print('Yes.')
elif result==False:
    print('No.')
else:
    print('Unknown.')

