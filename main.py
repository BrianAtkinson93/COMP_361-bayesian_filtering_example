"""Written by Brian Atkinson"""

import json
from classes.bayesian import BayesianFilter
from stubs.likelihood import calculate_likelihoods

# Evidence explanation
EVIDENCE_EXPLANATION = {
    'T1': "The first piece of evidence (T1) represents the patient testing positive for a certain symptom.",
    'T2': "The second piece of evidence (T2) represents the patient testing positive for a different symptom.",
}

# Load the data from the JSON file
with open('stubs/data.json', 'r') as f:
    data = json.load(f)['data']

# Define hypotheses and evidence
HYPOTHESES = ['D', 'ND']
EVIDENCE = ['T1', 'T2']

# Calculate the likelihoods
LIKELIHOOD = calculate_likelihoods(data, HYPOTHESES, EVIDENCE)

# Define prior probabilities for two hypotheses: D and ND.
PRIOR_PROB = {
    'D': 0.5,
    'ND': 0.5,
}


def main():
    # Create a BayesianFilter object with the given prior probabilities and likelihoods.
    bayesian_filter = BayesianFilter(PRIOR_PROB, LIKELIHOOD)

    print("Initial probabilities:")
    print(bayesian_filter.get_probabilities())

    # Update the probabilities with new evidence T1.
    print("\nProcessing evidence T1:")
    print(EVIDENCE_EXPLANATION['T1'])
    bayesian_filter.update('T1')

    # Print the updated probabilities after observing evidence T1.
    print("\nProbabilities after observing evidence T1:")
    print(bayesian_filter.get_probabilities())

    # Update the probabilities with new evidence T2.
    print("\nProcessing evidence T2:")
    print(EVIDENCE_EXPLANATION['T2'])
    bayesian_filter.update('T2')

    # Print the updated probabilities after observing evidence T2.
    print("\nProbabilities after observing evidence T2:")
    print(bayesian_filter.get_probabilities())


if __name__ == '__main__':
    # Main
    main()
