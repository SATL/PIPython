def f(x):
	return x**2
print f(8)

g = lambda x:x**2
print g(3)

#*************-------------------lambda Functions

def make_incrementor(n):
	return lambda x:x+n

f = make_incrementor(2)
g = make_incrementor(7)

print make_incrementor(5)(3)
print f(42), g(42)

foo = [2, 4, 3,7 ,12, 34]
# filt the array if is divisible by tree
flt = filter(lambda x:x%3==0, foo)
print flt
#each element of the array pass to the lambda
mp = map(lambda x:x*2+10, foo)
print mp

rdc = reduce(lambda x, y:x+y, foo)
print rdc

#********************--------------------Examples

#---Prime numbers of array
nums = range(2, 50)
isPrime = lambda x: x==i or x % i
print nums
#posible divisors
for i in range(2, 8):
	nums = filter(isPrime, nums)
print nums

#---Lenght of words
sentence = "I'm falling in love with python"
words = sentence.split()
print words
lengths = map(lambda word:len(word), words)
print lengths
print map(lambda w: len(w), "I'm falling in love with python".split())


#---mount points (Unix)
import commands
mount = commands.getoutput('mount -v')
print mount
lines = mount.splitlines()
points = map(lambda line: line.split()[2], lines)
print points

lines = commands.getoutput('mount -v').splitlines()
points = [line.split()[2] for line in lines]
print points