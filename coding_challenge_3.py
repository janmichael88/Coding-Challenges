import numpy as np 
import pandas as pd 
import os
from io import StringIO
import matplotlib.pyplot as plt
from collections import Counter

cwd = os.getcwd()
print(cwd)

path = "/Users/janmichaelaustria/Documents/Data Sets"
os.chdir(path)

cwd = os.getcwd()
print(cwd)

celebrities = pd.read_csv("celebrity_deaths_4.csv",header=0,encoding = 'unicode_escape')

celebrities.info

#view head of celebrities
celebrities.head(5)
celebrities.columns
columns_to_grab = ['birth_year','death_year']
celebrities_df = celebrities[columns_to_grab]

birth_death_years = celebrities_df.values
min_year = min(birth_death_years[:,0])
max_year = max(birth_death_years[:,1])

list_years = []
for i in range(birth_death_years.shape[0]):
    #get life span for the person
    life_span = birth_death_years[i,1] - birth_death_years[i,0]
    for j in range(life_span):
        #get the jth year
        j_year = birth_death_years[i,0] + j
        #add the year to list_years
        list_years.append(j_year)

array_list_years = np.array(list_years)
 
#get dictionary of counts from array
value_count = Counter(array_list_years)
max_value = max(value_count.values())

max_year_idx = []
max_year = array_list_years[max_year_idx]
for a,b in list(enumerate(value_count.values())):
    if b == max_value:
        to_index = a
        max_year_idx.append(to_index)
        

plt.hist(array_list_years)
plt.show()
#need to get the year that appears most in this list, and that's the answer

#first create a sorting function to sort the list
def selection_sort(arr):
    for eff in range(len(arr)):
        switch = eff + np.argmin(arr[eff:])
        (arr[eff], arr[switch]) = (arr[switch],arr[eff])
    return(arr)

len(list_years)
#need to filter out list of years that are repeated
filtered_list = []
for bah in list_years:
    if bah not in filtered_list:
        filtered_list.append(bah)









