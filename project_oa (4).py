# -*- coding: utf-8 -*-
"""project OA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fj9DBA436xcVKqd_VEnu8OJrmWtP7qOn
"""

pip install scipy

pip install deap

import scipy
from scipy.optimize import Bounds

pip install numdifftools

from scipy.optimize import minimize
import numpy as np
from numdifftools import Jacobian
import time

import numpy as np
from scipy.optimize import minimize

#PROBLEM NUMBER ONE WITH OPTIMIZATION ALGORYTHM

def objective(x) :
  x1 = x[0]
  x2 = x[1]
  return (x1 - 3)**2 + (x2 - 2)**2
def constraint1(x):
  return x[0]**2-x[1]-3.0
def constraint2(x):
  return -x[1]+1
def constraint3(x):
  return x[0]
x0 = np.zeros(2)

con1 = { 'type':'ineq', 'fun': constraint1}
con2 = { 'type':'ineq', 'fun': constraint2}
con3 = { 'type':'ineq', 'fun': constraint3}
cons = [con1, con2, con3]

solution = minimize(objective,x0,method='SLSQP', constraints= cons)
print(solution)
print(solution.fun)



#PROBLEM NUMBER TWO
def objective(x) :
  x1 = x[0]
  x2 = x[1]
  return (x1 - 1.5)**2 + (x2 - 5)**2
def constraint1(x):
  return x[0]-x[1] +2
def constraint2(x):
  return -2*x[0] - 3*x[1] + 11
def constraint3(x):
  return x[0]
def constraint4(x):
  return x[1]

x0 = np.zeros(2)


con1 = { 'type':'ineq', 'fun': constraint1}
con2 = { 'type':'ineq', 'fun': constraint2}
con3 = { 'type':'ineq', 'fun': constraint3}
con4 = { 'type':'ineq', 'fun': constraint4}
cons = [con1, con2, con3,con4]

solution = minimize(objective,x0,method='SLSQP', constraints= cons)
print(solution)



from scipy.optimize import minimize
import numpy as np

def objective(x):
    x1 = x[0]
    x2 = x[1]
    return (x1 - 1)**2 + (x2 - 1)**2

def constraint1(x):
    return -(x[0] + x[1] - 1)**3

def constraint2(x):
    return x[0]

def constraint3(x):
    return x[1]

x0 = np.zeros(2)

con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'ineq', 'fun': constraint2}
con3 = {'type': 'ineq', 'fun': constraint3}
cons = [con1, con2, con3]

solution = minimize(objective, x0, method='SLSQP', constraints=cons)
print('Optimal Solution:')
print('x1:', solution.x[0], 'x2:', solution.x[1])
print('Objective Value:', solution.fun)



import numpy as np
from scipy.optimize import minimize
import math

def objective(x):
    return 1 + x[1]**2 - x[0] - 0.1 * np.sin(3 * np.pi * x[0])

def constraint1(x):
    return -x[0] + 0.226

# Initial guess
x0 = np.array([0.226, 0])  # Starting from the expected optimal solution
bounds = [(0, 1.0), (-2, 2)]
# Define constraint
constraint = {'type': 'ineq', 'fun': constraint1}

# Perform optimization
solution = minimize(objective, x0, method='SLSQP', constraints=[constraint])

# Print the solution
print("Solution:")
print("x1:", solution.x[0])
print("x2:", solution.x[1])
print("Objective value:", solution.fun)

import math

import numpy as np
from scipy.optimize import minimize
import math

def objective(x):
    return 1 + x[1]**2 - x[0] - 0.1 * np.sin(3 * math.pi * x[0])

def constraint1(x):
    return -x[0] + 0.226

# Define bounds for variables
bounds = [(0, 1.0), (-2, 2)]  # Bounds for x[0] and x[1]

# Initial guess (must be within bounds and feasible region)
x0 = np.array([0.1, 0])  # An initial guess within bounds and near the feasible region

# Define constraint
constraint = {'type': 'ineq', 'fun': constraint1}

# Perform optimization
solution = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=[constraint])

# Print the solution
print("Solution:")
print("x1:", solution.x[0])
print("x2:", solution.x[1])
print("Objective value:", solution.fun)



#PROBLEM NUMBER 4
import numpy as np
from scipy.optimize import minimize
import math

def objective(x):
    return 1 - x[0] + x[1]**2 - 0.1 * math.sin(3 * math.pi * x[0])

def constraint1(x):
    return -x[0] + 0.441  # Upper bound for 'a'

def constraint2(x):
    return x[0] - 0.226  # Lower bound for 'a'

# Define bounds for variables
bounds = [(0, 1.0), (-2, 2)]  # Bounds for x[0] and x[1]

# Define constraints for 'a'
constraints = [{'type': 'ineq', 'fun': constraint1}, {'type': 'ineq', 'fun': constraint2}]

# Initial guess
x0 = np.zeros(2)

# Perform optimization
solution = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=constraints)

# Print the solution
print("Solution:")
print(solution)



pip install math

import numpy as np
from scipy.optimize import minimize
from math import sqrt

# Objective function
def objective(x):
    h = x[0]
    l = x[1]
    t = x[2]
    b = x[3]
    return 1.0471 * h**2 * l + 0.04811 * t * b * (14.0 + l)

# Constraints
def constraint1(x):
    return -x[0] + 10  # Upper bound for 'h'

def constraint2(x):
    return x[0] - 0.125  # Lower bound for 'h'

def constraint3(x):
    return -x[1] + 10  # Upper bound for 'l'

def constraint4(x):
    return x[1] - 0.1  # Lower bound for 'l'

# Initial guess
initial_h = 1
initial_l = 1
initial_t = 1
initial_b = 1
x0 = np.array([initial_h, initial_l, initial_t, initial_b])

# Define constraints
cons1 = {'type': 'ineq', 'fun': constraint1}
cons2 = {'type': 'ineq', 'fun': constraint2}
cons3 = {'type': 'ineq', 'fun': constraint3}
cons4 = {'type': 'ineq', 'fun': constraint4}
cons = [cons1, cons2, cons3, cons4]

# Perform optimization
solution = minimize(objective, x0, method='SLSQP', constraints=cons)

# Print the solution
if solution.success:
    print("Solution:")
    print(solution.x)
else:
    print("No feasible solution found.")

import pandas

#PROBLEM NUMBER 5
import numpy as np
from scipy.optimize import minimize
from math import sqrt

def objective(x):
    h = x[0]
    l = x[1]
    t = x[2]
    b = x[3]
    s=t*b
    return 1.0471 * h**2 * l + 0.04811 * s * (14.0 + l)


def constraint1(x):
    return -x[0] + 10  # Upper bound for 'h'

def constraint2(x):
    return x[0] - 0.125  # Lower bound for 'h'

def constraint3(x):
    return -x[1] + 10  # Upper bound for 'l'

def constraint4(x):
    return x[1] - 0.1  # Lower bound for 'l'

def constraint5(x, tx):
    return tx + 13600

def constraint6(x, ax):
    return ax + 30000

def constraint7(x):
    return -x[0] + x[3]

def constraint8(x, pcx):
    return pcx + 6000

def constraint9(x, gx):
    return -gx + 0.25

# Initial guess
x0 = np.ones(4)  # Initialize with non-zero values

# Define calculations for constraints
t1x = lambda x: 6000 / (sqrt(2) * x[0] * x[1])
t2x = lambda x: (6000 * (14 + 0.5 * x[1]) * sqrt(0.25 * ((x[1]**2 + (x[0] + x[2])**2)))) / (2 * (0.707 * x[0] * x[1]) * (x[1]**2 / 12 + 0.25 * (x[0] + x[2])**2))
ax = lambda x: 504000 / x[2]**2 * x[3]
pcx = lambda x: 64746.022 * (1 - 0.0282346 * x[2]) * x[2] * x[3]**3
gx = lambda x: 2.195**2 / x[2]**3 * x[3]
tx = lambda x: sqrt((t1x(x)**2) + (t2x(x)**2) + x[1] * t1x(x) * t2x(x)) / sqrt(0.25 * (x[1]**2 + (x[0] + x[2])**2))

# Define constraints
cons1 = {'type': 'ineq', 'fun': constraint1}
cons2 = {'type': 'ineq', 'fun': constraint2}
cons3 = {'type': 'ineq', 'fun': constraint3}
cons4 = {'type': 'ineq', 'fun': constraint4}
cons5 = {'type': 'ineq', 'fun': lambda x: constraint5(x, tx(x))}
cons6 = {'type': 'ineq', 'fun': lambda x: constraint6(x, ax(x))}
cons7 = {'type': 'ineq', 'fun': constraint7}
cons8 = {'type': 'ineq', 'fun': lambda x: constraint8(x, pcx(x))}
cons9 = {'type': 'ineq', 'fun': lambda x: constraint9(x, gx(x))}

# Perform optimization
cons = [cons1, cons2, cons3, cons4, cons5, cons6, cons7, cons8, cons9]
solution = minimize(objective, x0, method='SLSQP', constraints=cons)

# Print the solution
print("Solution:")
print(solution)

pip install gekko

#PROBLEM NUMBER 6
from gekko import GEKKO
import numpy as np
import math

# Initialize model
m = GEKKO(remote=False)

# Define variable
x = m.Var(value=1, lb=0, ub=2)

# Define objective function
m.Maximize(abs(m.sin(math.pi * x)))

# Solve optimization problem
m.solve(disp=False)

# Extract results
max_value = abs(np.sin(math.pi * x.value[0]))

# Print results
print('Maximized value:', max_value)
print('Corresponding x:', x.value[0])

#PROBLEM NUMBER 6
from gekko import GEKKO
import numpy as np
import math

# Initialize model
m1 = GEKKO(remote=False)
m2 = GEKKO(remote=False)

# Define variable
x1 = m1.Var(value=0.1, lb=0, ub=2)
x2 = m2.Var(value=1.9, lb=0, ub=2)

# Define objective function
m1.Maximize(abs(m1.sin(math.pi * x1)))
m2.Maximize(abs(m2.sin(math.pi * x2)))

# Solve optimization problems
m1.solve(disp=False)
m2.solve(disp=False)

# Extract results
max_value1 = abs(np.sin(math.pi * x1.value[0]))
max_value2 = abs(np.sin(math.pi * x2.value[0]))

# Print results
print('Maximized value 1:', max_value1)
print('Corresponding x 1:', x1.value[0])
print('Maximized value 2:', max_value2)
print('Corresponding x 2:', x2.value[0])

pip install gekko

import numpy as np
from scipy.optimize import minimize
import math

def objective(x):
    return 1 - x[0] + x[1]**2 - 0.1 * math.sin(3 * math.pi * x[0])

def constraint1(x, a):
    return -x[0] + a

# Define bounds for variables
bounds = [(0, 1.0), (-2, 2)]  # Bounds for x[0] and x[1]

# Initial guess
x0 = np.zeros(2)
a = 0.226

# Define constraint
constraint = {'type': 'ineq', 'fun': lambda x: constraint1(x, a)}

# Perform optimization
solution = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=constraint)

# Check if the problem is convex or non-convex based on the Hessian matrix of the objective function
def is_convex_hessian(x):
    # Hessian matrix of the objective function
    hessian = np.array([[0.3 * (math.pi)**2 * math.cos(3 * math.pi * x[0]), 0],
                        [0, 2]])
    # Check if the Hessian matrix is positive semidefinite
    eigenvalues = np.linalg.eigvals(hessian)
    return all(eig >= 0 for eig in eigenvalues)

# Print the solution
print("Optimal Solution:")
print("x1:", solution.x[0], "x2:", solution.x[1])
print("Objective Value:", solution.fun)

# Check if the problem is convex or non-convex
if is_convex_hessian(solution.x):
    print("The problem is convex.")
else:
    print("The problem is non-convex.")

from scipy.optimize import minimize
import numpy as np

# Define the objective function and constraints
def objective(x):
    return (x[0] - 1)**2 + (x[1] - 1)**2  # Objective function: f(x) = (x1 - 1)^2 + (x2 - 1)^2

def constraint1(x):
    return (x[0] + x[1] - 1)**3  # Constraint 1: (x1 + x2 - 1)^3 <= 0

def constraint2(x):
    return x[0]  # Constraint 2: x1 >= 0

def constraint3(x):
    return x[1]  # Constraint 3: x2 >= 0

# Define the constraints for the optimization
constraints = ({'type': 'ineq', 'fun': constraint1},
               {'type': 'ineq', 'fun': constraint2},
               {'type': 'ineq', 'fun': constraint3})

# Initial guess for the optimization
x0 = [0.5, 0.5]

# Minimize the objective function subject to the constraints
result = minimize(objective, x0, constraints=constraints)

# Check if the objective function is convex
def is_convex_objective():
    # The objective function (f(x)) is a quadratic function, which is convex.
    return True

# Check if all constraints are convex
def are_convex_constraints():
    # Constraint 1: (x1 + x2 - 1)^3 is convex because it is raised to an odd power.
    # Constraints 2 and 3 are linear, and linear constraints are convex.
    return True

# Print whether the problem is convex or non-convex
if is_convex_objective() and are_convex_constraints():
    print("The optimization problem is convex.")
else:
    print("The optimization problem is non-convex.")