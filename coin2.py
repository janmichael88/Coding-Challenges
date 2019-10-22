def coins_per_denomination(cents):
	#define list of coins
	coins = [25,10,5,1]
	#define number of times per coin
	num_times_coin = []
	#go through each coin and get number of times it goes into cents
	for coin in coins:
		#left remainder after going in n times
		remainder = cents % coin
		#divide remainer by coin to get fraction
		fraction = remainder / coin
		#subtract fraction from cents/coin to get number of times
		num_times =  (cents / coin) - fraction
		#add to list num of num times per coin
		num_times_coin.append(num_times)
	return(num_times_coin)

def num_times_coin_into_cents(cents,coin):
	#left remainder after going in n times
	remainder = cents % coin
	#divide remainer by coin to get fraction
	fraction = remainder / coin
	#subtract fraction from cents/coin to get number of times
	num_times =  (cents / coin) - fraction
	return(num_times)
	
def min_num_coins(cents):
	num_times = coins_per_denomination(cents)
	#remaining cents
	cents_leftover_after_quarters = cents
	cents_leftover_after_dimes = cents
	cents_leftover_after_nikels = cents
	cents_left_overver_after_pennies = cents
	#list of coins used up
	coins_used = []
	#go through quarters first
	if num_times[0] > 0:
		#use up quarters first
		cents_leftover_after_quarters = cents - num_times[0]*25
		coins_used.append(round(num_times[0]))
	else:
		only_quarters_used = num_times[0]
		coins_used.append(round(only_quarters_used))
	if cents_leftover_after_quarters > 0:
		#there are cents to use up, can they go into dimes?
		num_times_cents_leftover_after_quarters_into_dimes = num_times_coin_into_cents(cents_leftover_after_quarters,10)
		if num_times_cents_leftover_after_quarters_into_dimes > 0:
			#use up dimes
			dimes_used = num_times_cents_leftover_after_quarters_into_dimes
			cents_leftover_after_dimes = cents_leftover_after_quarters - dimes_used*10
			coins_used.append(round(dimes_used))
		else:
			#too small cannot use dimes
			cents_leftover_after_dimes = cents_leftover_after_quarters
	else:
		pass
	if cents_leftover_after_dimes > 0:
		#there cents left to use up, can they go into nikels
		num_times_cents_left_over_after_dimes_into_nikels = num_times_coin_into_cents(cents_leftover_after_dimes,5)
		if num_times_cents_left_over_after_dimes_into_nikels > 0:
			#use up nikels
			nikels_used = num_times_cents_left_over_after_dimes_into_nikels
			cents_leftover_after_nikels = cents_leftover_after_dimes - nikels_used*5
			#add to coins used
			coins_used.append(round(nikels_used))
		else:
			#too small to use nikels
			cents_leftover_after_nikels = cents_leftover_after_dimes
	else:
		pass
	if cents_leftover_after_nikels > 0:
		#there are cents left to use up, can they go into pennies
		num_times_cents_leftover_after_nikels_into_pennies = num_times_coin_into_cents(cents_leftover_after_nikels,1)
		if num_times_cents_leftover_after_nikels_into_pennies > 0:
			#there are pennies to use up
			pennies_used = num_times_cents_leftover_after_nikels_into_pennies
			cents_left_overver_after_pennies = cents_leftover_after_nikels - pennies_used*1
			#add to coins used
			coins_used.append(round(pennies_used))
		else:
			pass
	else:
		pass
	return((sum(coins_used)))

print(min_num_coins(10000000))

import numpy as np 
print(np.arange(0,20,10))
