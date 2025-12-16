import numpy as np

X = np.array([1,2,3,4,5])
Y = np.array([3,5,6,7,9])

X_Mean = np.mean(X)
Y_Mean = np.mean(Y)

X = X-X_Mean
Y = Y-Y_Mean

Covariance_XY = sum(X*Y)
Variance_X = sum(X*X)

Slope = Covariance_XY/Variance_X
Intercept = Y_Mean - Slope * X_Mean

print(f"{Slope:.4f}x + ({Intercept:.4f})")

