"""
Optimum happiness = highest of average happiness of all cafes * 300


Expected total happiness = avg happiness * the num of times the cafe was visited
    eplore only: avg hap * 100 for each caff
    exploit only: sum of every avg happ + 297*max avg happ
    e-greedy: 100-e days * max avg happ + (e/3) days * (summ of avg happ)


Expected regret
    Optimum Happiness - expected total happines
    for each func


Average total happines = the one we get after running the functions


Average regret = Optimum happiness - average total happiness
"""
