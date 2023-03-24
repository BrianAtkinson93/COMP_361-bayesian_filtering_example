from typing import Dict, List, Union


def calculate_likelihoods(data: List[Dict[str, Union[str, bool]]], hypotheses: List[str], evidence: List[str]) -> Dict[
    str, Dict[str, float]]:
    """
    Calculate the likelihood of each evidence given each hypothesis based on the given data.

    Args:
        data (List[Dict[str, Union[str, bool]]]): A list of dictionaries containing data for each patient.
            Each dictionary contains the keys 'hypothesis', 'evidence1', and 'evidence2', with the values
            representing the hypothesis (D or ND) and the observed evidence (T1 or T2).
        hypotheses (List[str]): A list of hypotheses (e.g., ['D', 'ND'] from the disease detection problem).
        evidence (List[str]): A list of evidence (e.g., ['T1', 'T2'] from the disease detection problem).

    Returns:
        Dict[str, Dict[str, float]]: A nested dictionary containing the likelihood of each evidence given
            each hypothesis. The outer dictionary keys represent the hypotheses, and the values are inner
            dictionaries. The inner dictionaries have keys representing the evidence and values representing
            the likelihood of observing that evidence given the corresponding hypothesis.
    """
    likelihoods = {}
    for hypothesis in hypotheses:
        likelihoods[hypothesis] = {}
        for e in evidence:
            numerator = 0
            denominator = 0
            for d in data:
                if d['hypothesis'] == hypothesis:
                    denominator += 1
                    if d['evidence1'] == e or d['evidence2'] == e:
                        numerator += 1
            likelihoods[hypothesis][e] = numerator / denominator
    return likelihoods
