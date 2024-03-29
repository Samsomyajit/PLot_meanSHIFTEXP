import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets.samples_generator import make_blobs

centers = [[1, 1], [-1, -1], [1, -1]]
X,_ = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)


bandwidth = estimate_bandwidth(X, n_samples=500)

ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)

print("number of estimated clusters : %d" % n_clusters_)


# Plot result
import matplotlib.pyplot as plt

for k in range(n_clusters_):
    my_members = labels == k
    cluster_center = cluster_centers[k]
    plt.scatter(X[my_members, 0], X[my_members, 1])
    plt.plot(cluster_center[0], cluster_center[1], 'o',
             markeredgecolor='b', markersize=14)
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
