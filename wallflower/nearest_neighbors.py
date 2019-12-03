import numpy as np
from scipy.spatial.distance import mahalanobis, cityblock


class NearestNeighbors:
    def __init__(self, window_size: int, step_size: int):
        """
        Custom Nearest Neighbors,

        Examples::
            >>> x_train = np.random.randn(512, 320)     # [ samples, features ]
            >>> x_test = np.random.randn(1, 320)        # [ samples, features ]
            >>> nn = NearestNeighbors(window_size=128, step_size=1)
            >>> nn.fit(x_train)
            >>> nn.predict(x_test)[:5]                  # show top 5.

        Args:
            window_size:
            step_size:
        """
        self.__data = None
        self.__ws = window_size
        self.__ss = step_size

    def fit(self, inputs: np.ndarray):
        """
        fit model.
        Args:
            inputs: [Samples, Features]

        Examples::
            >>> x_train = np.random.randn(512, 320)     # [ samples, features ]
            >>> x_test = np.random.randn(1, 320)        # [ samples, features ]
            >>> nn = NearestNeighbors(window_size=128, step_size=1)
            >>> nn.fit(x_train)

        Returns:
            self
        """
        self.__data = inputs
        return self

    def predict(self, inputs: np.ndarray, idx: int, criterion: str = "euclidean") -> np.ndarray:
        """

        Args:
            inputs:
            idx:
            criterion:

        Examples::
            >>> x_train = np.random.randn(512, 320)     # [ samples, features ]
            >>> x_test = np.random.randn(1, 320)        # [ samples, features ]
            >>> nn = NearestNeighbors(window_size=128, step_size=1)
            >>> nn.fit(x_train)
            >>> nn.predict(x_test)[:5]                  # show top 5.

        Returns:

        """
        tmp = self.separate(idx)

        if criterion == "manhattan":
            distance = np.array([self.manhattan_distance(p, inputs) for p in tmp])
            return distance

        elif criterion == "euclidean":
            distance = np.array([self.euclidean_distance(p, inputs) for p in tmp])
            return distance.argsort()

        elif criterion == "mahalanobis":
            distance = np.array([self.mahalanobis_distance(tmp, i) for i in inputs])
            return distance

        else:
            raise Exception("Argument not defined.")

    def separate(self, idx):
        if idx < 0:
            raise IndexError

        end = idx + self.window_size - 1
        rng_start = (idx - self.window_size) + 1
        rng_end = (end + self.window_size) - 1

        if rng_start < 0:
            rng_start = 0
        if rng_end > self.data.shape[0]:
            rng_end = self.data.shape[0]

        tmp = np.delete(self.data, slice(rng_start, rng_end), 0)
        return tmp

    @staticmethod
    def manhattan_distance(p0: np.ndarray, p1: np.ndarray) -> np.ndarray:
        return cityblock(p0, p1)

    @staticmethod
    def euclidean_distance(p0: np.ndarray, p1: np.ndarray) -> np.ndarray:
        return np.linalg.norm(p0 - p1)

    @staticmethod
    def mahalanobis_distance(data: np.ndarray, inputs: np.ndarray) -> np.ndarray:
        mean = np.mean(data, axis=0)
        cov = np.cov(data.T)
        distance = mahalanobis(inputs, mean, np.linalg.pinv(cov))
        return distance

    @property
    def data(self):
        return self.__data

    @property
    def window_size(self):
        return self.__ws

    @property
    def step_size(self):
        return self.__ss
