import numpy as np
from sklearn.metrics.pairwise import euclidean_distances, pairwise_distances
from src.fun_utils import *

class NMC(object):
    """
    Class implementing the Nearest Mean Centroid (NMC) classifier.

    This classifier estimates one centroid per class from the training data,
    and predicts the label of a never-before-seen (test) point based on its
    closest centroid.

    Attributes
    -----------------
    - centroids: read-only attribute containing the centroid values estimated
        after training

    Methods
    -----------------
    - fit(x,y) estimates centroids from the training data
    - predict(x) predicts the class labels on testing points

    """

    def __init__(self):
        self._centroids = None
        self._class_labels = None  # class labels may not be contiguous indices

    @property
    def centroids(self):
        return self._centroids

    @property
    def class_labels(self):
        return self._class_labels

    def fit(self, xtr, ytr):
        pass

    def predict(self, xts):
        """
        Compute similarities with centroids

        Parameters
        ----------
        xts : ndarray
            Input samples to be classified

        Returns
        -------
        ypred: ndarray
            Output values for each sample vs class
        """
        if self.centroids is None:
            raise ValueError(
                "Centroids have not been estimated. Call `fit' first.")

        dist = pairwise_distances(xts, self.centroids)
        scores = 1 / (1e-3 + dist)

        ypred = np.argmax(scores, axis=1)
        return ypred
