print("Welcome to the weekend planner!")
budget = int(input("Enter your budget:"))

print("you can go for",end=" ")

if budget >10000:
    print("trip")
elif budget >5000:
    print("resort")
elif budget >2000:
    print("cafe")
elif budget >1000:
    print("movie")
elif budget >500:
    print("street shopping")
else:
     print("sleep")   