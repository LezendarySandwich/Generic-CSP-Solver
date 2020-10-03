from .Hill_Climbing import HillClimbing
from .Hill_Climbing_chooseRandom import HillClimbing_chooseRandom
from .Hill_Climbing_greedyBias import HillClimbing_greedyBias
from .Hill_Climbing_Util import choice
from CSP_Solver.Util import big

def Hill_Climbing_with_restarts(obj, memoisation = False, allowedSideMoves = 0, choice = choice.chooseBest, tabuSize = 0, iterations = big):
    if memoisation:
        known = dict()
    else :
        known = None
    if choice == choice.chooseBest:
        while not HillClimbing(obj, known = known, allowedSideMoves = allowedSideMoves, tabuSize = tabuSize, iterations=iterations):
            pass
    elif choice == choice.chooseRandom:
        while not HillClimbing_chooseRandom(obj, known = known, allowedSideMoves = allowedSideMoves, tabuSize=tabuSize, iterations=iterations):
            pass
    elif choice == choice.greedyBias:
        while not HillClimbing_greedyBias(obj, known = known, allowedSideMoves = allowedSideMoves, tabuSize=tabuSize, iterations=iterations):
            pass