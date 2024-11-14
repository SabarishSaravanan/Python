#Given an array arr, the task is to find the largest element in it.

from array import array
vals = input("Enter space-separated numbers: ")

vals_list = list(map(int, vals.split()))
arr = array('i', vals_list)

#using recursive
larger=arr[0]
for i in range(0,len(arr)):
    if larger<=arr[i]:
        larger=arr[i]
print(larger)


"""
other methods
using brute force approach
use sorting
 """

