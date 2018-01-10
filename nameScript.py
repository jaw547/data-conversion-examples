#Read from name.txt
with open('name.txt') as f:
	my_name = f.read()

#Create a new variable with the string you want.
writeMe = 'Hello, my name is ' + my_name + '.'

#Save the string to a new file.
with open('hello.txt', 'w') as f:
	f.write(writeMe)
	f.write('\n') 

#Print the variable to the console for ease.
print writeMe