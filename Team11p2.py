from exploreOnly import exploreOnly
from exploitOnly import exploitOnly
from Egreedy import eGreedy

def simulation(t, e=10):
    opt_hap = 15 * 300

    xpt_tot_hap_xplr = (10 * 100) + (15 * 100) + (12 * 100)
    xpt_tot_hap_xplt = 10 + 15 + 12 + (15 * 297)
    xpt_tot_hap_egr = ((100-e)/100) * 300 * 15 + e * (10 + 15 + 12)


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
        print(f"———————————————simulation attempt {i+1}———————————————")
        print(f"Optimum happiness: {opt_hap}")
        #———————————————
        print("Explore only:")
        print(f"\texpected happiness: {xpt_tot_hap_xplr}")
        print(f"\texpected regret: {xpt_rgt_xplr}")
        hpp = exploreOnly()
        print(f"\tactual happiness: {hpp}")
        print(f"\tactual regret: {opt_hap - hpp}")
        act_hpp_xplr.append(hpp)
        act_rgt_xplr.append(opt_hap - hpp)
        #———————————————
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
        print(f"———————————————end of simulation attempt {i+1}———————————————\n\n")

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
    simulation(100000, 10)


