from .Hill_Climbing import HillClimbing
from .Hill_Climbing_with_memoisation import HillClimbing_with_memoisation

def Hill_Climbing_with_restarts(obj, memoisation = False, allowedSideMoves = 0):
    if memoisation:
        known = dict()
        while not HillClimbing_with_memoisation(obj, known = known, allowedSideMoves = allowedSideMoves):
            pass
    else:
        while not HillClimbing(obj, allowedSideMoves):
            pass