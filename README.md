# Bayesian Filter

The Bayesian Filter is a class that allows you to update probabilities based on new evidence using Bayesian probability. This README provides a brief explanation of the inputs and the class implementation in Python, as well as an example of how to use the class.

## Inputs

### Prior Probabilities

>#### Probabilities 
>Probabilities are numerical values between 0 and 1 that indicate the likelihood of an event or a hypothesis being true. In the Bayesian Filter class, the probabilities represent the prior beliefs about the truth of each hypothesis before considering any evidence. The sum of the prior probabilities for all hypotheses should equal 1.
<br>

>Example:<br><br>
prior_probabilities = {
    'A': 0.5,
    'B': 0.5,
}<br>
>In this example, we have two hypotheses (A and B) with prior probabilities of 0.5 each. This means that, before observing any evidence, we believe that both hypotheses are equally likely to be true, each with a 50% chance.

A dictionary containing the initial probabilities for each hypothesis before any evidence is considered. The keys of the dictionary represent the hypotheses, and the values represent their probabilities.


### Likelihoods
> Likelihoods represent the probability of observing a specific piece of evidence, given a hypothesis. The likelihoods are used to update the prior probabilities when new evidence is observed.
>
>In the Bayesian Filter class, likelihoods are organized in a nested dictionary. The outer dictionary keys represent the hypotheses (e.g., 'A' and 'B'), and the values are inner dictionaries. The inner dictionaries have keys representing the evidence (e.g., 'E1' and 'E2') and values representing the likelihood of observing that evidence given the corresponding hypothesis.
>A nested dictionary that contains the likelihood of each piece of evidence given a specific hypothesis. The outer dictionary has keys representing hypotheses (e.g., 'A' and 'B'), and the values are inner dictionaries. The inner dictionaries have keys representing the evidence (e.g., 'E1' and 'E2') and values representing the likelihood of observing that evidence given the corresponding hypothesis.
>
> For Example:<br>
>likelihoods = {
    'A': {'E1': 0.1, 'E2': 0.7},
    'B': {'E1': 0.3, 'E2': 0.3},
>}
>In this example, the likelihoods are defined as follows:<br>
><ul>
><li>For Hypothesis A: P(E1 | A) = 0.1 and P(E2 | A) = 0.7</li>
><li>This means that if Hypothesis A is true, there is a 10% chance of observing Evidence E1 and a 70% chance of observing Evidence E2.</li>
><li>For Hypothesis B: P(E1 | B) = 0.3 and P(E2 | B) = 0.3</li>
><li>This means that if Hypothesis B is true, there is a 30% chance of observing Evidence E1 and a 30% chance of observing Evidence E2.</li>
><li>The Bayesian Filter class uses these likelihoods to update the prior probabilities when new evidence is observed, thus providing updated probabilities that take the new evidence into account.</li>
></ul>
## Class Implementation

The Bayesian Filter class consists of the following methods:

1. `__init__(self, prior_probabilities, likelihoods)`: Initializes the Bayesian Filter with the given prior probabilities and likelihoods.
2. `normalize(self, probabilities)`: A helper method that normalizes a dictionary of probabilities, ensuring that the sum of probabilities is 1.
3. `update(self, evidence)`: Updates the prior probabilities based on the provided evidence using the likelihoods.
4. `get_probabilities(self)`: Returns the current probabilities for all hypotheses.

## Example Usage

1. Define the prior probabilities and likelihoods for the hypotheses and evidence.
2. Create an instance of the BayesianFilter class (found in `classes/bayesian_filter.py`) with the defined prior probabilities and likelihoods.
3. Update the probabilities using the `update` method by providing new evidence.
4. Retrieve the updated probabilities using the `get_probabilities` method.
