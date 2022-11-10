from random import randint
import random


class Cafe():
    def __init__(self, average_happiness, standard_deviation):
        self.avg_hpp = average_happiness
        self.std_dev = standard_deviation
        self.visit_history = []

    def visit(self):
        happiness = random.normalvariate(self.avg_hpp, self.std_dev)
        self.visit_history.append(happiness)

    @classmethod
    def max_avg_happiness_of(cls, cafes: list):
        """
        :param cafés: a list of cafes (class Cafe)
        :return: cafe with the most total happiness
        """
        best = cafes[0]
        for cafe in cafes:
            if (sum(cafe.visit_history) / len(cafe.visit_history)) \
                    > (sum(best.visit_history) / len(cafe.visit_history)):
                best = cafe

        return best

    @classmethod
    def total_hap_of(cls, cafes: list):
        """
        :param cafes: a list of cafes (class Cafe)
        :return: total happiness of all cafes
        """

        return sum([sum(cafe.visit_history) for cafe in cafes])


def exploreOnly():
    cafe1, cafe2, cafe3 = Cafe(10, 8), Cafe(15, 6), Cafe(12, 5)

    for _ in range(100):
        cafe1.visit()
        cafe2.visit()
        cafe3.visit()
    return Cafe.total_hap_of([cafe1, cafe2, cafe3])


def exploitOnly():
    cafe1, cafe2, cafe3 = Cafe(10, 8), Cafe(15, 6), Cafe(12, 5)

    cafe1.visit()
    cafe2.visit()
    cafe3.visit()
    best = Cafe.max_avg_happiness_of([cafe1, cafe2, cafe3])
    for i in range(297):
        best.visit()
    return Cafe.total_hap_of([cafe1, cafe2, cafe3])


def eGreedy(e=10):
    cafe1, cafe2, cafe3 = Cafe(10, 8), Cafe(15, 6), Cafe(12, 5)

    cafe1.visit()
    cafe2.visit()
    cafe3.visit()

    for _ in range(297):
        most_hap = Cafe.max_avg_happiness_of([cafe1, cafe2, cafe3])
        goto = randint(0, 100)
        if goto <= e:
            gt = randint(0, 2)
            [cafe1, cafe2, cafe3][gt].visit()
        elif goto > e:
            most_hap.visit()

    return Cafe.total_hap_of([cafe1, cafe2, cafe3])


def simulation(t, e=10):
    opt_hap = 15 * 300

    xpt_tot_hap_xplr = (10 * 100) + (15 * 100) + (12 * 100)
    xpt_tot_hap_xplt = 10 + 15 + 12 + (15 * 297)
    xpt_tot_hap_egr = ((100 - e) / 100) * 300 * 15 + e * (10 + 15 + 12)

    xpt_rgt_xplr = opt_hap - xpt_tot_hap_xplr
    xpt_rgt_xplt = opt_hap - xpt_tot_hap_xplt
    xpt_rgt_egr = opt_hap - xpt_tot_hap_egr

    act_hpp_xplr = []
    act_hpp_xplt = []
    act_hpp_egr = []

    act_rgt_xplr = []
    act_rgt_xplt = []
    act_rgt_egr = []

    for i in range(t):
        print(f"———————————————simulation attempt {i + 1}———————————————")
        print(f"Optimum happiness: {opt_hap}")
        # ———————————————
        print("Explore only:")
        print(f"\texpected happiness: {xpt_tot_hap_xplr}")
        print(f"\texpected regret: {xpt_rgt_xplr}")
        hpp = exploreOnly()
        print(f"\tactual happiness: {hpp}")
        print(f"\tactual regret: {opt_hap - hpp}")
        act_hpp_xplr.append(hpp)
        act_rgt_xplr.append(opt_hap - hpp)
        # ———————————————
        print("Exploit only:")
        print(f"\texpected happiness: {xpt_tot_hap_xplt}")
        print(f"\texpected regret: {xpt_rgt_xplt}")
        hpp = exploitOnly()
        print(f"\tactual happiness: {hpp}")
        print(f"\tactual regret: {opt_hap - hpp}")
        act_hpp_xplt.append(hpp)
        act_rgt_xplt.append(opt_hap - hpp)
        # ———————————————
        print("e-Greedy:")
        print(f"\texpected happiness: {xpt_tot_hap_egr}")
        print(f"\texpected regret: {xpt_rgt_egr}")
        hpp = eGreedy(e)
        print(f"\tactual happiness: {hpp}")
        print(f"\tactual regret: {opt_hap - hpp}")
        act_hpp_egr.append(hpp)
        act_rgt_egr.append(opt_hap - hpp)
        print(f"———————————————end of simulation attempt {i + 1}———————————————\n\n")

    print(f"———————————————simulation results for {t} attempts———————————————")
    print("Explore only:")
    print(f"\taverage happiness: {sum(act_hpp_xplr) / len(act_hpp_xplr)}")
    print(f"\taverage regret: {sum(act_rgt_xplr) / len(act_rgt_xplr)}")
    print("Exploit only:")
    print(f"\taverage happiness: {sum(act_hpp_xplt) / len(act_hpp_xplt)}")
    print(f"\taverage regret: {sum(act_rgt_xplt) / len(act_rgt_xplt)}")
    print("e-Greedy:")
    print(f"\taverage happiness: {sum(act_hpp_egr) / len(act_hpp_egr)}")
    print(f"\taverage regret: {sum(act_rgt_egr) / len(act_rgt_egr)}")


if __name__ == '__main__':
    simulation(100)
