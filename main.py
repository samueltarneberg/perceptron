from perceptron import train_perceptron, test_perceptron
from boolean_functions import (
    generate_inputs,
    generate_boolean_functions,
)
import numpy as np


def run(n):
    inputs = generate_inputs(n)
    boolean_functions = generate_boolean_functions(n)

    number_separable = 0
    for targets in boolean_functions:
        w, theta = train_perceptron(inputs,targets,n_epochs=20,eta=0.05)
        if test_perceptron(inputs, targets, w, theta):
            number_separable += 1

    fraction = number_separable / len(boolean_functions)
    return fraction




results = {}
for n in range(2, 6):
    fractions = []
    # Repeat experiment 20 times
    for _ in range(20):
        print(f"n = {n}, repetition = {_ + 1}/20")
        fraction = run(n)
        fractions.append(fraction)
    average = np.mean(fractions)
    standard_deviation = np.std(fractions)
    results[n] = (average, standard_deviation)
    print(
        f"n = {n}: "
        f"average = {average:.4f}, "
        f"standard deviation = {standard_deviation:.4f}"
    )



