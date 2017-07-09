def hotel_cost(nights):	
	nights = raw_input("How long will you be staying?")
	return nights * 140				
	if len(nights) < 1:
		print "Invalid"
def plane_ride_cost(city):	
	city = raw_input("Where will you be going")
	if len(city) < 1:
		print "Invalid"
	elif city == "Charlotte":
		return 183
	elif city == "Tampa":
		return 220
	elif city == "Pittsburgh":
		return 222
	elif city == "Los Angeles":
		return 475
def rental_car_cost(days)
	days = raw_input("How many days will you require a car")
	cost = days * 40
	if len(days) < 1:
		print "Invalid"
	elif days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost
def spending_money()
	spending_money = raw_input("How much cash will you bring?")
	if len(spending_money) <1:
		print "Invalid"
	else 
		return spending_money:
def trip_cost(city, days, spending_money):
	return rental_car_cost(days) + hotel_cost(nights) + plane_ride_cost(city) + spending_ money









"""def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print trip_cost("Los Angeles", 5, 600)"""
