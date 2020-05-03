#create levensthein as naive recursive call
'''
if the last two chars of two strings are the same, 
nothing to do, ignore last character and get count of remaining strings
recure for lengths m-1,and n-1
else (if last characters are not the same) consider all operations on str1
consider all three opertaions on the last char of first string
recursively copmute minimum cost for all three operations
insert: recur for m and n-1
remove recur for m-1 and n
replaces recur for m-1 and n-1
'''

def min_edit_distance(str1, str2):
	#get lengths
	m = len(str1)
	n = len(str2)
	if m == 0:
		return(n)
	if n == 0:
		return(m)
	#if the last two chars the the same, return and get counts for the smaller of the strings
	if str1[m-1] == str2[n-1]:
		return(min_edit_distance(str1[:m-1],str2[:n-1]))
	#if the last chars in the strings are not the same
	#consider all operations on the last char of the frist string
	#recursively compute the minimum cost for all three
	#return the min of the three values
	return(1+ min(min_edit_distance(str1,str2[:n-1]),
		min_edit_distance(str1[:m-1],str2),
		min_edit_distance(str1[:m-1],str2[:n-1])))

print(min_edit_distance(';kdrgkjfg',';dkfk;fngjk'))


#########
#Dynamic programming method
'''
to call min_edit_distance(3,3), min_edit_distance(2,2 ) must be called three timres
the time complexity can 3^m....which is really bad
store result of subproblems in a growing array
'''

def min_edit_distance_DP(str1,str2):
	#get lenghts
	m = len(str1)
	n = len(str2)
	#storeage for result of subproblems
	results = [[0 for x in range(n+1)] for x in range(m+1)]
	#fill results in bottom up manner
	for i in range(m+1):
		for j in range(n+1):
			#if the ith element of the the first string is empty, all elements of second string must be inserted
			if i == 0:
				results[i][j] = j
			#if the jth elememnt of the second string is emplty, all element of first string must be inserted
			elif j == 0:
				results[i][j] = i
			#if the last characters are the same, skip them and recur through i-1 and j-1
			elif str1[i-1] == str2[j-1]:
				results[i][j] = results[i-1][j-1]
			#if the last  chars are the same, consider all, and take min add 1
			else:
				results[i][j] = 1 + min(results[i][j-1],results[i-1][j],results[i-1][j-1])
	return(results[m][n])

print(min_edit_distance_DP('kittens','smitten'))







print([[0 for x in range(0,10)] for x in range(3)])


