import enum
from .Hill_Climbing import HillClimbing
from .Hill_Climbing_with_memoisation import HillClimbing_with_memoisation
from .Hill_Climbing_choose_random_with_memoisation import HillClimbing_choose_random_with_memoisation
class choice(enum.Enum):
    chooseBest = 1
    chooseRandom = 2

def Hill_Climbing_with_restarts(obj, memoisation = False, allowedSideMoves = 0, choice = choice.chooseBest):
    if choice == choice.chooseBest:
        if memoisation:
            known = dict()
            while not HillClimbing_with_memoisation(obj, known = known, allowedSideMoves = allowedSideMoves):
                pass
        else:
            while not HillClimbing(obj, allowedSideMoves):
                pass
    elif choice == choice.chooseRandom:
        known = dict()
        while not HillClimbing_choose_random_with_memoisation(obj, known = known, allowedSideMoves = allowedSideMoves):
            pass