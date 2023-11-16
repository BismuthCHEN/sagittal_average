import numpy as np
from sagittal_brain import run_averages

input_data = np.zeros([5, 5])
input_data[-1, :] = np.ones(5)
expected_data = np.ones([1, 5])

np.savetxt("brain_sample.csv", input_data, fmt='%d', delimiter=',')
run_averages()
actual_output = np.loadtxt("brain_average.csv", dtype=int,  delimiter=',')

print(actual_output)