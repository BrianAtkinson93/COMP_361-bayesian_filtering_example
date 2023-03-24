from typing import Dict


class BayesianFilter:
    def __init__(self, prior_probabilities: Dict[str, float], likelihoods: Dict[str, Dict[str, float]]):
        """
        Initialize the Bayesian Filter with prior probabilities and likelihoods.

        Args:
            prior_probabilities (Dict[str, float]): A dictionary containing the initial probabilities
                for each hypothesis before any evidence is considered.
            likelihoods (Dict[str, Dict[str, float]]): A nested dictionary that contains the likelihood
                of each piece of evidence given a specific hypothesis.

        Example:
            Consider a real-world problem of determining whether a person has a disease (D) or not (ND),
            based on two test results (T1 and T2). The prior probabilities and likelihoods can be defined as:

            prior_probabilities = {
                'D': 0.01,
                'ND': 0.99,
            }

            likelihoods = {
                'D': {'T1': 0.9, 'T2': 0.8},
                'ND': {'T1': 0.1, 'T2': 0.2},
            }

            The Bayesian Filter can then be used to update the probabilities as new test results are observed.
        """

        self.prior_probabilities = prior_probabilities
        self.likelihoods = likelihoods

    def normalize(self, probabilities: Dict[str, float]) -> Dict[str, float]:
        """
        Normalize the given probabilities so that they sum up to 1.

        Args:
            probabilities (Dict[str, float]): A dictionary containing unnormalized probabilities.

        Returns:
            Dict[str, float]: A dictionary containing normalized probabilities.
        """

        total = sum(probabilities.values())
        normalized_probabilities = {}
        for key, value in probabilities.items():
            normalized_probabilities[key] = value / total
        return normalized_probabilities

    def update(self, evidence: str) -> None:
        """
        Update the prior probabilities based on the observed evidence.

        Args:
            evidence (str): The observed evidence (e.g., 'T1' or 'T2' from the example).

        """
        unnormalized_posterior_probabilities = {}
        for hypothesis, prior_probability in self.prior_probabilities.items():
            likelihood = self.likelihoods[hypothesis][evidence]
            unnormalized_posterior_probabilities[hypothesis] = prior_probability * likelihood

        self.prior_probabilities = self.normalize(unnormalized_posterior_probabilities)

    def get_probabilities(self) -> Dict[str, float]:
        """
        Get the current probabilities of the hypotheses.

        Returns:
            Dict[str, float]: A dictionary containing the current probabilities of the hypotheses.
        """
        return self.prior_probabilities
