import itertools
import numpy as np


def generate_inputs(n):
    inputs=[[]]
    for i in range(n):
        new_inputs = []
        for j in inputs:
            new_inputs.append(j + [0])
            new_inputs.append(j + [1])
        inputs = new_inputs
    return inputs

def generate_boolean_functions(n):
    n_inputs = 2**n
    if n <= 3:
        functions =[[]]
        for i in range(n_inputs):
            new_functions = []
            for j in functions:
                new_functions.append(j + [-1])
                new_functions.append(j + [1])
            functions = new_functions
        return functions


    # else:
    #     number_of_inputs = 2**n
    #     return tuple(np.random.choice([-1, 1], number_of_inputs))





n = 3
output_inputs = generate_inputs(n)
boolean_functions = len(generate_boolean_functions(n))
print(output_inputs)
print(boolean_functions)