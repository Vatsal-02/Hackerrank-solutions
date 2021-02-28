n = int(input())
marksheet = {}
for i in range(n):
    name, *marks = input().split() #* matlab name ko .split se list me dal and phir uske baad jo *marks dala hai usse mat daal usse alag rakh list se bhar lekin sab sath me le sab kuch ek sath
    scores = list(map(float, marks)) #map islye use kiya taaki saare elemets select ho
    marksheet[name] = scores

query_name = input()

m = list(marksheet[query_name]) #access the particular name from the dictonary marksheet
average = sum(m) / len(m)  #nicer way to find the average of the a list of numbers

print("{:.2f}".format(average))  #{:.2f}".format(average) -  get the decimal value of average upto 2 decimal places
  
