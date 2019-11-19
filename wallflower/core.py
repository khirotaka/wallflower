import numpy as np


class BaseModel:
    def __init__(self, random_seed):
        self.__random_seed = np.random.RandomState(random_seed)

    def fit(self, *args, **kwargs):
        raise NotImplementedError("You have to implement initialize method.")

    def predict(self, *args, **kwargs):
        raise Exception("You have to implement initialize method.")

    def transform(self, *args, **kwargs):
        raise Exception("You have to implement initialize method.")

    @property
    def random_seed(self):
        return self.__random_seed
