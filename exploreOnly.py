from Cafe import Cafe

def exploreOnly():
    cafe1, cafe2, cafe3 = Cafe(10, 8), Cafe(15, 6), Cafe(12, 5)
    for _ in range(100):
        cafe1.visit()
        cafe2.visit()
        cafe3.visit()
    return Cafe.total_hap_of([cafe1, cafe2, cafe3])