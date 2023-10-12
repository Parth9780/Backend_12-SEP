fir = int(input("Enter first subject marks : "))
sec = int(input("Enter second subject marks : "))
thr = int(input("Enter threed subject marks : "))
fort = int(input("Enter fourth subject marks : "))


total = fir + sec + thr + fort
print(total)

per = total/4
print(per)

if 70<=per:
    print("Dist.")
elif 60<=per:
    print("First class.")
elif 50<=per:
    print("Second class.")
elif 40<=per:
    print("Pass.")
else:
    print("Fall")
