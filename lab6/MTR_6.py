#Variant 7

import numpy as np

profits_matrix = np.array([
    [8, 2, 4],
    [6, 7, 4],
    [4, 7, 5],
    [3, 5, 6]
])

P1_avg = (0.4 + 0.6) / 2
P2_avg = (0.3 + 0.4) / 2
P3_avg = (0.1 + 0.3) / 2
probabilities = np.array([P1_avg, P2_avg, P3_avg])

expected_profits = profits_matrix.dot(probabilities)

variances = np.var(profits_matrix * probabilities, axis=1)

weight_expected_profit = 2
weight_risk = 3

normalized_expected_profits = (expected_profits - np.min(expected_profits)) / (
            np.max(expected_profits) - np.min(expected_profits))
normalized_risks = 1 - (variances - np.min(variances)) / (np.max(variances) - np.min(variances))

scores = (normalized_expected_profits * weight_expected_profit) + (normalized_risks * weight_risk)

for i, score in enumerate(scores, 1):
    print(f"Проект {i}: Зважений бал = {score:.2f}")

optimal_project = np.argmax(scores) + 1
print(f"Рекомендований проект: Проект {optimal_project}")
