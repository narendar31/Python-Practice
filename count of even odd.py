start=1
end=10
e_total=0
o_total=0
while start<=end:
     if start%2==0:
        e_total+=start
     else:
        o_total+=start
     start+=1
print("even:",e_total)
print("odd",o_total)