from exploreOnly import exploreOnly
from exploitOnly import exploitOnly
from Egreedy import eGreedy

def simulation(t, e):
    opt_hap = 15 * 300

    xpt_tot_hap_xplr = (10 * 100) + (15 * 100) + (12 * 100)
    xpt_tot_hap_xplt = 10 + 15 + 12 + (15 * 297)
    xpt_tot_hap_egr = (100-e) * 300 * 15 + (e/3) * 300 * (10 + 15 + 12)

    xpt_rgt_xplr = opt_hap - xpt_tot_hap_xplr
    xpt_rgt_xplt = opt_hap - xpt_tot_hap_xplt
    xpt_rgt_egr = opt_hap - xpt_tot_hap_egr

    for _ in range(t):
        print(f"———————————————simulation attempt {t}———————————————")
        print(f"Optimum happiness: {opt_hap}")
        #———————————————
        print("Explore only:")
        print(f"\texpected happiness: {xpt_tot_hap_xplr}")
        print(f"\texpected regret: {xpt_rgt_xplr}")
        hpp = exploreOnly()
        print(f"\tactual happiness: {hpp}")
        print(f"\tactual regret: {opt_hap - hpp}")
        #———————————————
        print("Exploit only:")
        print(f"\texpected happiness: {xpt_tot_hap_xplt}")
        print(f"\texpected regret: {xpt_rgt_xplt}")
        hpp = exploitOnly()
        print(f"\tactual happiness: {hpp}")
        print(f"\tactual regret: {opt_hap - hpp}")
        # ———————————————
        print("e-Greedy:")
        print(f"\texpected happiness: {xpt_tot_hap_egr}")
        print(f"\texpected regret: {xpt_rgt_egr}")
        hpp = eGreedy(e)
        print(f"\tactual happiness: {hpp}")
        print(f"\tactual regret: {opt_hap - hpp}")
        print(f"———————————————end of simulation attempt {t}———————————————\n\n")


