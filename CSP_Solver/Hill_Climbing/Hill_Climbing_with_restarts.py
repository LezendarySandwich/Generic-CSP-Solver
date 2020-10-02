import enum
from .Hill_Climbing import HillClimbing
from .Hill_Climbing_with_memoisation import HillClimbing_with_memoisation
from .Hill_Climbing_choose_random_with_memoisation import HillClimbing_choose_random_with_memoisation
from .Hill_Climbing_greedyBias_with_memoisation import HillClimbing_greedyBias_with_memoisation
from CSP_Solver.Util import big

class choice(enum.Enum):
    chooseBest = 1
    chooseRandom = 2
    greedyBias = 3

def Hill_Climbing_with_restarts(obj, memoisation = False, allowedSideMoves = 0, choice = choice.chooseBest, tabuSize = 0, iterations = big):
    if choice == choice.chooseBest:
        if memoisation:
            known = dict()
            while not HillClimbing_with_memoisation(obj, known = known, allowedSideMoves = allowedSideMoves, tabuSize = tabuSize, iterations=iterations):
                pass
        else:
            while not HillClimbing(obj, allowedSideMoves, iterations = iterations, tabuSize=tabuSize):
                pass
    elif choice == choice.chooseRandom:
        known = dict()
        while not HillClimbing_choose_random_with_memoisation(obj, known = known, allowedSideMoves = allowedSideMoves, tabuSize=tabuSize, iterations=iterations):
            pass
    elif choice == choice.greedyBias:
        known = dict()
        while not HillClimbing_greedyBias_with_memoisation(obj, known = known, allowedSideMoves = allowedSideMoves, tabuSize=tabuSize, iterations=iterations):
            pass