print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear
		print "The bear leaves a sword behind! What do you do?"
		
		sword_action = raw_input('> ')

		if sword_action == 'take the sword' or 'grab the sword' or 'carry the sword' or 'take sword' or 'grab sword' or 'carry sword' or 'take' or 'grab' or 'carry':
			print 'You take the sword and it starts to shine really bright highlighting a narrow passage right in front of you.'
			print 'Do you go through the passage?(y/n)'
			
			go_action = raw_input('> ')

			if go_action == 'y' or 'Y' or 'Yes' or 'YES' or 'yes':
				print 'You go through the narrow passage and end up findind yourself inside a mirror room!'
			
			else:
				print 'After a short amount of time the bear returns and eat you alive. Good job!'	

		else:
			print 'The door you opened closes and you starve to death. Good job!'

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

else:
	print "You stumble around and fall on a knife and die. Good job!"