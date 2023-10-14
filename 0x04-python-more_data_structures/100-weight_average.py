#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:  # Check if the list is empty
        return 0

    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    if total_weight == 0:  # Avoid division by zero
        return 0

    weighted_average = total_score / total_weight
    return weighted_average
"""
# Example usage:
scores_weights = [(80, 2), (90, 3), (75, 1)]
average = weight_average(scores_weights)
print("Weighted Average:", average)  # Output: 86.25
"""