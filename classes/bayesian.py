class BayesianFilter:
    def __init__(self, prior_probabilities, likelihoods):
        self.prior_probabilities = prior_probabilities
        self.likelihoods = likelihoods

    def normalize(self, probabilities):
        total = sum(probabilities.values())
        normalized_probabilities = {}
        for key, value in probabilities.items():
            normalized_probabilities[key] = value / total
        return normalized_probabilities

    def update(self, evidence):
        unnormalized_posterior_probabilities = {}
        for hypothesis, prior_probability in self.prior_probabilities.items():
            likelihood = self.likelihoods[hypothesis][evidence]
            unnormalized_posterior_probabilities[hypothesis] = prior_probability * likelihood

        self.prior_probabilities = self.normalize(unnormalized_posterior_probabilities)

    def get_probabilities(self):
        return self.prior_probabilities
