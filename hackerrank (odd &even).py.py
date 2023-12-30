n=int(input("n:"))
if n % 2==0 and n in range(2,6):
    print("not weird")
elif n %2==0 and n in range(6,21):
    print("weird")
elif n%2==0 and n>20:
    print("not wierd")
else:
    print("wierd")
    

