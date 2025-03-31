# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import numpy as np

def roots(f, a, b, tol=1e-15):
    if np.sign(f(a)) == np.sign(f(b)):
        return None  # No root found if signs are the same

    for _ in range(1000):
        mid = (a + b) / 2
        if np.abs(f(mid)) < tol:  # Check if we are close enough to the root
            return mid
        elif np.sign(f(a)) == np.sign(f(mid)):
            a = mid  # Move the left boundary
        else:
            b = mid  # Move the right boundary

    return (a + b) / 2  # Return the midpoint as the best guess if max iterations reached

test_cases = [
    (lambda x: np.exp(x) + np.log(x), 0.1, 1),
    (lambda x: np.arctan(x) - x**2, 0, 2),
    (lambda x: np.sin(x) / np.log(x), 3, 4),
    (lambda x: np.log(np.cos(x)), 5, 7)
]

for i, (f, a, b) in enumerate(test_cases):
    r1 = roots(f, a, b)
    if r1 is not None:
        print(f"Root of function in [{a}, {b}] = {r1:.10f}")
    else:
        print(f"No root found for function in [{a}, {b}]")
