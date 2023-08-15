sub1=int(input("First subject: "))
sub2=int(input("Second subject: "))

avg=(sub1+sub2)/2

if avg>=90:
    print("Grade: A")
elif avg>=80 & avg<90:
    print("Grade: B")
else:
    print("Grade: C")
