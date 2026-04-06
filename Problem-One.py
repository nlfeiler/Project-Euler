#original solution (brute force)
sum = 0
for i in range(1000):
    if(i % 3 == 0) or (i % 5 == 0):
        sum += i
print(sum)

#number theory solution after some research
target=999 

#a function that just gives the sum of an arithmetic series
#an arithemtic series sum is used here because multiples of a number is an increasing arithmetic series
def SumDivisibleBy(n):
    product=int(target/n)
    return n*(product*(product+1))/2

#now if we add the sum of all numbers divisible by 3 and 5 and subtract the ones divisible by 15 (i.e, the ones in both lists) then it will give us the proper sum of all below the target
print(SumDivisibleBy(3) + SumDivisibleBy(5) - SumDivisibleBy(15))