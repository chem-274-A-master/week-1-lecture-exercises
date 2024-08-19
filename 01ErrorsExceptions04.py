"""
Consider the function below. It calculates a weighted average.

Check that values and weights have the same length. 
If they do not, a ValueError should be raised.
"""
import math

def weighted_average(values, weights):
  
  avg = 0
  weight_sum = 0

  for i in range(len(values)):
    avg += weights[i] * values[i]
    weight_sum += weights[i]

  avg = avg / weight_sum

  return avg
  

if __name__ == "__main__":

  weights = [0.1, 0.5, 0.4]

  vals = [ 5, 10, 1 ]

  wa = weighted_average(vals, weights)

  print(wa)
