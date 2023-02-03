import numpy as np
import matplotlib.pyplot as plt


X = ['Small','Medium','Big']
bs_100 = [76.42 ,17.61 ,71.16]
bs_1024 = [383.67 ,115.46 ,1.20]
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, bs_100, 0.4, label = 'Batch Size = 100')
plt.bar(X_axis + 0.2, bs_1024, 0.4, label = 'Batch Size = 1024')
  
plt.xticks(X_axis, X)
plt.xlabel("Model size")
plt.ylabel("Mean Eval Return")
plt.title("Walker2d-v2 task")
plt.legend()
plt.savefig("walker_hyperparameters.jpg")