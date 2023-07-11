#use of break
s="madeeha"
for i in s:
    if i=="h":
        break
    else:
        print(i)
print("This has break")
#use of continue and for with else
for i in range (0,7):
    if i%2==1:
        continue
    else:
        print(i)
else:
    print("This has continue")
print("\n")
#use of pass and while with else
j=1
while j<=10: 
        if i==7:    
            j+=1
            pass
        else:
            print(j)
        j+=1
else:
    print("This has pass")
