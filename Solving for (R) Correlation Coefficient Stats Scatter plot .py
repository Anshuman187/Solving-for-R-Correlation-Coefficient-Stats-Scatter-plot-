import numpy as np
x_values = [2,4,6]
y_values = [4,2,3]

correlation_matrix = np.corrcoef(x_values, y_values)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2

print(r_squared)