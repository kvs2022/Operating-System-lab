def no(lt):
    for i in range(len(lt)):
        for j in range(i+1,len(lt)):

                if lt[i]>lt[j]:
                    temp=lt[i]
                    lt[i]=lt[j]
                    lt[j]=temp
            
    return lt

n=int(input('Enter the total number of elements = '))
l=[]
for j in range(n):
    ele=eval(input('Enter a number = '))
    l.append(ele)
lt1=no(l)
print("Sorted numbers in ascending order = ")
for x in range(len(lt1)):
    print(lt1[x],end=',')
