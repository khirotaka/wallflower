import numpy as np
from scipy.sparse.linalg import svds


class PCA:
    def __init__(self, n_components, tol: float = 0.0, random_seed: int = 0):
        self.__random_seed = np.random.RandomState(random_seed)
        self.n_components = n_components
        self.tol = tol
        self.VT_ = None

    def fit(self, inputs: np.ndarray):
        v0 = self.random_seed.randn(min(inputs.shape))
        xbar = inputs.mean(axis=0)
        y = inputs - xbar
        s = np.dot(y.T, y)
        u, sigma, vt = svds(s, k=self.n_components, tol=self.tol, v0=v0)
        del sigma

        self.VT_ = vt[::-1, :]

    def transform(self, inputs: np.ndarray):
        return self.VT_.dot(inputs.T).T

    @property
    def random_seed(self):
        return self.__random_seed
