if __name__ == "__main__":
	N = int(input())
	if ((N % 2 != 0) | ((N % 2 == 0) & (N >=6) & (N <= 20))):
    		print("Weird")
	if ((N %2 == 0) & (N > 20) | ((N % 2 == 0) & (N >= 2) & (N <= 4))):
    		print("Not Weird")
