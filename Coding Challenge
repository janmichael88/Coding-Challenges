import numpy as np 
import pandas as pd 

#given a list of points [2,3], [3,1] [-2 1], [0,4] [4,2]
#near [1,3]
#return 3 closest

set_points_1 = [[2,3], [3,1], [-2,1], [0,4], [4,2]]
center_1 = [-3,2]
#then return 3 closest
k_1 = 3
#define funciton that takes in two inputs, 1 input is a point, the other is center
def find_distance(start_point,end_point):
	#get x cooridante of start_point
	x_start = start_point[0]
	#get y coordinate of start point
	y_start = start_point[1]
	#get x cooridante of end_point
	x_end = end_point[0]
	#get y coordinate of start point
	y_end = end_point[1]
	#get distance
	distance = np.sqrt((x_end - x_start)**2 + (y_end-y_start)**2)
	return(distance)

#create function that takes in list of points, and returns k neartest center_point
def get_points_near_k(list_points,center_point,k):
	#output of list of distances by point
	list_of_distances = np.zeros(len(list_points))
	for i in range(len(list_points)):
		distance_1 = find_distance(list_points[i],center_point)
		list_of_distances[i] = distance_1
	#get indices of list_of_distances when sorted
	dist_indices = [idx[0] for idx in sorted(enumerate(list_of_distances),key=lambda x:x[1])]
	#create vector of ordered points by distance
	ordered_points = []
	#loop over dist indices
	for j in range(len(dist_indices)):
		#get index from dist_indices:
		dist_idx = dist_indices[j]
		#add odered pair to list
		ordered_points.append(list_points[dist_idx])
	return(ordered_points[0:k])

print(get_points_near_k(set_points_1,center_1,k_1))



####
def reverse(x):
	output = []
	output_index = len(x) - 1
	for c in x:
		output[output_index] = c
		output_index -= 1
	return output 

b='sljfgljnadjg'

reverse(b)
