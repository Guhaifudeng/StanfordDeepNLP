from numpy import *
nums = ones(1,int,5) + range(5)
print nums

print nums[2:4] # 2+1:4
print nums[:4]  # 0+1:4
print nums[4:]  # 4+1:5
print nums[:-1]
print nums[-1]
print nums[-1:]
nums[2:4] = [11,22]
print nums

print "-----------------------"
animals =[ 'cat','dog ','monkey']
for animal in animals:
    print animal
for idx ,animal in enumerate(animals):
    print "%d %s" % (idx + 1, animal)

print "----------------------------"
nums = [0, 2, 4, 8 ,10]
squares = []

for x in nums:
    squares.append(x ** 2)
print squares

squares_2  = [x ** 2 for x in nums] #list comprehension
print squares_2

print squares == squares_2

#List comprehensions can also contain conditions
print nums
even_squares = [x ** 2 for x in nums if x % 4 ]
print even_squares
