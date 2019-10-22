#question
#given a dictionary of words in some different languae, but in order
#example if alphabet is b f g q
#and list is bog, fbq, fqf, ffq, gfg
#find a way to first determine order
#then from the order write another function that will take in a list of words and sort them


def get_first_letters(listt):
	ordered_first_letters = []
	for word in listt:
		#extra first letter
		first_letter = list(word)[0]
		#add the 
		ordered_first_letters.append(first_letter)
	#remove duplicated
	duplicates_removed = []
	for letter in ordered_first_letters:
		if letter not in duplicates_removed:
			duplicates_removed.append(letter)
	return(duplicates_removed)

test_list = ['lanf','fksh','wpei','suob','soren']
print(get_first_letters(test_list))
#in this case l > f > w > s > s

#write function that takes in two words and alphabetizes them
def alphabetize_two(word1, word2):
	#get length of words
	len_word1 = len(list(word1))
	len_word2 = len(list(word2))
	
