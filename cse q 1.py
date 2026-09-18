#importing module

import array as ar

#data entery 

print("*********data entering*************")

n=int(input("enter no of student:"))
reg_no=ar.array('i',[])
mark=ar.array('f',[])
sum=0
for i in range(n) :
    a=[]
    r_no=int(input("enter last 5 no of registration no of student:"))
    m=float(input("enter marks of student:"))
    reg_no.append(r_no)
    mark.append(m)

    sum=sum+m

#printing data

print("*********registration number and  marks*************")


print("registration no:",reg_no)
print("marks:",mark)

#average of class

print("*********class avg*************")


class_avg=sum/n
print("class average",class_avg)

# maximum and minimum

print("*********maximum and minimum marks*************")

print("maximum=",max(mark))
print("minimum=",min(mark))

#mark more then avg

print("*********mark more then avg*************")

for i in mark:
    if i>class_avg:
        print(i)

