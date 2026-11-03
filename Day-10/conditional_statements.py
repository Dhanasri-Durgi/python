'''product = input("Enter the product:")
Bestseller = eval(input("Enter the status:"))  #eval is used while we are taking bool as input

if Bestseller:
    print(f'{product} is a best seller')'''




'''batterycharge = int(input("Enter the battery charge percentage:"))
if batterycharge < 20:
    print("Battery is low, please charge your device.")'''




bill=int(input("Enter the bill amount:"))
status=eval(input("Is it raining?"))

if status:
    bill+=30
    print("Extra charge of 30 is added to the bill due to rain.")

print(f'the final bill amount is :{bill}')