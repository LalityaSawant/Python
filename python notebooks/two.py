#two.py
import one
print("Top level in two.py")

one.func()

if __name__ == '__main__':
	print("Toe.py is run directly")
else:
	print("two.py is imported")