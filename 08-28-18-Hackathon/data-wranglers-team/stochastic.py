# Stochastic approach 
# Run this for each wine input.
import numpy as np

# The great majority of the wine scores in the training data fall in this range.
lower_bound = 86
upper_bound = 92

# Prediction is a stochastic result that has a likelyhood of being close to the actual score, no matter the features.
prediction = np.random.randint(lower_bound, upper_bound)

print(prediction)