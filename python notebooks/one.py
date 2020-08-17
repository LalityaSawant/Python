#one.py
#print('hello')

#built in variable
#__name__

def func():
	print("Func() in one.py")

print("Top Level in one.py")

if __name__ == '__main__':
	print('One.py is run directly')
	func()
else:
	print('One.py has been imported')