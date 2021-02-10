from flask import Blueprint, request
from flask.json import jsonify
import json
import CSP_Solver as CS
import time

api = Blueprint('api', __name__)

def get_constraint(format, constraint):
    if format == 'python':
        constraint = 'def task_constraint():\n    ' + constraint.replace('\n', '\n    ') + '\nn_constraint = task_constraint()'
        _locals = locals()
        exec(constraint, globals(), _locals)
        constraint = _locals['n_constraint']
        return [C.strip() for C in constraint.split(';')]
    return [C.strip() for C in constraint.split('\n')]

def domain_change(D):
    D = D.replace('domain', 'task.separateDomain')
    D = D.replace('=', ',')
    pos_op = D.find('[')
    D = D[:pos_op] + '(' + D[pos_op + 1:]
    pos_op = D.find(']')
    return D[:pos_op] + D[pos_op + 1:] + ')'

def get_domain(format, domain):
    if format == 'python':
        domain = 'def task_domain():\n    ' + domain.replace('\n', '\n    ') + '\nn_domain = task_domain()'
        _locals = locals()
        exec(domain, globals(), _locals)
        domain = _locals['n_domain']
        return [domain_change(D.strip()) for D in domain.split(';')]
    return [domain_change(D.strip()) for D in domain.split('\n')]
    

def get_class(variables, format, constraint, domain):
    task = CS.CSP(variables=variables)
    constraint = get_constraint(format, constraint)
    for C in constraint:
        if C: task.addConstraint(C)
    domain = get_domain(format, domain)
    for D in domain:
        if D: exec(D)
    return task

@api.route('/')
def message():
    return "Working fine"

@api.route('/api/<variables>/<algorithm>/<format>/')
def get_solution(variables, algorithm, format):
    try:
        start = time.time()
        variables = int(variables)
        constraint = request.args.get('constraint')
        domain = request.args.get('domain')
        task = get_class(variables=variables, format=format, constraint=constraint, domain=domain)
        algorithm = f'task.{algorithm}(timeout=5)'
        exec(algorithm)
        end = time.time()
        solution = ''
        for i in range(1, variables + 1):
            solution += f'value[{task.variableConversion[i]}] = {task.value[i]}\n'
        done = task.stop
        timed_out = end - start > 5
        response = jsonify({'solution': solution, 'done': done, 'timed_out': timed_out})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response
    except:
        response = jsonify({"message": "Please check the input..."})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 400
