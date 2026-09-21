#*******************************************start*******************************************

#to add a data in the table

def add_data(l):
    n=int(input("enter no of data "))
    for i in range(n):
        x=[]
        id=int(input("enter id :"))
        name=input("enter name of employee :")
        experince=int(input("enter experince in years :"))
        salary=int(input("enter salary :"))
        x=[id,name,experince,salary]
        l.append(x)
    return l

#to remove a data from table

def remove(l):
    a=int(input("enter the id of the employee to remove"))
    for i in l:
        if i[0]==a:
            l.remove(i)
    return l

#to show a data with id

def show(l):
    a=int(input("enter the id of the employee to display"))
    for i in l:
        if i[0]==a:
            print(i)

#to display all data 

def show_all(l):
    for i in l:
        print(i)

#main program's data

l=[["id","name","experince","salary"]]
flag=True

#main loop of program

while flag:    

    #to user choice

    print("-----plese select what you want to do-----")
    print("1 - for adding data")
    print("2 - for removeing data")
    print("3 - for show the spesific data")
    print("4 - for show all data")
    choice=int(input("enter your choice"))
    
    # to calling function

    if choice==1:
        l=add_data(l)
    elif choice==2:
        l=remove(l)
    elif choice==3:
        show(l)
    elif choice==4:
        show_all(l)
    else:
        print("invalid")

    #to check if user want to continue
    
    c=input("do you want to continue(y/n)")
    if c=="y":
        flag=False
    elif c=="n":
        print("thanks for using")
    else:
        print("invalid choice ")
#************************************end of program******************************************





