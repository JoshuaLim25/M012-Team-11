def simulation(t, e):
    opt_hap = 15 * 300

    xpt_tot_hap_xplr = (10 * 100) + (15 * 100) + (12 * 100)
    xpt_tot_hap_xplt = 10 + 15 + 12 + (15 * 297)
    xpt_tot_hap_egr = (100-e) * 300 * 15 + (e/3) * 300 * (10 + 15 + 12)

    xpt_rgt_xplr = opt_hap - xpt_tot_hap_xplr
    xpt_rgt_xplt = opt_hap - xpt_tot_hap_xplt
    xpt_rgt_egr = opt_hap - xpt_tot_hap_egr




