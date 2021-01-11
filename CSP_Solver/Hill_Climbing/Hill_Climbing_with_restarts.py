from .Hill_Climbing import HillClimbing
from .Hill_Climbing_chooseRandom import HillClimbing_chooseRandom
from .Hill_Climbing_greedyBias import HillClimbing_greedyBias
from .Hill_Climbing_Util import choice, big
from time import time

def Hill_Climbing_with_restarts(obj, memoization = False, allowedSideMoves = 0, choice = choice.chooseBest, tabuSize = 0, iterations = big, application = big, timeout = 1000):
    start = time()
    if memoization:
        known = dict()
    else :
        known = None
    if choice == choice.chooseBest:
        while application > 0:
            if time() - start > timeout:
                return False
            application -= 1
            if HillClimbing(obj, known = known, allowedSideMoves = allowedSideMoves, tabuSize = tabuSize, iterations=iterations):
                obj.stop = 1
                return True
    elif choice == choice.chooseRandom:
        while application > 0:
            if time() - start > timeout:
                return False
            application -= 1
            if HillClimbing_chooseRandom(obj, known = known, allowedSideMoves = allowedSideMoves, tabuSize=tabuSize, iterations=iterations):
                obj.stop = 1
                return True
    elif choice == choice.greedyBias:
        while application > 0:
            if time() - start > timeout:
                return False
            application -= 1
            if HillClimbing_greedyBias(obj, known = known, allowedSideMoves = allowedSideMoves, tabuSize=tabuSize, iterations=iterations):
                obj.stop = 1
                return True
    return False