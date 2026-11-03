'''data = ('admin@gmail.com','admin@123')

gmail = input("Enter your email:")
password = input("Enter your password:")

if (gmail,password) == data:
    print("Login successful")
else:
    print("Invalid email or password")'''




'''seats = {
    's1':'Booked',
    's2':'Available',
    's3':'Available',
    's4':'Booked',
    's5':'Available',
    's6':'Available'
}

seatno = input("Enter your seat number:")

if seatno in seats and seats[seatno] == 'Available':
    seats[seatno] = 'Booked'
    print(f"{seatno} is booked successfully")
    print("Updated seat status:", seats)

else:
    print(f"{seatno} is not available for booking")'''





'''products={
    'laptop':{'price':40000,'stock':10},
    'mobile':{'price':20000,'stock':20},
    'tablet':{'price':15000,'stock':15},
    'headphones':{'price':5000,'stock':30},
    'keyboard':{'price':3000,'stock':0}

}

search_product = input("Enter the name of the product:")

if search_product in products and products[search_product]['stock'] > 0:
    print(f'you can buy {search_product} for Rs.{products[search_product]["price"]}')   
else:
    print(f'{search_product} is not available for purchase')'''





