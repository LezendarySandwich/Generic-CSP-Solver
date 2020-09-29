
from .verifySolution import verify

def dfs(obj, cur):
    if obj.stop:
        return 
    if cur > obj.variables:
        if verify(obj):
            obj.stop = 1
            print(obj.value[1:obj.variables+1])
        return
    for value in obj.domains[cur]:
        obj.value[cur] = value
        dfs(obj, cur + 1)