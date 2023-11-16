import numpy as np
from sagittal_brain import run_averages

data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')
run_averages()
#print()