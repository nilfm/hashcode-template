from abc import abstractmethod
import random


class Parameter:
    def __init__(self, name, lower, upper):
        assert lower <= upper, f"Parameter {name} has lower bound {lower} > upper bound {upper}"
        self.name = name
        self.lower = lower
        self.upper = upper

    @abstractmethod
    def generate_random(self):
        pass

    @abstractmethod
    def generate_nearby(self, previous):
        pass


class FloatParameter(Parameter):
    def generate_random(self):
        return random.uniform(self.lower, self.upper)

    def generate_nearby(self, previous):
        radius = (self.upper - self.lower)/20
        lower_bound = max(previous - radius, self.lower)
        upper_bound = min(previous + radius, self.upper)
        return random.uniform(lower_bound, upper_bound)

    def __repr__(self):
        return f"<FloatParameter {self.name} [{self.lower}, {self.upper}]>"

    def __str__(self):
        return self.__repr__()


class IntParameter(Parameter):
    def __init__(self, name, lower, upper):
        assert isinstance(
            lower, int), f"Integer parameter {name} has non-integer lower bound {lower}"
        assert isinstance(
            upper, int), f"Integer parameter {name} has non-integer upper bound {upper}"
        super().__init__(name, lower, upper)

    def generate_random(self):
        return random.randint(self.lower, self.upper)

    def generate_nearby(self, previous):
        lower_bound = max(previous - 1, self.lower)
        upper_bound = min(previous + 1, self.upper)
        return random.randint(lower_bound, upper_bound)

    def __repr__(self):
        return f"<IntParameter {self.name} [{self.lower}, {self.upper}]>"

    def __str__(self):
        return self.__repr__()
