
# Generic Constraint Satisfaction Problem Solver

CSP Solver is a library designed to provide the functionalities to solve contstraint satisfactions problems without the need of going through the hassle of writing the code to do so. As of now, it supports a variety of methods including but not restricted to Hill Climbing with greedy biasing, Arc Consistent backtracking etc. 

## Supported Methods!
> Depth first serch  
> solve_dfs(self: CSP, timeout: int)

> Backtracking  
> solve_BackTrack(self: CSP, timeout: int)

> Forward Checking  
> solve_ForwardChecking(self: CSP, timeout: int)

> Forward Checking with MRV ordering  
> solve_ForwardChecking_MRV(self: CSP, timeout: int)

> Forward checking with MRV & LCV ordering  
> solve_ForwardChecking_MRV_LCV(self:CSP, timeout:int)

> Classical Hill Climbing (Taking best available option)  
> solve_HillClimbing_chooseBest(self:CSP, memoization:bool, iterations:int, allowedSideMoves:int, tabuSize:int, timeout:int)

> Hill Climbing with random choice biased towards better choices  
> solve_HillClimbing_greedyBias(self:CSP, memoization:bool, iterations:int, allowedSideMoves:int, tabuSize:int, timeout:int)

> Hill Climbing with random choice  
> solve_HillClimbing_chooseRandom(self:CSP, memoization:bool, iterations:int, allowedSideMoves:int, tabuSize:int, timeout:int)

> Genetic Algorithm  
> solve_GeneticAlgo(self:CSP, populationSize:int, generations:int, timeout:int)

> Local beam search  
> solve_local_beam_search(self:CSP, beams:int, timeout:int)

> Simulated Annealing  
> solve_Simulated_Annealing(self:CSP, iterations:int, initialTemperature:int, cooling_coefficient:int, timeout:int)

> Arc consistent Backtracking  
> solve_ArcConsistent_BackTracking(self: CSP, timeout: int)

> Novel Approach  
> solve_novelAlgorithm(self, split:int, allowedSideMoves:int, tabuSize:int, tries:int, timeout:int)

> Run all methods on default parameters  
> testAllDefaultParams(self: CSP, timeout:int)

### Example
* *Initializing the class*
```python
import CSP_Solver as CS
task = CS.CSP(variables=..., solution_path=..., problem_name=...)
```
* *Adding constraints specifying domains*
```python
'''
Make sure that your constraint is python friendly
'''
task.addConstraint('value[1] != value[2]') # Example constraint
# You may use this if the domain is common for all variables
task.commonDomain(domain=[1,2,5,4]) 
# You may want to add constraints sperately
task.seperateDomain(variable=1,domain=[1,2]) 
# You may want to set value of some variable
task.setValue(variable=1, value=2)
task.testAllDefaultParams(timeout=10)
```
### Reports
* [Report](https://drive.google.com/file/d/1MkcQGpeX8d3Qng5sB2CW_B0oS5HVSeKy/view?usp=sharing)
* [Presentation](https://drive.google.com/file/d/1gMElklxYo2P_uIFUzBrgsuGk1OvaAOQR/view?usp=sharing)

### Installation
Install package from Pypi
```bash
$ pip install CSP-Solver
```

To test examples

```bash
$ git clone https://github.com/LezendarySandwich/Generic-CSP-Solver.git
$ cd Generic-CSP-Solver/Examples
$ python3 [Example]
```

### Test Functionality

https://csp-web.herokuapp.com/

License
----

MIT

