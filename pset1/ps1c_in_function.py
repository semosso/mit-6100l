def part_c(initial_deposit):
	#########################################################################
	cost_of_dream_home = 800000.0
	down_payment = 0.25 * cost_of_dream_home
	months = 36
	lowest_r, highest_r = 0.0, 1.0
	r = (highest_r + lowest_r) / 2
	amount_saved = initial_deposit
	epsilon = 100.0
	steps = 0
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	while highest_r - lowest_r > 0.001: # still have to nail down the condition, this is trash
	    if (initial_deposit * (1 + highest_r / 12) ** months) < down_payment:
	        r = None
	        break
	    elif initial_deposit >= down_payment:
	        r = 0.0
	        break
	    # print(highest_r, lowest_r, r, steps, amount_saved) # testing/debugging purposes
	    amount_saved = initial_deposit * (1 + r / 12) ** months
	    if amount_saved - down_payment > epsilon:
	        highest_r = r
	    else:
	        lowest_r = r
	    r = (highest_r + lowest_r) / 2
	    steps += 1
	print(f"Best savings rate: {r} [or very close to this number]\n"
	      f"Steps in bisection search: {steps} [or very close to this number]")
	return r, steps