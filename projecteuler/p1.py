#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

//O(N) algorithm
sum=0
for i in range(1000):
	if(i%3==0 or i%5==0):
		sum=sum+i
print(sum)

//O(1) algorithm 4x faster
target = 999
def sumdiv(n):
	p= target//n
	return n*(p*(p+1))//2

print(sumdiv(3)+sumdiv(5)-sumdiv(15))
