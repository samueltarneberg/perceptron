import numpy as np

class Perceptron: 
    def perceptron(x, w, theta):
            b = np.dot(w, x) - theta
            O = 1 if b >= 0 else -1
            return O


    def train_perceptron(inputs, targets, n_epochs, eta):
        n = len(inputs[0])
        # Initialize weights
        w = np.random.normal(0, 1 / np.sqrt(n), n)
        # Initialize threshold
        theta = 0
        for epoch in range(n_epochs):
            for x, t in zip(inputs, targets):
                O = Perceptron.perceptron(x, w, theta)
                error = t - O
                w += eta * error * np.array(x)
                theta += -eta * error
        return w, theta


    def test_perceptron(inputs, targets, w, theta):
        for x, t in zip(inputs, targets):
            O = Perceptron.perceptron(x, w, theta)
            
            if O != t:
                return False
        return True


class Boolean:
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
                for function in functions:
                    new_functions.append(function + [-1])
                    new_functions.append(function + [1])
                functions = new_functions
            return functions
        else:
            functions = []
            for i in range(10000):
                function = list(np.random.choice([-1,1], n_inputs))
                functions.append(function)
            return functions

            


    # else:
    #     number_of_inputs = 2**n
    #     return tuple(np.random.choice([-1, 1], number_of_inputs))


def run(n):
    inputs = Boolean.generate_inputs(n)
    boolean_functions = Boolean.generate_boolean_functions(n)

    number_separable = 0
    for targets in boolean_functions:
        w, theta = Perceptron.train_perceptron(inputs,targets,n_epochs=20,eta=0.05)
        if Perceptron.test_perceptron(inputs, targets, w, theta):
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
        f"average = {average:.6f}, "
        f"standard deviation = {standard_deviation:.6f}"
    )




# n = 4
# output_inputs = Boolean.generate_inputs(n)
# boolean_functions = len(Boolean.generate_boolean_functions(n))
# print(output_inputs)
# print(boolean_functions)