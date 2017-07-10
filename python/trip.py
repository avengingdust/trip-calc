city = raw_input("Where will you be going?")
days = raw_input("How many days will you be staying?")
spending_money = raw_input("How much extra spenfing money will you bring?")
def hotel_cost(days):
    return days * 140				
    if len(nights) < 1:
        print "Invalid"
def plane_ride_cost(city):	
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
    else: 
        print "INVALID"
def rental_car_cost(days):
    cost = days * 40
    if len(days) > 1:
        return cost
    else:
        print "Invalid"
    """elif days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20"""
def spending_money():
	if len(spending_money) < 1:
		print "Invalid" 
	else: 
		return spending_money
def trip_cost(city, days, spending_money):
	return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print trip_cost(city, days, spending_money)











"""def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
print trip_cost("Los Angeles", 5, 600)"""
