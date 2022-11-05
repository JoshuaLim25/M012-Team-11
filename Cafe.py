import random


class Cafe():
    def __init__(self, average_happiness, standard_deviation):
        self.avg_hpp = average_happiness
        self.std_dev = standard_deviation
        self.visit_history = []


    def visit(self) -> float:
        happiness = random.normalvariate(self.avg_hpp, self.std_dev)
        self.visit_history.append(happiness)
        return happiness

    @classmethod
    def max_happiness_of(cls, cafes:list):
        """
        :param cafes: a list of cafes (class Cafe)
        :return: cafe with the most total happiness
        """
        best = cafes[0]
        for cafe in cafes:
            if sum(cafe.visit_history) > sum(best.visit_history):
                best = cafe

        return cafe

    @classmethod
    def total_hap_of(cls, cafes:list):
        """
        :param cafes: a list of cafes (class Cafe)
        :return: total happiness of all cafes
        """
        s = 0.0
        for cafe in cafes:
            s += sum(cafe.visit_history)

        return s