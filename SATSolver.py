'''SATSolver.py - a simple Python interface to the zchaff SAT solver.
Originally by Todd Neller
Ported to Python and updated to pycryptosat by Dave Musicant

Copyright (C) 2019 Dave Musicant

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

Information about the GNU General Public License is available online at:
http://www.gnu.org/licenses/
To receive a copy of the GNU General Public License, write to the Free
Software Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
02111-1307, USA.
'''

import pycryptosat

def testKb(clauses):
    s = pycryptosat.Solver()
    s.add_clauses(clauses)
    
    sat, solution = s.solve()
    return sat

def testLiteral(literal,clauses):
    s = pycryptosat.Solver()
    s.add_clauses(clauses)
    
    sat, solution = s.solve([literal])
    if not sat:
        return False

    sat, solution = s.solve([-literal])
    if not sat:
        return True

    return None

if __name__ == '__main__':
    clauses = [[-1,-2],[2 ,1],[-2,-3],[3,2],[-3,-1],[-3, -2],[1,2,3]]
    print('Knowledge base is satisfiable:',testKb(clauses))
    print('Is Cal a truth-teller?', end=' ')
    result = testLiteral(3,clauses)
    if result==True:
        print('Yes.')
    elif result==False:
        print('No.')
    else:
        print('Unknown.')