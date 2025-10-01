def print_age(YOB):
	print("You are: ", 2025- YOB)
	
if __name__ == '__main__':
	import sys
	BY = int(sys.argv[1])
	print_age(BY)
