"""Written by Brian Atkinson"""

# Import the BayesianFilter class from the bayesian module.
from classes.bayesian import BayesianFilter

# Define prior probabilities for two hypotheses: A and B.
PRIOR_PROB = {
    'A': 0.5,
    'B': 0.5,
}

# Define likelihoods of evidence E1 and E2 for both hypotheses.
LIKELIHOOD = {
    'A': {'E1': 0.1, 'E2': 0.7},
    'B': {'E1': 0.3, 'E2': 0.3},
}


def main():
    # Create a BayesianFilter object with the given prior probabilities and likelihoods.
    bayesian_filter = BayesianFilter(PRIOR_PROB, LIKELIHOOD)

    print("Initial probabilities:")
    print(bayesian_filter.get_probabilities())

    # Update the probabilities with new evidence E1.
    bayesian_filter.update('E1')

    # Print the updated probabilities after observing evidence E1.
    print("\nProbabilities after observing evidence E1:")
    print(bayesian_filter.get_probabilities())

    # Update the probabilities with new evidence E2.
    bayesian_filter.update('E2')

    # Print the updated probabilities after observing evidence E2.
    print("\nProbabilities after observing evidence E2:")
    print(bayesian_filter.get_probabilities())


if __name__ == '__main__':
    # Main
    main()
