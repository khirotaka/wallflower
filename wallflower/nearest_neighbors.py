import numpy as np

from .core import BaseModel


class NearestNeighbors(BaseModel):
    def __init__(self, window_size: int, step_size: int, random_seed: int = None):
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
            random_seed:
        """
        super(NearestNeighbors, self).__init__(random_seed=random_seed)
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

    def predict(self, inputs: np.ndarray, idx: int) -> np.ndarray:
        """

        Args:
            inputs:
            idx:

        Examples::
            >>> x_train = np.random.randn(512, 320)     # [ samples, features ]
            >>> x_test = np.random.randn(1, 320)        # [ samples, features ]
            >>> nn = NearestNeighbors(window_size=128, step_size=1)
            >>> nn.fit(x_train)
            >>> nn.predict(x_test)[:5]                  # show top 5.

        Returns:

        """
        end = idx + self.window_size - 1
        rng_start = (idx - self.window_size) + 1
        rng_end = (end + self.window_size) - 1
        tmp = np.delete(self.data, slice(rng_start, rng_end), 0)
        distance = np.array([self.__distance(p, inputs) for p in tmp])
        return distance.argsort()

    @staticmethod
    def __distance(p0: np.ndarray, p1: np.ndarray) -> np.ndarray:
        return np.linalg.norm(p0 - p1)

    @property
    def data(self):
        return self.__data

    @property
    def window_size(self):
        return self.__ws

    @property
    def step_size(self):
        return self.__ss
