# 5 X 5 squire
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# code
# for i in range(5):
#     for j in range(5):
#         print("*", end=' ')
#     print('\n')


################
# triangle
# *
# * *
# * * *
# * * * *
# * * * * *

# for i in range(5):
#     for j in range(i):
#         print("*", end=" ")
#     print()

###############

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# code
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

#####################


# * * * * *
# * * * *
# * * *
# * *
# *

# code:
# N=5
# for i in range(N):
#      for j in range(N-i):
#          print("*", end=' ')
#      print()

#################

#   *
#  ***
# *****

# Function to demonstrate printing pattern triangle
# n=3
# k = n - 1
# # outer loop to handle number of rows
# for i in range(0, n):
#
#     # inner loop to handle number spaces
#     # values changing acc. to requirement
#     for j in range(0, k):
#         print(end=" ")
#
#     # decrementing k after each loop
#     k = k - 1
#
#     # inner loop to handle number of columns
#     # values changing acc. to outer loop
#     for j in range(0, i + 1):
#         # printing stars
#         print("* ", end="")
#
#         # ending line after each row
#     print("\r")
#
# #######################

# n=3
# k=n
# for i in9 range(n):
#
#     for j in range(k+2,0,-1):
#         print('* ', end='')
#     print()
#     k-=1

#################################

#
# *****
#  ***
#   *
#
#
# #code
# n=3
# for i in range(n):
#     for j in range(0,i,1):
#         print(" ",end='')
#     for t in range(2*n-(2*i+1)):
#         print('*',end='')
#     print('\r')
# # ###############################
#   *
#  ***
# *****
# *****
#  ***
#   *
#
# # code
# n=6
# p=int(n/2)
# k=p-1
# u=int(n/2)
# for i in range(p):
#     for j in range(0,p-i-1):
#         print(" ",end='')
#     for k in range(0,2*i+1):
#         print("*",end='')
#     print("\r")
#
# for i in range(u):
#     for j in range(0,i,1):
#         print(" ",end='')
#     for t in range(2*u-(2*i+1)):
#         print('*',end='')
#     print('\r')


##############################

# *
# **
# ***
# ****
# ***
# **
# *
# # code:
# n=7
# mid=int(n/2)+1
# y=n-mid
# for i in range(0,mid+1):
#     for j in range(0,i):
#         print("*",end="")
#     print("\r")
# for t in range(y,0,-1):
#     for o in range(t):
#         print("*",end="")
#     print("\r")

####################################
# 1             1
# 1 2         2 1
# 1 2 3     3 2 1
# 1 2 3 4 4 3 2 1
# code::thoda esko dyan se observe karna guru logic bhut sahi likha hai bande ne.
# N=4
# for i in range(1, N + 1):
#     j = 1
#     s = N * 2 - 2
#     while j <= N * 2:
#         if j <= i:
#             print(j, end=' ')
#         elif j >= N * 2 - i + 1:
#             print(i, end=' ')
#             i -= 1
#         else:
#             print(' ', end=' ')
#         j += 1
#     print()
#
##########################################

# A
# AB
# ABC
# ABCD
# # code:::
# n = 5


# alph=65
# for i in range(n):
#     alph=65
#     for j in range(i):
#         print(chr(alph),end='')
#         alph=alph+1
#     print()
# #
# #3############################################
#
# n=5
# for i in range(n,0,-1):
#     alph=65
#     for j in range(i):
#         print(chr(alph),end='')
#         alph=alph+1
#     print("\r")
# ################################################
# * * * * * *
# *         *
# *         *
# *         *
# *         *
# * * * * * *

## code::
# n=6
# for i in range(n):
#     for j in range(n):
#         if(i!=0 and i!=n-1):
#             if(j!=0 and j!=n-1):
#                 print("  ",end='')# here we have to give 2 time gap
#             else:
#                 print("* ",end='')
#         else:
#             print("* ",end="")
#     print('\r')

################################################

########## RECURTION #################################################################################################################################


# def name(N):
#     if N==0:
#         return
#     else:
#         name(N-1)
#         print("Ashish will gonna be crack google india!!")
#         N-=1
#
#
# name(10)

#################################
# print 1 to n using recursion:

# def print1ton(n):
#     if n==0:
#         return
#
#     else:
#
#         print1ton(n-1)
#         print(n)
#
# print1ton(10)

#####################################
# sum of 1st n no:

# def sum1stn(N):
#
#     if N<=0:
#         return N
#     else:
#         return N+sum1stn(N-1)
#
# print(sum1stn(10))


# def recur_sum(n):
#    if n <= 1:
#        return n
#    else:
#        return n + recur_sum(n-1)
#
# print(recur_sum(10))

#############################


# def fect(n):
#     if n==1:
#         return n
#     else:
#         return n * fect(n-1)
# print(fect(5))

##################################

# reverse a array using recursion


# def swap(t, y):
#     # using 3 variable swap ker rhe ho :::::
#     # c=a[t]
#     # a[t]=a[y]
#     # a[y]=c
#     # return ---> eski jarurat hai nhi hai
#     # using 2 variable swap kiya hai :::::
#     a[t] = a[t] + a[y]
#     a[y] = a[t] - a[y]
#     a[t] = a[t] - a[y]
# def revarr(i, a, n):
#     if i >= int(n / 2):
#         return
#     swap(i, n - i - 1)
#     revarr(i + 1, a, n)
#
#
# import array as arr
# a = arr.array('i', [1, 2, 3, 4, 5, 6, 7])
# revarr(0, a, len(a))
# for i in a:
#     print(i,end=' ')
###u did it man!!, thats how ppl suceed keep doing !!!!
############################


# def check_palin(i,S,n):
#     if (i>=int(n/2)):
#         return 4
#         print(" ye chal rha1")
#     if S[i]==S[n-i-1]:
#         i=i+1
#     elif S[i]!=S[n-i-1]:
#         print("ye  chal rha hai 2")
#         return 3
#
# S=['m','a','d','a','m']
# t=check_palin(0,S,len(S))
# if t==4:
#     print("It's Palindrom!")
# elif t==3:
#     print("It's not Palindrom!!")
#
########################################

# print fibonacci series

# def fib(n,a,b):

##############################


#     if n-2==0:
#         return
#     else:
#         if a+b==1:
#             print(a,b,end=' ')
#         c=a+b
#         print(c,end=' ')
#         a=b
#         b=c
#         fib(n-1,a,b)
#
# fib(8,0,1)
##############################################################################################
# step1.6 basics of HASHING ####striver
##############################################################################################

# 5*10 KA ARRAY bna dega with prebuild value 3:
#
# arr2 = [[3 for col in range(5)] for row in range(10)]
# print(arr2)
###############################

# ydi meko size 10 ka prebuild value 0 ke sath array create karna ho to:

# arr=[0 for col in range(10)]

###############################
# HASHING MAIN CODE:
# ye number ke liye hoga bro:
#
# def prehash(arr):
#     max = 0
#     for i in arr:
#         if i > max:
#             max = i
#     brr = [0 for col in range(max+1)]
#     print(brr)
#     for j in arr:
#         brr[j]+=1
#     print(brr)
#     return brr
#
#
# def hash(brr, check):
#     return brr[check]
#
#

# k = int(input())
# arr= [int(input()) for col in range(k)]
# print(arr)
# brr= prehash(arr)
# check = int(input("enter the value to whom you have to check:"))
# print(hash(brr, check))
#
#
# ##YOU FINALLY WRITTEN THE HASHING CODE BRUUUU!!!
#
##########################################
# ye srting ke liye hona chahiye :::::-
#
# def hash(S,arr,I):
#     if I=='small':
#         for j in S:
#             t = ord('a') - ord(j)
#             # print("small ",t)
#             arr[t] += 1
#         y = ord('A') - ord(input("Bro kis character ka count check karna hai tumk"))
#         return arr[y]
#     elif I=='cap':
#         for j in S:
#             t = ord('A') - ord(j)
#             # print(t)
#             arr[t] += 1
#         y = ord('A') - ord(input("Bro kis character ka count check karna hai tumk"))
#         return arr[y]
#
#
#
# I= input("Is cap or small:")
# if(I=='small'):
#     arr=[0 for i in range(26)]
# elif(I=='cap'):
#     arr=[0 for i in range(26)]
# S=input("Please type the string:")
# print(hash(S,arr,I))

###################################i###########

## Find the highest and lowest frequency element :::

# def findminmax(arr):
#     max = 0
#     for i in arr:
#         if i > max:
#             max = i
#     brr = [0 for col in range(max+1)]
#     print(brr)
#     for j in arr:
#         brr[j]+=1
#     print(brr)
#     max = brr[0]
#     min = brr[0]
#     p=0
#     t=0
#     for i in range(len(brr)):
#         if brr[i]>max:
#             max = brr[i]
#             p=i
#
#         elif brr[i]<min:
#             min=brr[i]
#             t=i
#     return min,t,max,p
#
#
# k = int(input())
# arr= [int(input()) for col in range(k)]
# min,t,max,p= findminmax(arr)
# print('{0}->{1}and {2}->{3}'.format(min,t,max,p))
#
#
####################################################################
##SHORTING TECHNIC::::
#####################################################################
############***SELECTION SORT ####################:::
#
# def swap(t,y,arr):
#
#     # using 3 variable swap ker rhe ho :::::
#     c=arr[t]
#     arr[t]=arr[y]
#     arr[y]=c
#     # return ---> eski jarurat hai nhi hai
#     # using 2 variable swap kiya hai :::::
#     # arr[t] = arr[t] + arr[y]
#     # arr[y] = arr[t] - arr[y]
#     # arr[t] = arr[t] - arr[y]
#     # print(arr)
#     return arr
#
# def m(a,b,arr):
#     min=arr[a]
#     print("abhi ke liye ye arr[a]",min)
#     t=0
#     print("a and b:",a,b)
#     for k in range(a,len(arr)):
#         print("ye k hai :",k)
#         if(arr[k]<=min): # iski vajah se nhi ho rha hai min value
#             min=arr[k]
#             t=k
#             print("trace karne ke liye  k ko :", arr[t])
#     print("ye value hai min",arr[t])
#     return t
#
# arr= [50, 10, 3, 55, 80]
#
#
# for i in range(len(arr)):
#     print("this is i:", i)
#     l=m(i,(len(arr)-1),arr)
#     arr=swap(i,l,arr)
# print(arr)
#
#
################################################################
####33####### BUBBLE Sort ################33

# def swap(t,y,arr):
#     # using 3 variable swap ker rhe ho :::::
#     c=arr[t]
#     arr[t]=arr[y]
#     arr[y]=c
# def bubble(arr):
#     i=0
#     for i in range(0,len(arr)-i):
#         for j in range(0,(len(arr)-i)-1):
#             if(arr[j]>arr[j+1]):
#                 swap(j,j+1,arr)
#         i+=1
#     return arr
#
# arr=[10,9,7,5,3,2,1]
# bubble(arr)
# print(arr)

# @###@@@@@ Note if array is already sorted than it means O(1) eske liye 1st iteartion me koi swap nhi hoga  wha break ker do bus !!!
# ##########################  INSERTION SORT#################

# def swap(t,y,arr):
#     # using 3 variable swap ker rhe ho :::::
#     c=arr[t]
#     arr[t]=arr[y]
#     arr[y]=c
#
# arr=[13,14,9,15,12,6,8]
#
# for i in range(len(arr)):
#     for j in range(0,i):
#         if arr[i]<arr[j]:
#             swap(i,j,arr)
#
# print(arr)
#
#############################################
##########  MERGESORT      ###############
# def mergeSort(arr):
#     if len(arr) > 1:
#
#         # Finding the mid of the array
#         mid = len(arr) // 2
#
#         # Dividing the array elements
#         L = arr[:mid]
#
#         # Into 2 halves
#         R = arr[mid:]
#
#         # Sorting the first half
#         mergeSort(L)
#
#         # Sorting the second half
#         mergeSort(R)
#
#         i = j = k = 0
#
#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] <= R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#
#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
#
#
# # Code to print the list
# def printList(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=" ")
#     print()
#
#
# # Driver Code
# if __name__ == '__main__':
#     arr = [12, 11, 13, 5, 6, 7]
#     print("Given array is")
#     printList(arr)
#     mergeSort(arr)
#     print("\nSorted array is ")
#     printList(arr)
#
#######################################################

############# RECURSIVE BUBBLE SORT ALGO###################


# # Python Program for implementation of
# # Recursive Bubble sort
# class bubbleSort:
#
#
#     def __init__(self, array):
#         self.array = array
#         self.length = len(array)
#
#     def __str__(self):
#         return " ".join([str(x)
#                          for x in self.array])
#
#     def bubbleSortRecursive(self, n=None):
#         if n is None:
#             n = self.length
#         count = 0
#
#         # Base case
#         if n == 1:
#             return
#         # One pass of bubble sort. After
#         # this pass, the largest element
#         # is moved (or bubbled) to end.
#         for i in range(n - 1):
#             if self.array[i] > self.array[i + 1]:
#                 self.array[i], self.array[i +
#                                           1] = self.array[i + 1], self.array[i]
#                 count = count + 1
#
#         # Check if any recursion happens or not
#         # If any recursion is not happen then return
#         if (count == 0):
#             return
#
#         # Largest element is fixed,
#         # recur for remaining array
#         self.bubbleSortRecursive(n - 1)
#
#
# # Driver Code
# def main():
#     array = [64, 34, 25, 12, 22, 11, 90]
#
#     # Creating object for class
#     sort = bubbleSort(array)
#
#     # Sorting array
#     sort.bubbleSortRecursive()
#     print("Sorted array :\n", sort)
#
#
# if __name__ == "__main__":
#     main()
#

#######################################################################
######## RECURSIVE INSERTION SORT ################

# def Reinsertion(arr,i ,n):
#     if i==n:
#         return
#     j=i
#     while(j>0 and arr[j-1]>arr[j]):
#         temp=arr[j-1]
#         arr[j-1]=arr[j]
#         arr[j]=temp
#         j-=1
#     Reinsertion(arr,i+1,n)
#
# arr=[22,4,56,78,9,0]
# Reinsertion(arr,0,len(arr))
# print(arr)
#
#
###################################################
########### Quick Short#################

# Function to find the partition position
# def partition(array, low, high):
#
# 	# Choose the rightmost element as pivot
# 	pivot = array[high]
#
# 	# Pointer for greater element
# 	i = low - 1
# 	#
# # Traverse through all elements
# # compare each element with pivot
# for j in range(low, high):
# 	if array[j] <= pivot:
#
# 		# If element smaller than pivot is found
# 		# swap it with the greater element pointed by i
# 		i = i + 1
#
# 		# Swapping element at i with element at j
# 		(array[i], array[j]) = (array[j], array[i])
#
# # Swap the pivot element with
# # the greater element specified by i
# (array[i + 1], array[high]) = (array[high], array[i + 1])
#
# # Return the position from where partition is done
# return i + 1


# Function to perform quicksort
# def quicksort(array, low, high):
# 	if low < high:
#
# 		# Find pivot element such that
# 		# element smaller than pivot are on the left
# 		# element greater than pivot are on the right
# 		pi = partition(array, low, high)
#
# 		# Recursive call on the left of pivot
# 		quicksort(array, low, pi - 1)
#
# 		# Recursive call on the right of pivot
# 		quicksort(array, pi + 1, high)
#
#
# # Driver code
# if __name__ == '__main__':
# 	array = [10, 7, 8, 9, 1, 5]
# 	N = len(array)
#
# 	# Function call
# 	quicksort(array, 0, N - 1)
# 	print('Sorted array:')
# 	for x in array:
# 		print(x, end=" ")
######################################################################################################################################
################################################### NOW PLAY WITH ARRAY ######################################

##########Find max in array ########

# def highinarr(arr):
# 	max=arr[0]
# 	for i in arr:
# 		if max<i:
# 			max=i
# 	return max
#
# arr=[12,3,23,34,56,678,8967,2]
# print(highinarr(arr))
#
##############################################
# Check if array is sorted

# def Isarrshorted(A):
#     for i in range(0,len(A)-1):
#         if A[i]<=A[i+1]:
#             continue
#         else:
#             return 2
#     return 3
# A=[1,3,4,5,6,52]
# I=Isarrshorted(A)
# print(I)
# if I==2:
#     print("Array is not shorted")
# elif I==3:
#     print("array is shorted")
#
############################################################
# remove the duplicate ele from shorted array:

# def Trimdupele(arr):
#     brr=[]
#     for i in range(len(arr)-1):
#         if arr[i]!=arr[i+1]:
#             brr.append(arr[i+1])
#     return brr
#
#
# arr=[12,12,13,14,15,15,16,77,88,88,99,400,400,500,500,500]
# print(Trimdupele(arr))
#
##################################################################

#####Right Rotate the Array by One ############
# def r(a):
#    o=a[len(a)-1]
#    p1=a[0]
#    for i in range(0,len(a)-1):
#        p=a[i+1]
#        a[i+1]=p1
#        p1=p
#    a[0]=o
#    return a
#
#
# a=[4,3,5,4,6,67,9,90]
# print(r(a))

############################################################
##Letf rotate the array by d element :
# def dtimerotate(arr,n,d):
#     d=d%n
#     l=[0 for i in range(d)]
#     for i in range(0,d):
#         l[i]=arr[i]
#     for i in range(d,n):
#         arr[i-d]=arr[i]
#     for i in range(n-d,n):
#         arr[i]=l[i-(n-d)]
#     return arr
#
#
# arr=[2,23,89,23,3,4,5,3,12]
# print("intial array:",arr)
# print(dtimerotate(arr,len(arr),int(input("how many time do u want to left rotate the array:"))))


#######################################################################
# def swap(t, y):
#     # using 3 variable swap ker rhe ho :::::
#     # c=a[t]
#     # a[t]=a[y]
#     # a[y]=c
#     # return ---> eski jarurat hai nhi hai
#     # using 2 variable swap kiya hai :::::
#     arr[t] = arr[t] + arr[y]
#     arr[y] = arr[t] - arr[y]
#     arr[t] = arr[t] - arr[y]
# # def all0atlast(arr):
# #     j=len(arr)-1
#     for i in range(len(arr)):
#         if arr[i]==0 and i<j:
#             while arr[j]==0:
#                 j-=1
#             swap(j,i)
#     return arr
#
# arr=[2,0,3,0,5,0,6,0,8,0,99,0,90,99,0,45,40,0,0,5,0,3,0,2,0]
# print(all0atlast(arr))

########## Linear search  ###############################

# def Liearsearch(arr,n):
#     for i in range(len(arr)):
#         if arr[i] == n:
#             return i
#     return -1
#
# arr=[2,3,1,4,5,6,0]
# k=Liearsearch(arr,5)
# if k==-1:
#     print("No not exist")
# else:
#     print("index of u r value:",k)

#############################################################
######### union of array##############

# def unionarr(arr,brr):
#     for i in brr:
#         if i not in arr:
#             arr.append(i)
#     return arr
#
# arr=[2,4,6,8,0,12]
# brr=[4,56,6,7,0,12]
# print(unionarr(arr,brr))

########################################################
#### For this question I can think in 2 approach :::
###APPROACH1:
# def Missingele(arr,N):
#     for i in range(1,N-1):
#         if i == arr[i-1]:
#             pass
#         else:
#             return i
#
#
# arr=[1,2,3,4,5,6,7,9,10]
# N = len(arr)+1
# print(Missingele(arr,N))

###APPROACH2 : optimal solution
# def Missingele(arr,N):
#     s1=N*(N+1)//2
#     s2=0
#     for i in arr:
#         s2+=i
#     return s1-s2
#
# arr=[1,2,3,4,5,6,7,8,9,11]
# N = len(arr)+1
# print(Missingele(arr,N))

########################################################

###Count Maximum Consecutive One’s in the array


# def max_conse(arr):
#     count1=0
#     count2 = 0
#     for i in arr:
#         if i == 1:
#             count1 += 1
#         elif i == 0 and count1 > count2:
#             count2 = count1
#             count1=0
#     if count1 > count2:
#         count2 = count1
#     return count2
#
#
# arr = [1, 0, 1, 1, 0, 0, 1, 1, 1,1,1,1,1,1,0]
# print("max consecutive one's in array", max_conse(arr))

###############################################################

## find the no which will appear once in array
# in this way I can able to think in hashing way only :::
# -> find max -> max+1 array -> no add+1


# arr=[1,2,2,3,3,5,5,6,6,7,8]
# y=max(arr)
# hash=[0 for i in range(y+1)]
# for i in arr:
#     hash[i]+=1
# for i in range(len(hash)):
#     if hash[i]==1:
#         print(i,end=' ')
#

##################################################
# Longest subarray with given sum (k)
# def lenOfLongSubarr(arr, N, K):
#
# 	maxlength = 0
#
# 	for i in range(0,N):
#
# 		# Variable to store sum of subarrays
# 		Sum = 0
#
# 		for j in range(i,N):
#
# 			# Storing sum of subarrays
# 			Sum += arr[j]
#
# 			# if Sum equals K
# 			if (Sum == K):
#
# 				# Update maxLength
# 				maxlength = max(maxlength, j - i + 1)
#
# 	# Return the maximum length
# 	return maxlength
#
# # Driver Code
# # Given input
# arr = [ 10, 5, 2, 7, 1, 9 ,0,0,0,0,0,0,0,15]
# n = len(arr)
# k = 15
#
# # Function Call
# print("Length = " , lenOfLongSubarr(arr, n, k))

####################################################

#if u find the array 0 in doubly array than make row and coloum 0 thats it...

# explaination :
# arr=[[1,0,1],[2,4,5],[3,6,9]] ---> input
# arr=[[0,0,0],[2,0,5],[3,0,9]-->output
# arr=[[1,0,1],[2,7,5],[3,6,9]]
# dics={}
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j]==0:
#             dics[i]=j
#
# for i in dics.items():
#     print(i)
#     for j in range(len((arr[i[0]]))):
#         arr[i[0]][j]=0
#     for p in range(len(arr)):
#         arr[p][i[1]]=0
# print(arr)
########################################################

####1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

##2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

##Note: You are not allowed to use the same element twice. Example: If the target is equal to 6 and num[1] = 3,
## then nums[1] + nums[1] = target is not a solution.
#O(N^2)
# arr=[1,4,5,6,9,20,3]
# T=23
# u=0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if T== arr[i]+arr[j]:
#             print("Yes")
#             u=1
#             print('index of the elements:',i,j)
#             break
# if u!=1:
#     print("No")

# optomized wa:y:o(N)---> here basically we are using the dictonary concept

# dict={}
# T=9
# arr=[2,3,5,0,5,8,6]
# for i in range(len(arr)):
#     if dict.get(T-arr[i])!=None:
#         print(i,dict.get(T-arr[i]))
#     else:
#         dict[arr[i]]=i

############################################
##Sort an array of 0s, 1s and 2s
# many ways to short this array:
#   1 ST WAY :::  Brutforce 2*2 loop-->O(N^2)
# 2ND WAY :::  O(n)--> COUNT HOW MANY 0S , 1S AND 2S and than create a array like that
## 3RD WAY :::  DUTCH NATIONAL FLAG ALGO:: 0s 1s unshorted 2s

# def sort012(arr, n):
# 	# Initialisation
# 	l = 0
# 	r = n - 1
# 	i = 0
# 	while i < n and i <= r:
# 		# current element is 0
# 		if arr[i] == 0:
# 			arr[l], arr[i] = arr[i], arr[l]
# 			l += 1
# 			i += 1
# 		# current element is 2
# 		elif arr[i] == 2:
# 			arr[i], arr[r] = arr[r], arr[i]
# 			r -= 1
# 		# current element is 1
# 		else:
# 			i += 1
# def printArray(arr, arr_size):
# 	# Iterate and print every element
# 	for i in range(arr_size):
# 		print(arr[i], end=" ")
# # Driver Code
# if __name__ == "__main__":
# 	arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# 	n = len(arr)
#     sort012(arr, n)
# 	printArray(arr, n)
########################################
##Find the Majority Element that occurs more than N/2 times:::

# arr=[1,2,2,1,1,0,2,2,2]
# dict={}
# for i in arr:
#     if dict.get(i)==None:
#         dict[i]=1
#     else:
#         dict[i]+=1
# m=0
# for i in dict:
#     print(dict[i])
#     if i>m:
#         m=i
# print(m)
###############################################







