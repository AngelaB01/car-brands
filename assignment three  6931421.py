#list of available cars and their prices
cars = {
'Mercedes-Benz': 80000,
'Scion': 45000,
'Chevrolet':35000,
'Ford Explorer':50000,
'Kia':22000,
'Honda':25000,
'Hyundai':34000,
'Volvo':21000,
'Toyota Corolla':55000,
'BMW':45000,
'Porche':56000,
'Ford':92000,
'Nissan':51000,
'SUV':23000,
'Acura':98000,
'lamborghini':62000,
'Volkswagen':74000,
'LandRover':63000,
'Infinity':99000,
'GMC':69000,
'Mitsubishi':43000,
'Chrysler':60000,
'Dodge':80000,
'Cadilac':90000,
'Lincoln':45700,
'Mini':94500,
'Audi':30000,
'Lexus':40000,
'Subaru':87000,
'Mazda':89000
}
# get user input for car name
carName = input('Enter a carName: ')
# check if car name is in the list of available cars
if carName in cars:
 print('Yes')
 #if car name is present, get its price
 carPrice = cars[carName]
 print(f'The price of {carName} is ${carPrice}.' )
else:
 # if car name is not present, inform the user
 print(f'Sorry, {carName} is not available at the moment.' )
 
github.com/AngelaB01