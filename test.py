
def getMissingNo(A):
    """missing no"""  
    n = len(A)    
    total = (n+1)*(n+2)//2
    # return total
    sum_of_A = sum(A)
    return total - sum_of_A 

A = [1, 2, 3,4,6,7] 
miss = getMissingNo(A) 
#print(miss)
# print(getMissingNo.__doc__ )



##max and min,second max  from list

def maxandmin(n):
    maxno=n[0]
    minno=n[0]
    largest2 = None
    for i in n:
        if i >maxno:
           largest2 = maxno
           maxno=i
        elif largest2 == None or largest2 < i:
            largest2 = i 
        if i < minno:
            minno=i
    return maxno,minno,largest2

n=[3,5,8,6,15,2,18]
max=maxandmin(n)
#print(max)



# def Range(list1):  
#     largest = list1[0]  
#     lowest = list1[0]  
#     largest2 = None
#     lowest2 = None
#     for item in list1[1:]:      
#         if item > largest:  
#             largest2 = largest 
#             largest = item  
#         elif largest2 == None or largest2 < item:  
#             largest2 = item  
#         if item < lowest:  
#             lowest2 = lowest 
#             lowest = item  
#         elif lowest2 == None or lowest2 > item:  
#             lowest2 = item  
              
#     print("Largest element is:", largest)  
#     print("Smallest element is:", lowest)  
#     print("Second Largest element is:", largest2)  
#     print("Second Smallest element is:", lowest2)  
  
  
# # Driver Code 
# list1 = [12, 45, 2, 41, 31, 10, 8, 6, 4] 
# Range(list1)



#find which number is not present in the second array.
# item = [0,1,2,3,4,5,6,7,8,9]
# z = [0,1,2,3,4,5,6,7]
# for elem in item:
#  if elem not in z:
   #print (elem)







#find sum with out third variable
# and  =>1 1 =>1  else 0
#  or=> 0 0 ->0 else 1
# xor =>both input same =>0 otherwise 1 
def fn(s):
  order = []
  counts = {}
  for x in s:
    if x in counts:
      counts[x] += 1
    else:
      counts[x] = 1 
      order.append(x)
      
  for x in order:
    if counts[x] == 1:
      return x
  return None 


print (fn('hhhhhhjjjjjjjjhhhphzhh'))


# repeating elements in a given array 
  
def printRepeating(arr, size): 
  
    print("Repeating elements are ", 
                         end = '') 
    repf=[]                     
    for i in range (0, size): 
        for j in range (i + 1, size): 
            if arr[j] == arr[i] and arr[i] not in repf  : 
                # print(arr[i], end = ' ')
                repf.append(arr[i]) 

    return repf      
      
# Driver code 
arr = [4, 2, 4, 5,5,5, 3, 1,1] 
arr_size = len(arr) 
#print(printRepeating(arr, arr_size)) 


# Returns number of pairs in arr[0..n-1]  
# with sum equal to 'sum' 
def getPairsCount(arr, n, sum): 
      
    count = 0
    count = 0
    dictd={} 
    for i in range(0, n): 
        for j in range(i + 1, n): 
            if arr[i] + arr[j] == sum:
                dictd[j]  =(arr[i] , arr[j])
                # print ((arr[i] , arr[j]))
                # print (dictd)
                count += 1
      
    return count,dictd 


arr = [1, 5, 7, -1, 5] 
n = len(arr) 
sum = 6
# print("Count of pairs is", 
#       getPairsCount(arr, n, sum)) 



