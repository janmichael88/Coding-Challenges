import numpy as np 

#write a function that returns the minimum number of coins to give out
#input is a number in cents
#inefficient way, try to improve!
def get_minimum_num_coins(cents):
	#define list of coins
	coins = [25,10,5,1]
	#define number of times per coin
	num_times_coin = []
	#define total history
	total_history = []
	#selection equal to cents
	equal_to_cents = []
	#combination equal to cents
	sum_coins = []
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
	for a in range(0,cents):
		for b in range(0,cents):
			for c in range(0,cents):
				for d in range(0,cents):
					#get total 
					total = coins[0]*a + coins[1]*b + coins[2]*c + coins[3]*d
					number_each_coin = [a,b,c,d]
					#pack together
					packed = [total,number_each_coin]
					#add to total history
					total_history.append(packed)
	#seach through total history to find values equal to cents
	for a,b in total_history:
		if a == cents:
			#store a and b
			packed_2 = [a,b]
			equal_to_cents.append(packed_2)
	#search through equal to cents
	for i,j in equal_to_cents:
		sum_coins.append(sum(j))
	return(min(sum_coins))
print(get_minimum_num_coins(80))

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
	#set inial count of coins 
	num_quarters = num_times[0]
	num_dimes = num_times[1]
	num_nickels = num_times[2]
	num_pennies = num_times[3]
	#remaining cents
	cents_leftover_after_quarters = cents
	cents_leftover_after_dimes = cents
	cents_leftover_after_nikels = cents
	cents_left_overver_after_pennies = cents
	#list of coins used up
	coins_used = []
	#go through quarters first
	if num_quarters > 0:
		#use up quarters first
		quarters_used = num_quarters
		cents_leftover_after_quarters = cents - quarters_used*25
		coins_used.append(round(quarters_used))
	else:
		only_quarters = num_quarters
		coins_used.append(round(only_quarters))
	if cents_leftover_after_quarters > 0:
		#there are cents to use up, can they go into dimes?
		num_times_cents_leftover_after_quarters_into_dimes = num_times_coin_into_cents(cents_leftover_after_quarters,10)
		if num_times_cents_leftover_after_quarters_into_dimes > 0:
			#use up dimes
			dimes_used = num_times_cents_leftover_after_quarters_into_dimes
			cents_leftover_after_dimes = cents_leftover_after_quarters - dimes_used*10
			coins_used.append(round(dimes_used))
		else:
			dimes_used = num_times_cents_leftover_after_quarters_into_dimes
			only_dimes = dimes_used
			coins_used.append(round(only_dimes))
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
			nikels_used = num_times_cents_left_over_after_dimes_into_nikels
			only_nikels = nikels_used
			coins_used.append(round(only_nikels))
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
			pennies_used = num_times_cents_leftover_after_nikels_into_pennies
			only_pennies = pennies_used
			coins_used.append(round(only_pennies))
	else:
		pass
	return((coins_used))

print(min_num_coins(130))





	















	while num_quarters < 0:
		left_over_after_quarters = cents - num_times[0]*25
		if left_over_after_quarters == 0:
			num_quarters = num_quarters - num_times[0]
			return_val_1 = num_times[0]
		else:


k=1
while k<10:
	print(k)
	k+=1


	







