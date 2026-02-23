# Open a file for reading
demotextfile = open("06.00.00 DemoText.txt")
# Read through the file
for x in demotextfile:
# Print the contents - Note the imbedded linefeeds
	print(x)
# Close the file
demotextfile.close()