cars = 50
bicycles = 15
bikes = 30

if cars + bikes > bicycles:
	motors = cars + bikes
	print "There are %d motors on the streets." % motors

motors -= 75

if motors <= bicycles:
	print ("We are saved! We have %d people riding bicycles"
		" and %d jerks polluting the city!") % (bicycles, motors)


motors += 35

car_tires = cars * 4

bicycle_tires = bicycles * 2

bike_tires = bikes * 2

total_tires =  car_tires + bicycle_tires + bike_tires

print "Now we have %d tires on the streets!" % total_tires