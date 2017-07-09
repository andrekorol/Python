name = 'Zed A. Shaw'
age = 35.0 # not a lie
height = 74.0 # inches
weight = 180.0 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
cm_height = height * 2.54
kg_weight = weight * 0.453592

print "Let's talk about %s." % name
print "He's %d centimeters tall." % cm_height
print "He's %d kilograms heavy." % kg_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d" % (age, height, weight, age + height + weight)