from Cafe import Cafe
from random import randint


def eGreedy(e=10):
    cafe1, cafe2, cafe3 = Cafe(10, 8), Cafe(15, 6), Cafe(12, 5)

    cafe1.visit()
    cafe2.visit()
    cafe3.visit()

    for _ in range(297):
        most_hap = Cafe.max_happiness_of([cafe1, cafe2, cafe3])
        goto = randint(0, 100)
        if goto <= e:
            gt = ran
            [cafe1, cafe2, cafe3][gt].visit()
        elif goto > e:
            most_hap.visit()

    return Cafe.total_hap_of([cafe1, cafe2, cafe3])