
arr1=int(input())
arr2=int(input())

for i in range (0,arr1,arr2):
    ratio=(arr1/arr2)        #arr1[i+1]
    if ratio >= 1.80 and ratio <= 1.90:
        print("Eureka" ,"[",arr1,",",arr2,"]")
        break
    else:
        print("again",end=" ")
        break
           
    
