import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Perform PCA to reduce to 3 dimensions
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X)

# Plotting 3D chart
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
colors = ['r', 'g', 'b']

for target, color in zip(range(len(iris.target_names)), colors):
    ax.scatter(X_pca[y == target, 0], X_pca[y == target, 1], X_pca[y == target, 2], color=color, label=iris.target_names[target])

ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_zlabel('Principal Component 3')
ax.set_title('3D PCA of Iris Dataset')
ax.legend(loc='best')

plt.show()
