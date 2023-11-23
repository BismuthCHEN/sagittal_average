import subprocess

import numpy as np

input_data = np.zeros([20, 20])
input_data[-1, :] = np.ones(20)
expected_data = np.zeros([20])
expected_data[-1] = 1
np.savetxt("brain_sample.csv", input_data, fmt='%d', delimiter=',')

subprocess.run("python", "sagittal_brain.py", shell=True)

actual_output = np.loadtxt("brain_average.csv", dtype=int,  delimiter=',')
np.testing.assert_array_equal(actual_output, expected_data)
#print(actual_output.all() == expected_data.all())