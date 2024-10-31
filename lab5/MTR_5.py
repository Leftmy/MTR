# Variant 7

import numpy as np

A = np.matrix([[2.5, 3.5, 4],
               [1.5, 2, 3.5],
               [3.5, 8, 2.5],
               [7.5, 1.5, 2.5],
               [8.5, 1.5, 4]])

R = np.zeros((5, 3))

max_values = np.max(A, axis=0)

for i in range(5):
    for j in range(3):
        R[i, j] = max_values[0, j] - A[i, j]

max_regret_decisions = np.max(R, axis=1)

optimal_decision = np.argmin(max_regret_decisions)

print("Матриця ризику (невикористаних можливостей):")
print(R)
print("\nМаксимальний ризик для кожного рішення:")
print(max_regret_decisions)
print(f"\nОптимальне рішення за критерієм Севіджа: x_{optimal_decision + 1}")
