# _*_ coding: utf-8 _*_

from sys import argv

script, user_name, age = argv
prompt = 'Type your answer here: '
age = int(age)
year = 2016 - age

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
You have a %r computer and you were born in %d. Nice.
""" % (likes, lives, computer, year)