# Predicting Wine Score 

## Worst Case Model
Our worst case model randomizes a number between 80 and 100, because we know the target's score will be in that range. Accuracy is less than 5%.

## Stochastic approach (Better than worst case model)
In the training data, the wine scores cluster very tightly between 86 and 91. The two middle quartiles are in that. Since the great majority of the score values are between 86-91, we can generate a random score in this range and have a higher accuracy.

For the stochastic approach, run `stochastic.py` for each wine review. 
Each gue

## Copy-paste Regression approach
Follow the model here, but use Score instead of Price.
https://medium.com/tensorflow/predicting-the-price-of-wine-with-the-keras-functional-api-and-tensorflow-a95d1c2c1b03

Accuracy with 10 epochs was %27.9

## Members of the Team
Ed
Amit
Jesse
Ryan
