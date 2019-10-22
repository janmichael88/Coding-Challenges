import numpy as np
import pandas as pd 

#write function that takes in two strings and returns if strings are equal

def check_two_strings(string1,string2):
	#split strings 1 and 2 and get distance
	length_string1_split = len(list(string1.upper()))
	length_string2_split = len(list(string2.upper()))
	return(length_string1_split == length_string2_split)

#test the function
test_string1 = 'ABCD'
test_string2 = 'ABCD'

print(check_two_strings(test_string1,test_string2))

def check_two_strings_case_insenstive(s1,s2):
	#check the lengths
	if len(s1) != len(s2):
		return False
	#check first character in string
	if list(s1)[0] != list(s2)[0]:
		return(false)
	#make s1 and s2 iter objects
	s1_iter = iter(s1)
	s2_iter = iter(s2)
	s1_c = s1_iter.next()
	s2_c = s2_iter.next()
	if s1_c != st2_c:
			return False

print(check_two_strings_case_insenstive(test_string1,test_string2))










