#def fact(n):
#    ans=1
#    for i in range (1,n+1):
#        ans=ans*i
 #       
#    return print(" Factorial : ",ans)
    #
#a=int(input(" Enter A number : "))
#fact(a)
   
def students(l ,m ,n ,o):
    info = {}
    info.update({'roll' : a, 'name' : b,'age': c,'grades': d })
   
    return info

a=int(input(" Enter Your Roll No. : "))  # a=id,b=name , c=age,d =grades
b=input(" Enter Your name : ")
c=int(input(" Enter Your Age : "))
d=int(input(" Enter Your Grades  : "))

r=students(a,b,c,d)
print(r)
