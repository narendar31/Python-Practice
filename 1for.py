#10
print("---------------")
m=2
for i in range(1,11):
        print(m,"X",i,"=",m*i)


#9
print("---------------")
'''     n       i       j
        1       1       1
        2       1       2
        3       1       3
        2       2       1
        4       2       2
        6       2       3
        3       3       1
        6       3       2
        9       3       3
'''

for i in range(1,4):
       for j in range(1,4):
           print(i*j,end=",")
       print()


#8 fibanacci
print("---------------")
n1=0
n2=1
next=0
'''          next = n1   n2 
              1      0    1
              2      1    2
              3      1    2
              5      2    3
              8      3    5 
              13     5    8
              21     8    13                
'''
print(n1,n2,end=",")
for i in range(1,8):
    next=n1+n2
    print(next,end=",")
    n1,n2=n2,next
print("\n  ")


#7 factorial
print("---------------")
fact=1
'''
    fact= fact * 1
    1        1    1
    2        1    2
    6        2    3
    24       6    4
    120      24   5     
'''
for i in range(1,6):
    fact = fact*i
print(fact)




#6
print("---------------")
for n in [10,20,40,69,46,35]:
    print(n)

#5
print("---------------")
city='california'
for s in city:
    print(s)


#4
print("-----------")
for j in reversed (range(1,11,)):
    print(j)

#3
print("---------------")
for x in range(1,11,4): #using step
    print(x)


#2


print("---------------")
for x in range(1,11,):
    print(x)

#1
print("---------------")
for i in range(10):
    print(i)
    #i=i+1

