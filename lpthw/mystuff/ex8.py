# Set variables with format character inside it that turns everything 
# (python object) into a string using repr()
formatter = "%r %r %r %r"

# prints variable with integers as strings
print formatter % (1, 2, 3, 4)
# prints variable with strings as strings
print formatter % ("one", "two", "three", "four")
# prints variable with python keywords as strings
print formatter % (True, False, False, True)
# prints variable with the same variable as strings
print formatter % (formatter, formatter, formatter,formatter)
# prints variable with separeted by comma strings as strings
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)